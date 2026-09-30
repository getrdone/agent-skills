# Local Whisper sidecar

Existing runner: `G:/__ai-projects/_agent-tools/whisper-local/whisper_local.py`.
Read its README for current status and configuration. It uses an isolated environment and existing GPU/model configuration. Do not install another service.

For an authorized full-transcript request:

1. Record the URL with the video library before starting transcription. Resolve the canonical URL from the existing video record; do not add another request just to retry.
2. Download audio only with yt-dlp, quietly and with serial downloads initially. Do not activate or play browser video tabs. Verify the downloaded audio's duration and integrity before transcription.
3. Use the configured local Whisper model. Begin with one transcription at a time; only increase to two or three after measuring throughput, GPU memory, and desktop responsiveness. Record stage, attempt, error, and QA data in SQLite `processing_batches`, `processing_items`, and `processing_events`. A job folder may hold temporary audio and timed source evidence, but must not be the authoritative progress log.
4. Check transcript coverage, timing, language, and uncertain passages. Flag sparse or low-confidence output as `needs_review`; automated checks do not certify word-perfect transcription. Import the complete timed SRT through `library.py import-transcript VIDEO_KEY PATH`, or the reviewed full Markdown. Preserve timing evidence and chapter markers. Verify SQLite text and Markdown/HTML exports, then delete temporary audio.
5. Run the current clean-video-transcript skill when editorial cleanup is requested. Preserve full speech and references; import the final transcript without adding a new user-request event.

The dashboard's existing Fetch action still attempts captions and has an in-memory queue. It has not yet been replaced by the durable audio-first worker. Report that limitation honestly; do not promise unattended processing from that control.

The existing runner currently focuses on YouTube input. Other video URLs can still be catalogued and their supplied transcripts imported; verify runner support before promising automatic ASR for another provider.


Default unattended execution: use the project `_tools/run-parallel-batch.py` instead of the historical serial runner. Launch with pythonw and no-window child flags. The worker records benchmark/QA/progress in SQLite and uses a bounded serial download queue. Dashboard Fetch dispatches this workflow automatically. See the current SKILL.md for resource limits and verification gates.
