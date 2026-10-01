# Adobe Premiere Pro Masterclass — Learner Guide

**Course code:** C387
**Version:** v12 · 21 August 2026

## Purpose

This guide contains the detailed Premiere Pro procedures, evidence requirements and acceptance criteria intentionally omitted from the visual slides. Each lab includes a valid starter .prproj plus MP4 media. Preserve the supplied source, save a named working project, and retain the verified export and edit evidence.

## Learning outcomes

- LO1: Analyse and arrange footage in a logical sequence for editing.
- LO2: Create editing logs and edit shots.
- LO3: Resolve audio and still-image issues.
- LO4: Collaborate with production teams to edit clips and colour.
- LO5: Perform final touch-up to clean imperfections and deliver the video.

## Core professional workflow

1. Clarify story purpose, audience, delivery channel and technical constraints.
2. Verify source integrity, ownership, licence, consent and permitted use.
3. Record media properties and create the project, bins, tracks and sequence naming convention.
4. Build an editing log, rough cut and fine cut before finishing sound, graphics and colour.
5. Retain sequence versions and change one controlled factor at a time.
6. Review at full speed and frame by frame using story, picture, sound, caption and technical criteria.
7. Export, reopen and verify every deliverable; retain the .prproj, media, captions, manifest and evidence.

## Starter-project compatibility

The starter .prproj files are valid copies of the legacy Built By Life project. On a different computer or Premiere release, the project may upgrade and the original legacy media may appear offline. Choose **Offline All**, immediately use **Save As** inside the current lab folder, then import the supplied LabNN-Source.mp4. Never overwrite the supplied starter project. If Premiere offers to convert the project, retain both the original and converted copy.

## Topic 1 — Get Started on Premiere Pro

Video theory · project setup · import · codecs · proxies · bins · logs · rough-cut planning

**Alignment:** LO1

### Story Purpose and Audience

Editing selects and orders picture and sound so a defined audience can follow an intended message and emotional arc.

**Best used for:** Turning a brief, interview or documentary theme into edit decisions.

**Key controls:** Audience; purpose; duration; channel; call to action; tone; constraints.

**Watch for:** Choosing attractive shots that do not advance the story or meet the brief.

**Quality evidence:** A one-sentence story intention and a shot-selection rationale are recorded.

### Shot Size, Angle and Visual Grammar

Wide, medium and close shots establish context, action and detail; angle and screen direction change meaning.

**Best used for:** Building coverage that orients viewers and supports clean cuts.

**Key controls:** Establishing shot; eyeline; headroom; lead room; 180-degree rule; match on action.

**Watch for:** Jumping screen direction, missing context or cutting between nearly identical framings.

**Quality evidence:** The sequence preserves orientation and uses shot-size contrast intentionally.

### Continuity and Montage

Continuity hides construction across cuts; montage uses juxtaposition to compress time or create a new idea.

**Best used for:** Choosing between invisible narrative flow and expressive association.

**Key controls:** Action match; eyeline match; cutaway; reaction; insert; temporal compression.

**Watch for:** Continuity errors that distract, or montage shots with no conceptual relationship.

**Quality evidence:** A viewer can explain place, time and action without verbal repair.

### Project, Sequence and Media

A project stores edit decisions and metadata, a sequence stores the timeline, and source media remains external.

**Best used for:** Designing a portable, recoverable editing workspace.

**Key controls:** Project location; scratch disks; sequence settings; media paths; cache; autosave.

**Watch for:** Assuming a .prproj contains the media, or saving projects inside disposable cache folders.

**Quality evidence:** Project, media and export locations are documented and recoverable.

### Containers, Codecs and Frame Rates

A container packages streams; codecs encode picture or sound; frame rate defines temporal sampling.

**Best used for:** Diagnosing compatibility, playback and delivery decisions.

**Key controls:** MP4/MOV; H.264/HEVC/ProRes; CFR/VFR; 23.976/25/29.97/50/60 fps.

**Watch for:** Treating MP4 as a codec or mixing frame rates without an explicit interpretation plan.

**Quality evidence:** Media properties and sequence decisions are recorded before editing.

### Import and Ingest

Import registers source files in the project; ingest can copy, transcode or create proxies while preserving source relationships.

**Best used for:** Starting projects from cameras, recorders, stills and shared storage.

**Key controls:** Media Browser; Import mode; copy; transcode; proxy preset; checksum; naming.

**Watch for:** Renaming or moving camera-card structures before a verified copy exists.

**Quality evidence:** All sources appear in named bins and the verified master copy remains untouched.

### Proxy Workflow

Proxies are lighter alternate files attached to high-quality originals and toggled for smoother editing.

**Best used for:** High-resolution, long-GOP or multi-camera media on constrained hardware.

**Key controls:** Create Proxies; preset; frame size; watermark; attach; toggle; full-resolution export.

**Watch for:** Exporting the proxies accidentally or losing source/proxy relink relationships.

**Quality evidence:** Proxy status is visible, playback improves and final export uses approved masters.

### Bins, Metadata and Search

Bins create human-readable hierarchy while metadata and search bins expose technical and editorial attributes.

**Best used for:** Large interview and B-roll libraries.

**Key controls:** Scene; take; camera; good; description; label; search bin; icon/list/freeform view.

**Watch for:** Deep anonymous folders, duplicate names or metadata that exists only in a separate spreadsheet.

**Quality evidence:** A second editor can locate a requested moment quickly.

### Offline Media and Relinking

Premiere retains clip metadata when source files move and can reconnect them by name, path and media properties.

**Best used for:** Portable drives, shared storage and handed-off projects.

**Key controls:** Link Media; Locate; relink others automatically; file extension; media start; timecode.

**Watch for:** Relinking a same-named but different clip or breaking folder structure after approval.

**Quality evidence:** Every clip is online and spot checks match picture, duration and timecode.

### Lab 01 — Project Setup, Ingest and Proxies

**Scenario:** A documentary team has supplied mixed interview and B-roll files. The edit must remain portable and responsive on a training laptop.

**Objective:** Set up a recoverable project, inspect source properties, import media into bins and attach proxies.

#### Detailed procedure

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

#### Evidence

Lab01-Working.prproj, media-property log, bin screenshot, proxy-status screenshot and verified MP4.

#### Acceptance criteria

- Project uses the required bins and a named sequence.
- Source properties and proxy choice are recorded.
- Media and proxies remain linked after reopening.
- The review MP4 opens and matches sequence settings.

Self-contained lab folder: `labs/lab-01-project-ingest-proxies/`

### Lab 02 — Editing Logs, Markers and Rough-Cut Plan

**Scenario:** A producer needs a traceable shortlist of interview ideas and supporting B-roll before the first assembly.

**Objective:** Create an editing log, mark selects and assemble a clear story spine.

#### Detailed procedure

1. Open the Lab02 starter, save as Lab02-Working.prproj and import Lab02-Source.mp4.
2. Create an editing log with columns for source, In, Out, duration, shot size, content, quality, use and notes.
3. Review the clip with J, K and L and mark at least six candidate moments with source In and Out points.
4. Add colour-coded markers for story, picture issue, audio issue and possible B-roll coverage.
5. Create a SELECTS sequence and add each logged range using Insert edits.
6. Create a ROUGH_v01 sequence with a beginning, development and closing beat.
7. Place an establishing shot before detailed action and use one reaction/cutaway to protect continuity.
8. Review the sequence without stopping and revise any shot that does not advance the story.
9. Update the editing log with the selected sequence timecodes.
10. Export a selects reel and save the project.

#### Evidence

Lab02-Working.prproj, completed log, marker screenshot and selects-reel MP4.

#### Acceptance criteria

- At least six logged ranges include source timecodes and intended use.
- Markers use a consistent legend.
- The rough cut has a recognisable beginning, middle and end.
- No unexplained offline media remains.

Self-contained lab folder: `labs/lab-02-logs-markers-rough-cut/`

## Topic 2 — Shot Editing

Source and Program monitors · three-point editing · track control · trim types · pacing · transitions

**Alignment:** LO2

### Source, Program and Timeline Roles

The Source Monitor prepares individual clips; the Program Monitor shows sequence output; the Timeline holds edit relationships.

**Best used for:** Separating source decisions from sequence review.

**Key controls:** Playhead; In/Out; track headers; time ruler; safe margins; playback resolution.

**Watch for:** Marking the sequence when intending to mark the source, or judging quality at low playback resolution.

**Quality evidence:** The correct monitor and timecode are named in the editing log.

### In, Out and Three-Point Editing

Any three of source In, source Out, sequence In and sequence Out define an edit; Premiere calculates the fourth.

**Best used for:** Precise duration-controlled assembly.

**Key controls:** I/O; clear In/Out; insert; overwrite; source duration; sequence target.

**Watch for:** Leaving stale marks or forcing a duration that changes the wrong source boundary.

**Quality evidence:** The inserted segment starts, ends and lands at the logged timecodes.

### Insert vs Overwrite

Insert opens time and ripples later clips; overwrite replaces occupied duration without changing later timing.

**Best used for:** Choosing whether new material should move or replace downstream content.

**Key controls:** Comma/period shortcuts; source patching; track targeting; sync locks.

**Watch for:** Using insert in a locked-duration programme or overwriting wanted content.

**Quality evidence:** Before/after duration and displaced tracks match the editing intention.

### Source Patching and Track Targeting

Source patches route incoming channels; track targets determine many timeline commands and navigation operations.

**Best used for:** Controlling where video and audio land in multi-track sequences.

**Key controls:** V1/A1 patches; target highlights; sync locks; linked selection.

**Watch for:** Sending audio to the wrong track or misunderstanding target versus patch state.

**Quality evidence:** Imported channels land on named tracks without disturbing protected content.

### Selection, Razor and Add Edit

Selection moves and trims clips; Razor or Add Edit creates edit points; keyboard methods reduce tool switching.

**Best used for:** Building and restructuring rough cuts.

**Key controls:** Selection; Razor; Cmd/Ctrl+K; linked selection; snapping; track selection.

**Watch for:** Cutting every enabled track or separating linked audio unintentionally.

**Quality evidence:** Edit points are deliberate and no orphaned frames or audio pieces remain.

### Ripple and Rolling Trims

Ripple changes one side and sequence duration; Rolling moves the cut while preserving combined duration.

**Best used for:** Tightening pauses or shifting emphasis between adjacent shots.

**Key controls:** Ripple tool; Rolling tool; Q/W trims; trim mode; sync locks.

**Watch for:** Breaking sync or rippling a locked timing milestone.

**Quality evidence:** The intended timing changes and downstream sync remains verified.

### Slip and Slide Edits

Slip changes a clip's source In/Out while holding timeline position; Slide moves the clip while adjusting its neighbours.

**Best used for:** Refining content without rebuilding sequence timing.

**Key controls:** Slip tool; Slide tool; four-up display; handles; neighbouring coverage.

**Watch for:** Insufficient handles or changing the wrong narrative beat.

**Quality evidence:** Sequence duration is unchanged and the chosen action frames improve continuity.

### Pacing and Shot Duration

Shot duration, movement, audio rhythm and information density shape perceived energy and comprehension.

**Best used for:** Matching fast action, reflective interviews and instructional content.

**Key controls:** Average shot length; pause; reaction; beat; J-cut/L-cut; music phrase.

**Watch for:** Uniform shot duration or speed used without story justification.

**Quality evidence:** A pacing log links key cuts to story beats and audience response.

### Transitions and Handles

A transition overlaps outgoing and incoming media, requiring unused source frames called handles.

**Best used for:** Signalling time, place, memory or a deliberate stylistic change.

**Key controls:** Cut; dissolve; dip; wipe; duration; alignment; handles; default transition.

**Watch for:** Using transitions to hide weak shot choice, or repeated decorative effects.

**Quality evidence:** Most edits work as cuts; selected transitions have a documented narrative purpose.

### J-Cuts, L-Cuts and Continuity Bridges

A J-cut lets incoming audio lead picture; an L-cut lets outgoing audio continue under the next shot.

**Best used for:** Smoother dialogue, interview B-roll and scene connections.

**Key controls:** Linked selection; rolling audio; constant power; room tone; cutaway.

**Watch for:** Audible discontinuities, exposed gaps or dialogue cut mid-phoneme.

**Quality evidence:** Audio bridges hide picture edits while speech remains natural.

### Lab 03 — Three-Point Editing, Trims and Pacing

**Scenario:** An interview section feels slow and repetitive. The director wants a concise version that keeps the speaker's meaning.

**Objective:** Use three-point edits and multiple trim types to produce a deliberate 25–35 second sequence.

#### Detailed procedure

1. Open the Lab03 starter, save as Lab03-Working.prproj and import Lab03-Source.mp4.
2. Create ROUGH_v01 and mark source In/Out points for the interview and B-roll ranges.
3. Use Insert and Overwrite edits intentionally; record which command you used and why.
4. Create at least one Add Edit cut using the keyboard shortcut rather than the Razor tool.
5. Use a ripple trim to remove a weak pause and confirm downstream sync.
6. Use a rolling trim to shift emphasis between two adjacent shots without changing duration.
7. Use a slip edit to improve action timing while preserving the clip's timeline position.
8. Create one J-cut or L-cut so audio bridges a picture edit.
9. Duplicate the sequence as FINE_v02 and improve shot-duration variation.
10. Export the paced sequence and compare it with the supplied reference output.

#### Evidence

Lab03-Working.prproj, trim-decision log and paced MP4.

#### Acceptance criteria

- Sequence duration is 25–35 seconds.
- Ripple, rolling and slip edits are visible in sequence history or evidence.
- Dialogue meaning remains intact.
- The audio bridge sounds continuous.

Self-contained lab folder: `labs/lab-03-trim-pacing/`

### Lab 04 — Continuity, Cutaways and Transitions

**Scenario:** A farm-work montage needs clear geography and one motivated passage of time without decorative transition overload.

**Objective:** Build a continuity sequence and use a transition only where it communicates story meaning.

#### Detailed procedure

1. Open the Lab04 starter, save as Lab04-Working.prproj and import Lab04-Source.mp4.
2. Create a sequence and identify the establishing, action, detail and reaction roles of each shot.
3. Arrange shots to preserve screen direction and match action through at least one cut.
4. Insert a cutaway to conceal a time compression or continuity repair.
5. Inspect source handles on both sides of the edit point.
6. Apply one Cross Dissolve or Dip to Black only at the deliberate time/location change.
7. Adjust transition alignment and duration; explain the selected value in the log.
8. Replace any unnecessary transition with a straight cut.
9. Review at full sequence speed and inspect the edit point frame by frame.
10. Export and retain before/after comparison notes.

#### Evidence

Lab04-Working.prproj, continuity map, transition rationale and montage MP4.

#### Acceptance criteria

- Screen direction and action remain understandable.
- The sequence uses at most one decorative transition.
- Transition handles do not freeze or repeat unwanted frames.
- The cutaway has a clear continuity purpose.

Self-contained lab folder: `labs/lab-04-continuity-transitions/`

## Topic 3 — Audio and Graphics Editing

Gain and volume · keyframes · repair · music · sync · stills · graphics · effects · masks

**Alignment:** LO3

### Gain, Volume and Signal Flow

Gain changes clip input level; volume and track controls change level later in the sequence signal path.

**Best used for:** Normalising inconsistent recordings before mixing.

**Key controls:** Audio Gain; peak amplitude; normalize; clip volume; track fader; meters.

**Watch for:** Boosting noisy audio excessively or confusing gain with track automation.

**Quality evidence:** Dialogue is consistent, unclipped and leaves suitable headroom.

### Meters, Headroom and Clipping

Digital meters show sample peaks; 0 dBFS is the ceiling and clipping cannot be repaired by lowering volume later.

**Best used for:** Preventing distortion and balancing dialogue, music and effects.

**Key controls:** Peak meter; dBFS; true-peak awareness; channel layout; mute/solo.

**Watch for:** Mixing by ear alone or allowing red clip indicators to persist.

**Quality evidence:** Full-programme playback shows stable, unclipped levels.

### Clip Keyframes and Automation

Keyframes store parameter values over time and interpolate volume, pan, opacity, motion and effects.

**Best used for:** Fades, ducking, emphasis and animated properties.

**Key controls:** Add/remove keyframe; Bezier/linear; temporal interpolation; rubber band; automation mode.

**Watch for:** Too few keyframes causing abrupt change or too many creating noisy automation.

**Quality evidence:** The envelope is smooth and parameter changes occur at intended story beats.

### Dialogue Repair and Essential Sound

Dialogue tools classify clips and provide repair, clarity and loudness controls around common speech problems.

**Best used for:** Noise, hum, rumble, sibilance and inconsistent interview recordings.

**Key controls:** Dialogue tag; Reduce Noise; Reduce Rumble; DeHum; DeEss; Enhance Speech; loudness.

**Watch for:** Over-processing that creates metallic or phasey speech.

**Quality evidence:** A/B review improves intelligibility without audible artefacts.

### Music Editing, Remix and Fades

Music edits can follow phrase boundaries; Remix changes duration algorithmically; fades and ducking protect dialogue.

**Best used for:** Fitting music to locked duration and shaping scene energy.

**Key controls:** Waveform; beat; remix duration; crossfade; keyframes; Essential Sound ducking.

**Watch for:** Cutting across a musical phrase or masking speech with midrange energy.

**Quality evidence:** The music ends musically and dialogue remains clear.

### Synchronising Audio and Video

Premiere can synchronise by timecode, markers or matching waveforms; manual slips handle residual offsets.

**Best used for:** Dual-system sound and multi-camera interviews.

**Key controls:** Synchronize; merge clips; timecode; waveform; slate; linked selection.

**Watch for:** Syncing noisy reference audio blindly or deleting production audio before verification.

**Quality evidence:** Lip sync and transient checks match at multiple points.

### Still Images and Motion

Still images occupy time like clips; Motion properties and keyframes create reframing and pan/zoom movement.

**Best used for:** Photographs, documents, maps and title cards.

**Key controls:** Default still duration; Set/Scale to Frame Size; Position; Scale; anchor; keyframes.

**Watch for:** Scaling beyond available pixels or creating distracting constant motion.

**Quality evidence:** Image detail holds at delivery size and motion supports the narration.

### Graphics and Lower Thirds

Text and vector shapes remain editable graphics clips whose properties can be styled and animated.

**Best used for:** Names, roles, locations, chapter labels and calls to action.

**Key controls:** Type tool; Properties; alignment; safe margins; responsive design; styles.

**Watch for:** Low contrast, tiny type, inconsistent margins or covering important picture content.

**Quality evidence:** The lower third reads at playback speed and survives safe-area review.

### Effects and Adjustment Layers

Clip effects affect one item; adjustment layers apply effects to the composite beneath and preserve shared control.

**Best used for:** Consistent looks, effects stacks and reusable treatments.

**Key controls:** Effects panel; Effect Controls; order; enable/disable; adjustment layer; render bar.

**Watch for:** Duplicating inconsistent settings or stacking effects without isolating the cause.

**Quality evidence:** Effect order is documented and an A/B toggle proves the intended contribution.

### Masks, Tracking and Stabilisation

Effect masks limit treatment; tracking follows motion; Warp Stabilizer analyses camera motion and reframes edges.

**Best used for:** Privacy blur, selective correction and unwanted camera shake.

**Key controls:** Ellipse/pen mask; feather; expansion; track; stabilisation method; smoothness; crop.

**Watch for:** Tracking poor contrast, masking the wrong object or accepting heavy warping.

**Quality evidence:** The mask follows the subject and stabilisation does not distort important geometry.

### Lab 05 — Dialogue Repair, Music and Keyframes

**Scenario:** The interview is uneven and contains background noise; music must support the scene without masking speech.

**Objective:** Repair dialogue, balance music and create smooth level automation.

#### Detailed procedure

1. Open the Lab05 starter, save as Lab05-Working.prproj and import Lab05-Source.mp4.
2. Inspect the waveform and meters; record the starting peak range and any clipping indicators.
3. Set clip gain so dialogue starts from a consistent level without clipping.
4. Tag the clip as Dialogue in Essential Sound and apply only the repair controls needed.
5. A/B Reduce Noise or Enhance Speech and reduce the setting if artefacts become audible.
6. Add the supplied music or choose a trainer-approved segment; trim on a musical phrase.
7. Use Constant Power fades at music edit points.
8. Add clip-volume keyframes to duck music under speech and restore it between phrases.
9. Play the full sequence and verify that every word remains intelligible.
10. Export the mixed sequence and record final peak observations.

#### Evidence

Lab05-Working.prproj, before/after level notes, keyframe screenshot and mixed MP4.

#### Acceptance criteria

- No clip indicator remains lit after full playback.
- Dialogue is intelligible and not metallic or over-processed.
- Music fades and ducking are smooth.
- The exported mix matches the timeline review.

Self-contained lab folder: `labs/lab-05-audio-repair-mix/`

### Lab 06 — Stills, Graphics and Adjustment Effects

**Scenario:** A short documentary section needs a still photograph, a lower third and a restrained shared treatment.

**Objective:** Animate a still, build a readable lower third and apply a shared effect non-destructively.

#### Detailed procedure

1. Open the Lab06 starter, save as Lab06-Working.prproj and import Lab06-Source.mp4 plus one supplied image.
2. Create a 25 fps or trainer-approved sequence and place the still for 5–7 seconds.
3. Use Set to Frame Size or a justified alternative; confirm the still has sufficient pixels for the final scale.
4. Add Position and Scale keyframes to create slow purposeful motion with an ease at each end.
5. Create an editable lower third with the subject name and role.
6. Align the graphic inside title-safe margins and verify contrast against the picture.
7. Create a simple entry/exit animation using opacity and position keyframes.
8. Place an adjustment layer above the montage and apply one shared effect.
9. Toggle the adjustment layer to prove its contribution and revise if it distracts.
10. Export the sequence and review text at normal playback speed.

#### Evidence

Lab06-Working.prproj, keyframe screenshot, safe-margin screenshot and graphics MP4.

#### Acceptance criteria

- Still-image motion is smooth and retains detail.
- Lower-third text is editable, accurate and readable.
- Graphics remain inside safe margins.
- The shared effect is isolated on an adjustment layer.

Self-contained lab folder: `labs/lab-06-stills-graphics-effects/`

### Lab 07 — Masks, Tracking and Visual Clean-up

**Scenario:** An outdoor clip contains camera shake and a distracting region that must be reduced without damaging the subject.

**Objective:** Stabilise the clip and track a feathered effect mask to clean a local imperfection.

#### Detailed procedure

1. Open the Lab07 starter, save as Lab07-Working.prproj and import Lab07-Source.mp4.
2. Duplicate the source clip or sequence so the untreated baseline remains available.
3. Apply Warp Stabilizer and let analysis complete before changing settings.
4. Start with a conservative Smooth Motion value and check edges and subject geometry.
5. Create an effect mask around the distracting area and set appropriate feather and expansion.
6. Track the mask forward; stop and correct it whenever it leaves the target.
7. Apply a restrained blur, denoise or correction inside the mask.
8. Review at 100% and full speed for warping, halos and mask slips.
9. Compare baseline and treated versions with the effect bypassed.
10. Export the approved version and record the rejected settings.

#### Evidence

Lab07-Working.prproj, stabilisation/mask settings, A/B notes and cleaned MP4.

#### Acceptance criteria

- Stabilisation does not introduce visible geometry distortion.
- The mask follows the target for the full clip.
- Feathering avoids a hard treatment edge.
- The baseline remains available for comparison.

Self-contained lab folder: `labs/lab-07-masks-stabilise-clean/`

## Topic 4 — Clip and Colour Editing

Speed · time remapping · colour correction · scopes · matching · review and collaboration

**Alignment:** LO4

### Speed and Duration

Speed percentage and duration are inversely related; frame blending or optical methods create intermediate frames.

**Best used for:** Slow motion, time compression and fitting action to timing.

**Key controls:** Speed/Duration; reverse; ripple trailing clips; frame sampling; frame blending; optical flow.

**Watch for:** Using optical flow on occlusions or violating production frame-rate requirements.

**Quality evidence:** Motion is visually acceptable and final duration matches the brief.

### Rate Stretch and Time Remapping

Rate Stretch fits a clip to timeline duration; Time Remapping changes speed over time with keyframes and ramps.

**Best used for:** Variable-speed emphasis and precise gap filling.

**Key controls:** Rate Stretch tool; speed keyframes; ramp handles; time interpolation.

**Watch for:** Unmotivated ramps, audio pitch artefacts or action changing too abruptly.

**Quality evidence:** The ramp enters and exits smoothly at meaningful action points.

### Correction vs Grading

Correction neutralises technical differences; grading applies an intentional creative look after correction.

**Best used for:** Matching cameras before establishing visual style.

**Key controls:** White balance; exposure; contrast; saturation; look; bypass; order.

**Watch for:** Using a LUT as repair or grading inconsistent sources before matching.

**Quality evidence:** Shots match first, then the approved grade remains consistent.

### Video Scopes

Waveform displays signal level by horizontal position; parade separates RGB channels; vectorscope shows hue and saturation.

**Best used for:** Objective exposure, balance, skin-tone and legal-range review.

**Key controls:** Luma waveform; RGB parade; vectorscope; scale; clipping; reference frame.

**Watch for:** Trusting an uncalibrated display alone or reading scopes without scene context.

**Quality evidence:** Scope captures and visual review support each correction decision.

### White Balance and Exposure

Temperature/tint and tonal controls neutralise casts and place key picture regions in usable ranges.

**Best used for:** Mixed interviews, outdoor shifts and camera mismatch.

**Key controls:** Eyedropper; temperature; tint; exposure; highlights; shadows; whites; blacks.

**Watch for:** Forcing neutral balance in intentionally warm/cool scenes or clipping highlights.

**Quality evidence:** Neutral references and important skin/detail areas remain plausible.

### Curves and Colour Wheels

Curves reshape tonal relationships; wheels move shadows, midtones and highlights toward chosen colour vectors.

**Best used for:** Targeted contrast, cast repair and controlled creative shaping.

**Key controls:** RGB curves; hue/saturation curves; shadow/midtone/highlight wheels; luma vs chroma.

**Watch for:** Crossing channels aggressively or creating banding and unnatural skin.

**Quality evidence:** Before/after scopes show controlled change without new clipping.

### Shot Matching and Comparison View

Comparison View places a reference beside the current shot so visual and automatic matching can be evaluated.

**Best used for:** Interviews, multi-camera scenes and sequences under one lighting condition.

**Key controls:** Reference frame; current frame; face detection; colour wheels; shot match; wipe.

**Watch for:** Matching to an unrepresentative frame or accepting automatic results without review.

**Quality evidence:** Adjacent shots cut without distracting shifts in exposure or colour.

### Collaborative Review and Change Control

Timecoded comments, sequence versions and change logs make creative decisions traceable across production roles.

**Best used for:** Director, producer, editor and client review cycles.

**Key controls:** Version name; locked review export; timecode burn-in; comment status; change log.

**Watch for:** Overwriting approved versions or implementing ambiguous feedback without confirmation.

**Quality evidence:** Every accepted change links to a comment, version and verifier.

### Lab 08 — Speed, Duration and Time Remapping

**Scenario:** A farm-action montage must compress time while preserving one moment of emphasis and meeting a fixed duration.

**Objective:** Create constant and variable speed treatments and verify motion quality.

#### Detailed procedure

1. Open the Lab08 starter, save as Lab08-Working.prproj and import Lab08-Source.mp4.
2. Duplicate the sequence into ConstantSpeed and TimeRemap versions.
3. Use Speed/Duration on the first version and record speed percentage, new duration and interpolation method.
4. Use Rate Stretch on a duplicate to fit a trainer-specified gap and compare the result.
5. On the TimeRemap version, show Clip Keyframes > Time Remapping > Speed.
6. Add speed keyframes around the emphasis moment and separate the keyframe halves to form ramps.
7. Test Frame Sampling, Frame Blending and Optical Flow where appropriate.
8. Inspect hands, tools and crossing edges for interpolation artefacts.
9. Choose the best treatment, document why and keep the alternatives named.
10. Export the approved 15–20 second speed study.

#### Evidence

Lab08-Working.prproj, three treatment variants, interpolation comparison and MP4.

#### Acceptance criteria

- The approved output meets the duration target.
- Speed ramps enter and exit smoothly.
- Interpolation is justified and free of unacceptable warping.
- Alternative versions remain clearly named.

Self-contained lab folder: `labs/lab-08-speed-time-remap/`

### Lab 09 — Colour Correction, Shot Matching and Review

**Scenario:** Two shots recorded under different conditions must cut together naturally before a subtle approved grade is applied.

**Objective:** Correct exposure and white balance with scopes, match shots and record review changes.

#### Detailed procedure

1. Open the Lab09 starter, save as Lab09-Working.prproj and import Lab09-Source.mp4.
2. Display Lumetri Scopes and capture baseline waveform, RGB parade and vectorscope evidence.
3. Choose a reference shot representative of the scene and correct its white balance and exposure.
4. Use Comparison View to match the second shot; treat automatic match as a starting point only.
5. Refine the match with Basic Correction, Curves or Colour Wheels while protecting highlights and skin/detail.
6. Create an adjustment layer for the shared creative grade after the technical match.
7. Export REVIEW_v01 with timecode overlay or clear filename.
8. Record one timecoded peer/trainer comment and its disposition.
9. Duplicate as REVIEW_v02, implement the accepted change and update the change log.
10. Export the approved match and capture final scopes.

#### Evidence

Lab09-Working.prproj, before/after scopes, review v01/v02, comment log and final MP4.

#### Acceptance criteria

- Adjacent shots do not show a distracting exposure or colour shift.
- Scopes support the correction rationale.
- The creative grade is separate from technical correction.
- One review comment is traceably implemented or rejected.

Self-contained lab folder: `labs/lab-09-colour-match-review/`

## Topic 5 — Final Touch-up and Delivery

Titles · captions · reframing · quality control · export · archive · production hand-off

**Alignment:** LO5

### Text Hierarchy and Safe Placement

Title size, weight, spacing and placement establish reading order while safe margins protect delivery visibility.

**Best used for:** Openers, lower thirds, end cards and instructional labels.

**Key controls:** Font; size; leading; tracking; alignment; safe margins; duration; contrast.

**Watch for:** Too much text, weak hierarchy or appearing for too little reading time.

**Quality evidence:** Text passes contrast, spelling, safe-area and playback-duration checks.

### Captions and Accessibility

Caption tracks align text to speech and can be styled, burned in, embedded or exported as sidecar files.

**Best used for:** Accessible dialogue, multilingual delivery and silent autoplay.

**Key controls:** Transcribe; speaker names; caption creation; track style; line length; timing; SRT.

**Watch for:** Uncorrected transcription, poor line breaks or captions covering essential visuals.

**Quality evidence:** Captions match speech, identify speakers where needed and pass a full read-through.

### Aspect Ratios and Auto Reframe

Reframing adapts composition to another canvas; Auto Reframe analyses motion and creates position keyframes.

**Best used for:** 16:9, 1:1, 4:5 and 9:16 derivatives.

**Key controls:** Sequence size; nest; Auto Reframe; motion tracking; safe zones; graphic repositioning.

**Watch for:** Blindly accepting automated framing or cropping gestures and text.

**Quality evidence:** Each derivative preserves the focal subject and readable graphics.

### Technical Quality Control

QC combines uninterrupted playback with targeted inspection of picture, sound, captions and specifications.

**Best used for:** Final approval before client or platform delivery.

**Key controls:** Resolution; frame rate; aspect; field order; audio channels; peaks; captions; black frames.

**Watch for:** Checking only favourite scenes or verifying the timeline but not the exported file.

**Quality evidence:** A signed checklist records full-duration playback and spot checks.

### Export Format, Codec and Bitrate

Export mode encodes the sequence into a delivery container and codec using frame, audio and bitrate settings.

**Best used for:** Web MP4, review files, mezzanine masters and archive derivatives.

**Key controls:** H.264; QuickTime; preset; frame size/rate; VBR; target/max bitrate; hardware/software encoding.

**Watch for:** Choosing the smallest file without quality review or changing frame rate unintentionally.

**Quality evidence:** The export reopens, reports expected properties and meets the destination brief.

### Audio and Caption Export

Delivery includes explicit audio channel, sample-rate, loudness and caption-mode decisions.

**Best used for:** Accessible web delivery, broadcast hand-off and social publishing.

**Key controls:** Stereo/mono; 48 kHz; bitrate; normalization; embed/burn-in/sidecar; SRT frame rate.

**Watch for:** Missing caption files, wrong channels or clipped programme peaks.

**Quality evidence:** A package inventory confirms picture, audio and caption deliverables.

### Project Archiving and Consolidation

Project Manager can collect, transcode or trim used media so the edit can be restored later.

**Best used for:** Handover, long-term retention and freeing active storage.

**Key controls:** Exclude unused clips; handles; collect/copy; transcode; destination; verification.

**Watch for:** Archiving only the .prproj or deleting sources before the archive opens successfully.

**Quality evidence:** The archive opens on another path with all required media online.

### Final Hand-off and Versioning

A delivery package separates editable master, review export, approved final, captions, rights records and change notes.

**Best used for:** Production team hand-off and auditable client delivery.

**Key controls:** Version convention; checksum; manifest; approval status; archive location; retention.

**Watch for:** Using 'final-final' names or sending unapproved sources and personal data.

**Quality evidence:** The manifest, checksum and approval record identify the exact delivered version.

### Lab 10 — Captions, Reframe, QC and Final Export

**Scenario:** The completed documentary excerpt needs accessible captions, 16:9 and 9:16 versions, technical QC and an archive-ready hand-off.

**Objective:** Finish titles/captions, create a vertical derivative, export verified deliverables and archive the project.

#### Detailed procedure

1. Open the Lab10 starter, save as Lab10-Capstone-v01.prproj and import Lab10-Source.mp4.
2. Create or verify the opening title, lower third and end card; check spelling, duration and safe placement.
3. Transcribe dialogue, create captions and correct every word, speaker name and punctuation mark.
4. Apply a readable caption style and resolve any collision with graphics or important picture content.
5. Duplicate the approved 16:9 sequence and use Auto Reframe to create a 9:16 derivative.
6. Review every automated keyframe and manually correct poor framing and graphic placement.
7. Run full-duration QC for picture, audio, captions, black frames, aspect and version labels.
8. Export the 16:9 master/review file and the 9:16 derivative using trainer-approved H.264 settings.
9. Export captions as SRT and reopen both MP4 files to verify properties and content.
10. Use Project Manager or a trainer-approved collect workflow to create an archive copy, then open the archived project and confirm all required media is online.

#### Evidence

Lab10-Capstone-v01.prproj, QC checklist, 16:9 MP4, 9:16 MP4, SRT, manifest and verified archive.

#### Acceptance criteria

- Captions match speech and remain readable.
- Both aspect-ratio versions preserve the subject and graphics.
- Exports reopen with expected frame/audio properties.
- The archive opens with required media online and a delivery manifest.

Self-contained lab folder: `labs/lab-10-captions-reframe-export/`

## Media rights and responsible AI

Use only footage, music, stills, graphics and voices that you created or are permitted to use. Record the source, owner, licence or consent, date, allowed modifications, commercial/redistribution scope and attribution requirement. Public visibility does not grant reuse permission. Review AI-assisted transcripts, reframes, matches and generated results; retain provenance and human approval evidence where appropriate. This guide is educational information, not legal advice.

## Source register

- **Official course page:** https://www.tertiarycourses.com.sg/adobe-premiere-pro-masterclass.html
- **Adobe Premiere Help:** https://helpx.adobe.com/premiere/desktop.html
- **Adobe editing workflow:** https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/edit-video-in-premiere.html
- **Adobe Text-Based Editing:** https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/overview-of-text-based-editing.html
- **Adobe export settings:** https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/overview-of-export-settings.html
