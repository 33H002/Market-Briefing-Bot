from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CHANNELS_FILE = BASE_DIR / "config" / "slack_channels.yaml"
BOT_ENV_FILE = BASE_DIR / "config" / "slack_bot.env"


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def load_channels(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Slack channels config not found: {path}")
    channels: dict[str, dict[str, str]] = {}
    in_channels = False
    current_key: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.strip() == "channels:":
            in_channels = True
            continue
        if not in_channels:
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 2 and line.endswith(":"):
            current_key = line[:-1]
            channels[current_key] = {}
            continue

        if indent == 4 and current_key and ":" in line:
            field, value = line.split(":", 1)
            channels[current_key][field.strip()] = value.strip().strip('"').strip("'")

    if not channels:
        raise ValueError("Invalid slack channels config: no channels found.")
    return channels


def resolve_channel(channels: dict, channel_key: str, fallback_key: str | None) -> tuple[str, dict]:
    config = channels.get(channel_key)
    if config:
        return channel_key, config
    if fallback_key:
        fallback = channels.get(fallback_key)
        if fallback:
            return fallback_key, fallback
    available = ", ".join(sorted(channels.keys()))
    raise KeyError(f"Channel key `{channel_key}` not found. Available keys: {available}")


def read_message(args: argparse.Namespace) -> str:
    if args.message:
        return args.message
    if args.message_file:
        return Path(args.message_file).read_text(encoding="utf-8")
    raise ValueError("Provide either --message or --message-file.")


def send_message(token: str, channel_id: str, message: str) -> dict:
    body = json.dumps(
        {
            "channel": channel_id,
            "text": message,
            "unfurl_links": False,
            "unfurl_media": False,
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if not payload.get("ok"):
        raise RuntimeError(f"Slack API error: {payload.get('error', 'unknown_error')}")
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Send a Slack message with a bot token.")
    parser.add_argument("--channel-key", required=True, help="Channel key in config/slack_channels.yaml")
    parser.add_argument("--fallback-key", help="Fallback channel key if --channel-key is missing")
    parser.add_argument("--message", help="Inline Slack message text")
    parser.add_argument("--message-file", help="Path to a UTF-8 text file containing the Slack message")
    parser.add_argument("--dry-run", action="store_true", help="Print resolved channel and message without sending")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    load_env_file(BOT_ENV_FILE)
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "SLACK_BOT_TOKEN is not set. Fill config/slack_bot.env or export the environment variable."
        )

    channels = load_channels(CHANNELS_FILE)
    resolved_key, channel = resolve_channel(channels, args.channel_key, args.fallback_key)
    channel_id = channel.get("channel_id")
    if not channel_id:
        raise ValueError(f"Channel `{resolved_key}` does not have a channel_id.")

    message = read_message(args).strip()
    if not message:
        raise ValueError("Slack message is empty.")

    if args.dry_run:
        print(
            json.dumps(
                {"channel_key": resolved_key, "channel_id": channel_id, "message": message},
                ensure_ascii=False,
            )
        )
        return 0

    payload = send_message(token, channel_id, message)
    print(
        json.dumps(
            {
                "ok": True,
                "channel_key": resolved_key,
                "channel_id": payload.get("channel"),
                "ts": payload.get("ts"),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, KeyError, ValueError, RuntimeError, urllib.error.URLError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
