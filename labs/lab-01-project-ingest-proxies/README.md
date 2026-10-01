# Lab 01 — Project Setup, Ingest and Proxies

**Course:** Adobe Premiere Pro Masterclass (`C387`)
**Version:** v12 · 21 August 2026

## Scenario

A documentary team has supplied mixed interview and B-roll files. The edit must remain portable and responsive on a training laptop.

## Objective

Set up a recoverable project, inspect source properties, import media into bins and attach proxies.

## Supplied Premiere Pro and MP4 files

- `Lab01-project-ingest-proxies-Starter.prproj`
- `Lab01-Reference-Output.mp4`
- `Lab01-Source.mp4`

## Detailed procedure

1. Open the supplied Lab01 starter project. If Premiere reports missing legacy media, choose Offline All; do not search outside this lab folder.
2. Choose File > Save As and create Lab01-Working.prproj inside the lab folder.
3. Open the supplied Lab01-Source.mp4 in a source monitor and record frame size, frame rate, audio channels and duration in your editing log.
4. Create bins named 01_VIDEO, 02_AUDIO, 03_STILLS, 04_SEQUENCES, 05_EXPORTS and 99_ADMIN.
5. Import Lab01-Source.mp4 into 01_VIDEO and confirm it is linked and online.
6. Create a sequence from the clip, rename it D01_PROXY_TEST_v01 and move it to 04_SEQUENCES.
7. Choose Proxy > Create Proxies and select a low-resolution H.264 or ProRes Proxy preset approved by the trainer.
8. Add the Toggle Proxies button to the Program Monitor and compare playback with proxies enabled and disabled.
9. Save the project, close it, reopen it and confirm that the media remains online.
10. Export an 8–12 second H.264 review file to 05_EXPORTS and reopen it for verification.

## Evidence to retain

Lab01-Working.prproj, media-property log, bin screenshot, proxy-status screenshot and verified MP4.

## Acceptance criteria

- [ ] Project uses the required bins and a named sequence.
- [ ] Source properties and proxy choice are recorded.
- [ ] Media and proxies remain linked after reopening.
- [ ] The review MP4 opens and matches sequence settings.

## Reflection prompts

- Which edit decision most improved story clarity or pacing?
- How do the sequence, track names and edit log prove that the workflow remains traceable?
- Which technical risk should be checked again before delivery?
