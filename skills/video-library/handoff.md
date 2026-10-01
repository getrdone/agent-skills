# Web / cloud handoff

The canonical database lives on Steve's computer. A cloud sandbox's localhost or G: path is not that computer. Use only tools actually available in the current session.

1. If authorized local filesystem or connected-computer tools are available, run the library intake on the connected computer and verify the result.
2. Otherwise use an available supported chat-messaging tool to send the video request to the local ChatGPT Work/Codex library chat. Resolve the destination from the user's named chat or local `video-library/handoff-target.json` when accessible. With `list_threads`, match the exact title **Build YouTube video archive**, verify the context, then use `send_message_to_thread`. Do not invent a chat ID, start a new user-owned chat, or claim a cloud tool exists because a desktop tool has the same name. The user's standing instruction authorizes this scoped handoff.
3. Include all URLs, request purpose, originating chat/message link or stable identifier, requested time, known title/channel/category, any already-created complete transcript or accessible artifact URL, actual acquisition time if known, and missing work. Preserve the same request_id across delivery retries. Each genuinely new user request gets a new request_id; each video within the request is counted once.
4. Verify tool confirmation. Say **handoff delivered; local download pending** until local completion is confirmed. A sent note is not proof that SQLite or transcripts were updated.
5. If messaging is unavailable or fails, provide a clearly labeled **Video Library — pending local handoff** note (and JSON file when useful). Explicitly say it has not been sent. Ask the user to pass it to the local library chat. Do not silently drop the request or claim cross-platform automation is installed when only a local skill exists.

## Receiver

Record the request before downloading. The local utility `_tools/import-handoff.py NOTE.json` imports this shape idempotently; add `--fetch` only to fetch immediately. Retrieval retries never add another request. The utility imports only inline transcripts explicitly marked complete; validate the content first. Other attached files can be imported using the library CLI after confirming source access.

```json
{
  "request_id": "source-chat-id:source-message-id",
  "requested_at": "2026-09-29T00:00:00Z",
  "source_chat": "original chat link or identifier",
  "purpose": "Create transcript and evaluate usefulness",
  "videos": [{
    "url": "https://www.youtube.com/watch?v=VIDEO_ID",
    "category": "Content creation",
    "subcategory": "Storytelling",
    "transcript_complete": false
  }]
}
```

Optional per-video fields: `transcript_text`, `transcript_complete`, `downloaded_at`. Unknown dates stay null. A receiving agent must return the library record/count and saved artifact status, or identify the concrete missing access.

## Installing defaults

Local agents: the authoritative `_tools/agent-homes.json` distribution and startup-context/install tools make this a default. For ChatGPT web, install an equivalent custom instruction or a supported plugin containing this skill in the actual signed-in account; local filesystem publishing alone does not install it in web chats. Keep existing instructions. Cross-agent capture is best-effort instruction routing, not a platform-enforced hook.
