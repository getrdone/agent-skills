# Local Whisper sidecar

Existing runner: `G:/__ai-projects/_agent-tools/whisper-local/whisper_local.py`.
Read its README for current status and configuration. It uses an isolated environment and existing GPU/model configuration. Do not install another service.

For a video with no useful captions and an authorized transcript request:

1. Record the URL with the video library before starting transcription. Resolve the canonical URL from the existing video record; do not add another request just to retry.
2. Use a project-local job folder `_wip/whisper/<video-id>/`. Start the existing detached worker with `py G:/__ai-projects/_agent-tools/whisper-local/whisper_local.py start --url URL --output-dir JOB_FOLDER`.
3. Check `status --job JOB_FOLDER --json`. The runner retains resumable checkpoints. Do not start duplicate jobs or treat time elapsed as failure. Preserve errors.
4. After successful completion, import its full `transcript.srt` (preserves cue times) or verified complete Markdown into `library.py import-transcript VIDEO_KEY PATH`. Label it local ASR in notes; timing follows source segments, not independently verified word alignment. The source JSON carries quality/timing evidence.
5. Run the current clean-video-transcript skill when editorial cleanup is requested. Preserve full speech, references, and source files; then import the final transcript without adding a new user-request event.

The existing runner currently focuses on YouTube input. Other video URLs can still be catalogued and their supplied transcripts imported; verify runner support before promising automatic ASR for another provider.
