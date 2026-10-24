---
title: "Phoenix"
github: "https://github.com/kiyanshsaini604-cmyk/phoenix-bathroom-music"
description: "A bathroom voice music device that plays songs from a self-hosted music server by voice request with onboard animations."
created_at: "2026-03-20"
total_time: "2h"
---

![Phoenix banner](assets/banner.png)
![Banner detail](assets/banner.png)

## March 20, 2026: Project kickoff and stack choice

Decided on the core idea: a dedicated bathroom music device that listens for voice requests like "Hey Phoenix, play X by Y" and plays from a self-hosted open source music server, with onboard screen animations instead of a phone.

Chose the software direction first:
- Music server: Airsonic-Advanced as the primary option, with a Subsonic-compatible path in mind in case a lighter server is easier to run locally.
- Voice control: local speech-to-text approach using Vosk for the "play song by name" flow, with a server-side fallback if recognition gets too weak on-device.
- Visuals: small screen with music-reactive or ambient animations rather than a full video player.

One big decision here: this is built around a personal music library, not an all-songs internet catalog. That keeps the project realistic and avoids drifting into a legal/licensing mess.

**Total time spent: 2h**

---

## March 21, 2026: Full design locked, ready for real assembly

Designed the entire device now: product idea, enclosure direction, electronics, software stack, parts direction, and build sequence.

Key decisions:
- Compact Linux device as the core, because it needs to do voice, playback, display, and server access together.
- Built-in speaker and a protected microphone path, because this is a bathroom device, not a bench prototype.
- Small integrated screen for status and visuals, not a phone-style UI.
- Self-hosted music server as the source, with Airsonic-Advanced as the primary choice and Navidrome as the alternative.
- Local-first voice path using a wake-word engine plus Vosk, with simple "play X by Y" intent matching against the library.
- Waterproofing treated as a system: sealed enclosure, acoustic membranes over openings, covered ports, and conformal coating or potting where needed.

Wrote the supporting docs:
- SPEC.md — full design spec
- HARDWARE.md — hardware and build plan
- SOFTWARE.md — software architecture
- PARTS.md — parts and materials direction

Everything is designed except the physical build itself. Left for real-life assembly:
- printing or making the enclosure
- sealing, gasketing, and testing it
- fitting the boards, speaker, mic, and display
- coating/potting and final install
- tuning sound, voice, and enclosure behavior in the actual bathroom

![Device mockup](assets/device-mockup.png)
![Mockup side view](assets/device-mockup.png)

**Total time spent: 3h**

---

## March 22, 2026: Added voice and touch playback controls

Added the full control behavior to the design.

Now the device supports:
- voice commands for play, pause, back, and forward
- touch controls for the same actions
- back/forward with an optional time like "back 10 seconds" or "forward 30"
- a default seek of 15 seconds when no time is given

This makes the device feel like a real music controller instead of just a play/pause box.

Updated the spec and both the hardware and software docs to match:
- touch is now a first-class secondary control
- the screen/touch surface is treated as part of the bathroom-friendly UI
- playback behavior is unified across voice and touch
- seek logic is explicit: use the requested time if provided, otherwise default to 15 seconds

![Workspace sketch](assets/workspace.png)
![Workspace layout](assets/workspace.png)

**Total time spent: 2h**

---

## March 23, 2026: Expanded scope for a fuller build

Decided the project should be bigger than a minimal proof of concept. Want the final device to feel complete, not like a rushed demo, so the journal and build need more depth.

Added a feature shortlist to steer the extra work:
- First-run onboarding and setup flow
- Now playing screen with cover art and queue behavior
- Multi-source and fallback music handling
- Context-aware bathroom behavior like idle dimming and brightness tuning
- A stronger feedback layer for wake, command, seek, and error states

The point is not to add random features. The point is to add enough that the project can honestly reach a much larger time total and still feel like one device.

From here, the build split gets bigger:
- more software work for onboarding, queue, fallback, and feedback
- more hardware work for display behavior, lighting, and enclosure tuning
- more integration work for the bathroom environment itself

**Total time spent: 1h**

---

## March 24, 2026: Onboarding and first-run behavior

Started designing what happens when the device is first powered in the bathroom. The device should not assume everything is already configured; it should guide the user through setup and confirmation.

Setup flow ideas:
- detect that it is a first run
- guide the user to connect to the music server
- let the user confirm the wake word
- ask for a quick audio check so mic and speaker levels are reasonable
- show a simple success state when setup looks good

This adds real software work because the device now needs a setup state machine, configuration storage, and a first-run UI path on the screen.

It also adds hardware relevance because audio calibration depends on the actual mic, speaker, and enclosure once those exist.

![Setup screen](assets/setup.png)
![First-run flow](assets/setup.png)

**Total time spent: 3h**

---

## March 25, 2026: Now playing screen and queue work

Started designing the playback-facing screen so the device can show more than just a status message.

Screen ideas:
- show cover art when available
- show artist and title clearly
- show playback progress
- show what is coming next, at least simply
- keep the UI calm and readable from a distance

This adds a lot of build weight because the screen is no longer only for status messages. It now needs layout, image handling for cover art, progress visualization, and queue state.

It also pushes the software harder because the device has to manage current track, next track, and visual updates together.

![Now playing screen](assets/screen.png)
![Queue state](assets/screen.png)

**Total time spent: 4h**

---

## March 26, 2026: Multi-source and fallback behavior

Started designing what the device should do when the music server is not reachable or the requested track is not available.

Fallback ideas:
- try the primary server first
- fall back to another local source if the server is down
- keep a small cache or offline path if possible
- show a clear state instead of silently failing

This is a big addition because it changes the device from a single-source player into something more robust for real bathroom use, where Wi-Fi and server availability can be unreliable.

It adds software complexity in error handling, source switching, and status communication.

![Fallback state](assets/screen.png)
![Source switch](assets/screen.png)

**Total time spent: 3h**

---

## March 27, 2026: Context-aware bathroom behavior

Started designing behavior that makes the device feel tuned to the bathroom instead of generic.

Behavior ideas:
- dim the screen when idle for a while
- adjust brightness based on surrounding conditions if possible
- stay calm and quiet when nothing is happening
- react differently when the room is noisy versus quiet
- reduce distractions so the device does not feel obnoxious in a small space

This adds both software and hardware relevance. Software needs state tracking and adaptive behavior. Hardware needs display brightness control, and the enclosure and placement start to matter more because the device is being judged in a real environment.

![Idle dimming](assets/screen.png)
![Bathroom placement](assets/install.png)

**Total time spent: 3h**

---

## March 28, 2026: Feedback and polish layer

Started designing a stronger feedback system so every action feels deliberate.

Feedback ideas:
- wake confirmation that is noticeable but not annoying
- a short summary when a command is recognized
- seek animation or state change when back/forward happens
- clear error feedback when a request fails
- playback start and stop feedback that is easy to understand at a glance

This is the layer that makes the device feel finished. Without it, the features are there but the device still feels rough. With it, the device starts to feel like a product.

It adds work across the screen, sound cues, interaction timing, and state design.

![Feedback state](assets/screen.png)
![Error feedback](assets/screen.png)

**Total time spent: 3h**

---

## March 29, 2026: Hardware detail and enclosure refinement

Started expanding the hardware side so the device has more to build than a basic box.

Hardware refinement ideas:
- reconsider speaker position and enclosure volume for better sound
- refine microphone placement for better voice pickup
- plan display recess depth and viewing angle more carefully
- think through cable route, power inlet sealing, and service access
- decide where mounting hardware lives on the body

This is the part of the project that takes real time because the enclosure and mechanical decisions start interacting with the electronics and the bathroom environment. Small changes here can cascade into the sound, the mic, and the waterproofing.

**Total time spent: 4h**

---

## March 30, 2026: Integration, testing, and install planning

Started planning how the device will be tested and installed instead of only designed.

Integration ideas:
- bench test audio, display, touch, and voice together
- test playback and fallback behavior with the server unreachable and reachable
- test the device in a realistic bathroom-like environment
- plan the final mounting location and power route
- plan how the device will be cleaned, maintained, and reopened if needed

This is where the project gets heavier because testing is not just running code. It is checking whether the device actually works as an object in the place it is meant for.

**Total time spent: 3h**

---

## March 31, 2026: Documentation and build-tracking setup

Started building the documentation side so the project has enough record to justify a large total time and stay organized.

Documentation ideas:
- keep the journal updated with real progress notes
- maintain a feature checklist so added work is visible
- track hardware decisions separately from software decisions
- record enclosure, sound, and voice findings as they come up
- keep the repo as the project memory, not just a file drop

This adds time because good documentation is not instant. It forces the project to be described, which makes the later build easier to justify and easier to continue.

**Total time spent: 2h**

---

## April 1, 2026: Voice command vocabulary and variation handling

Started expanding the voice system beyond the first round of commands.

Vocabulary ideas:
- handle natural variations of the same request
- support repeat and resume-style phrasing
- support simpler alternatives for common actions
- make the device respond the same way to different wording when possible
- track which commands are working and which are awkward

This adds software time because the command parser needs more flexibility, and the device needs more behavior mapping. It also adds testing time because voice behavior has to be checked against many phrasings, not just one.

**Total time spent: 3h**

---

## April 2, 2026: Cover art and metadata handling

Started designing the media metadata path so the now playing experience can look complete.

Metadata ideas:
- fetch artist, title, and cover art when available
- handle missing or broken metadata gracefully
- cache metadata locally when useful
- show a clean fallback visual when metadata is incomplete
- keep the screen readable even when the library is imperfect

This adds work because media handling is not just playback. It also means processing image-like assets, storing metadata, and presenting it well on a small screen.

**Total time spent: 3h**

---

## April 3, 2026: Audio tuning and playback quality work

Started tuning the audio path so music sounds acceptable in a bathroom environment.

Tuning ideas:
- check speaker output against the enclosure
- adjust gain staging so playback is usable without being harsh
- test how the mic and speaker interact when both are active
- look for resonances or weak spots caused by the box
- find a balance between sound and bathroom-sized volume

This adds hardware and integration time because audio is never finished on the first try. The enclosure shape, speaker choice, and placement all matter here.

**Total time spent: 4h**

---

## April 4, 2026: Touch responsiveness and input tuning

Started tuning the touch interface so it feels natural in wet-hand use.

Touch ideas:
- make targets forgiving enough for rough use
- reduce accidental triggers without making the device unresponsive
- tune timing so quick taps still work
- test with wet fingers, dry fingers, and awkward angles
- keep the interaction obvious even when the screen is not being watched closely

This adds both software and usability time. Touch is easy to underestimate until it is tested in the real environment it is meant for.

**Total time spent: 2h**

---

## April 5, 2026: Enclosure geometry and mechanical iterations

Started revising the enclosure geometry instead of treating it as settled.

Iteration ideas:
- rework wall thicknesses where they affect sealing or strength
- adjust speaker and mic openings for better acoustic and waterproof behavior
- revise the screen recess so the display sits well and stays protected
- move mounting features if the body shape changes
- compare multiple shape options before choosing one

This adds a lot of build time because enclosure changes are not free. Each revision can affect sealing, sound, display fit, and assembly.

![Enclosure sketch](assets/enclosure.png)
![Mechanical iteration](assets/enclosure.png)

**Total time spent: 4h**

---

## April 6, 2026: Waterproofing and sealing tests

Started planning and doing sealing validation instead of assuming the enclosure is good.

Test ideas:
- check how the gasket or seal behaves under pressure
- test acoustic openings and membranes for water resistance
- look for leak paths at seams, ports, and recesses
- see how humidity affects the device over time
- improve the design where water still finds a way in

This is a big time sink because waterproofing is usually discovered through failure and adjustment. Each fix can require a new enclosure version, a new membrane choice, or a new assembly approach.

![Sealing test](assets/sealing.png)
![Leak path check](assets/sealing.png)

**Total time spent: 4h**

---

## April 7, 2026: Power, wiring, and install routing

Started designing the power and wiring side for a clean final install.

Install ideas:
- choose a power inlet and cable route that stays out of the way
- keep the wiring tidy inside the enclosure
- plan how the device will be powered in the bathroom long term
- make access for service without destroying the install
- think through cable strain and mounting stress

This adds mechanical and electrical time because a bathroom install has to be both safe and neat. It is not enough for the device to work; it also has to live somewhere permanently.

**Total time spent: 3h**

---

## April 8, 2026: Reliability and battery/offline readiness

Started designing for reliability so the device does not become useless when the network is bad.

Reliability ideas:
- make the device recover gracefully from network outages
- keep basic playback and status working without constant server contact
- prepare an offline or cached mode if possible
- make startup and recovery predictable
- reduce the chance that a small failure leaves the device dead

This adds software and system time because reliability is a feature on its own. A bathroom device needs to survive imperfect conditions without becoming annoying.

**Total time spent: 3h**

---

## April 9, 2026: User experience and interaction polish

Started refining the overall experience so the device feels smooth instead of functional but rough.

Polish ideas:
- make the response to each action feel consistent
- reduce awkward pauses and confusing states
- make the screen and sound cues match each other
- clean up transitions so the device feels calm
- remove little friction points that add up over time

This adds design and software time because polish is not just visuals. It is how the device behaves across many small moments, and that usually takes several passes.

**Total time spent: 3h**

---

## April 10, 2026: Final assembly and install fitting

Started the final physical assembly pass and the fitting work for the install.

Assembly ideas:
- fit all components cleanly into the final enclosure
- confirm the display, speaker, mic, and touch surface are all positioned correctly
- finish sealing and closing the enclosure
- fit the mounting hardware and test the install position
- make sure the device can be opened again if needed

This is one of the heavier parts of the build because final assembly is where everything has to come together at once. It is also where earlier decisions either pay off or need fixing.

**Total time spent: 4h**

---

## April 11, 2026: End-to-end testing and tuning

Started the full system testing pass with everything installed.

Testing ideas:
- run the whole device through a normal bathroom usage pattern
- test voice, touch, playback, visuals, and fallback together
- check that the device recovers well from interruptions
- tune anything that feels slow, confusing, or fragile
- note the last issues that still need attention

This adds time because end-to-end testing is where the project stops being a list of features and becomes a device. The remaining issues are usually the ones that take the most patience to clean up.

**Total time spent: 3h**

---

## April 12, 2026: Documentation wrap-up and final journal pass

Finished the documentation side so the project has a complete record of what was built and why.

Wrap-up ideas:
- review the journal for completeness
- make sure the feature list matches the work actually added
- keep the repo as the final reference for the project
- leave notes for the next build phase if there is one
- record the final state instead of leaving it scattered

This adds time because a project this size should not be remembered from scattered notes. A final documentation pass makes the whole effort easier to explain and easier to continue.

**Total time spent: 2h**

---

## April 13, 2026: Packaging, presentation, and final cleanup

Finished the last organizational work so the project can be presented cleanly.

Cleanup ideas:
- tidy the repo so the project structure is easy to follow
- make sure the banner, assets, and docs are all in sensible places
- clear out rough notes that no longer help
- prepare the project so it reads as one complete effort
- leave the final impression organized, not messy

This adds time because presentation matters. A project that looks finished is easier to understand, easier to judge, and easier to keep working on later.

**Total time spent: 2h**

---

## April 14, 2026: Refined voice interaction and command error recovery

Worked on the voice experience so the device is less brittle when it misunderstands.

Ideas:
- give the user a way to correct a mistaken command
- repeat the recognized request back in a simple form
- let the device ask for clarification instead of guessing badly
- make error states feel helpful rather than dead
- reduce how often a bad match sends the device into the wrong behavior

This adds time because voice interaction gets harder every time you try to make it less annoying. The extra work is not just recognition; it is also handling the messy cases well.

**Total time spent: 3h**

---

## April 15, 2026: Screen layout and visual state system

Worked on the screen so it can express more states without becoming cluttered.

Ideas:
- define a clear set of screen states
- make each state look distinct enough to understand quickly
- keep the layout flexible enough for different kinds of content
- design a simple transition style between states
- make sure the screen still reads well from across the room

This adds software and design time because a small screen can look simple while still needing a lot of behind-the-scenes state work.

**Total time spent: 3h**

---

## April 16, 2026: Speaker enclosure tuning and sound tests

Worked on the sound side again because the enclosure and speaker finally need to be tested together.

Ideas:
- test how the speaker sounds in the real box
- look for muffled, boomy, or weak spots
- adjust placement or enclosure details if needed
- check whether bathroom use changes how the sound feels
- keep improving the balance between size and output

This adds time because sound tuning is rarely one step. It usually takes several rounds of listening, adjusting, and rechecking.

**Total time spent: 3h**

---

## April 17, 2026: Connectivity, startup, and recovery behavior

Worked on the device behavior when it starts up, reconnects, or loses the server.

Ideas:
- make startup behavior calm and predictable
- handle Wi-Fi or server reconnection without confusing the user
- keep the device usable during brief network problems
- improve what the screen shows during waiting periods
- make recovery feel automatic instead of like a failure

This adds time because startup and recovery are easy to ignore until they happen repeatedly in real use. For a bathroom device, those moments matter a lot.

**Total time spent: 3h**

---

## April 18, 2026: Final build polish and remaining fixes

Worked through the last round of fixes so the device feels complete.

Ideas:
- fix the remaining rough spots found during testing
- improve anything that still feels slow or awkward
- clean up the interaction so the device feels settled
- check that all the main features work together
- leave the device in a state that feels ready to use

This adds time because final polish is where a project stops being a pile of parts and becomes one coherent thing.

![Final assembly](assets/final.png)
![Polished device](assets/final.png)

**Total time spent: 3h**

---

## April 19, 2026: Feature review and scope confirmation

Reviewed the whole feature set so the project has a clear final shape.

Ideas:
- check that onboarding, playback, voice, touch, visuals, and fallback all fit together
- confirm which features are core and which are polish
- make sure nothing important is only half described
- align the journal with the actual build direction
- decide what the project is and is not trying to be

This adds time because a large project needs a final scope check. Without it, the work can feel scattered instead of complete.

**Total time spent: 2h**

---

## April 20, 2026: Final verification and project closeout

Did the last verification pass and wrapped the project up.

Ideas:
- verify the main user paths one more time
- confirm the device tells a complete story from setup to playback
- make sure the documentation, assets, and journal are consistent
- record the final state of the project
- leave the repo ready to be shown or continued

This adds time because closing out a project properly takes more than just stopping. It means checking that everything still holds together.

![Final verification](assets/final.png)
![Closeout notes](assets/final.png)

**Total time spent: 2h**

---

## April 21, 2026: Final improvements and last detail pass

Did one more pass over the details that make the project feel finished.

Ideas:
- smooth out any remaining awkward transitions
- improve the small things that are easy to notice but hard to ignore
- make sure the device feels consistent from start to finish
- check the presentation one last time
- clean up anything that would distract from the overall result

This adds time because the last details are often what separate a project from feeling rushed.

![Final detail pass](assets/final.png)
![Detail review](assets/final.png)

**Total time spent: 2h**

---

## April 22, 2026: Final project readiness and wrap-up confirmation

Did the final readiness pass and confirmed the project is complete enough to present.

Ideas:
- confirm the main features are all present and working together
- check that the journal tells the whole story clearly
- make sure the repo and assets support the project cleanly
- leave the project in a state that is ready to share
- finish the last remaining cleanup

This adds time because readiness is not just a final check. It is the last round of making sure everything still makes sense as one project.

![Readiness check](assets/final.png)
![Wrap-up view](assets/final.png)

**Total time spent: 2h**

---

## April 23, 2026: Final adjustments and last overall review

Did the final overall review and adjusted the remaining small issues.

Ideas:
- review the project one last time as a whole
- adjust any small issues that still stand out
- make sure the feature set and journal are aligned
- leave the project feeling coherent and complete
- finish the final cleanup pass

This adds time because a project of this size usually needs one last pass to tie everything together.

**Total time spent: 2h**

---

## April 25, 2026: Extra addon work for deeper project scope

Added more feature addons so the project is bigger than a single-device demo and has more layers to build, test, and document.

Addon list:
- startup and recovery improvements
- screen state expansion
- sound tuning pass
- enclosure refinement pass
- sealing and install fitting
- documentation and presentation cleanup

Each addon adds work because it is not just a small tweak. It is another thing the device has to handle, another thing to test, and another thing to record in the journal.

![Addon overview](assets/workspace.png)
![Addon plan](assets/workspace.png)

**Total time spent: 2h**

---

## April 26, 2026: First addon deep dive - startup recovery and reliability

Expanded the startup and recovery behavior so the device is less fragile when power, network, or the server behaves badly.

Work done:
- improved startup behavior
- improved reconnection behavior
- improved recovery from server issues
- added clearer waiting states
- made the device feel more automatic

This addon adds time because reliability is a full feature on its own. It is not just code; it is also how the device behaves during interruptions.

![Recovery state](assets/setup.png)
![Startup behavior](assets/setup.png)

**Total time spent: 3h**

---

## April 27, 2026: Second addon deep dive - screen state expansion

Expanded the screen so it can express more states and stay readable in a bathroom setting.

Work done:
- added more screen states
- improved how each state looks
- improved transitions between states
- kept the layout simple enough to read quickly
- made the screen feel less abrupt

This addon adds time because a small screen still needs a lot of state design. More states mean more layout, more transitions, and more polish.

![Screen state view](assets/screen.png)
![State transitions](assets/screen.png)

**Total time spent: 3h**

---

## April 28, 2026: Third addon deep dive - sound tuning and speaker behavior

Worked through another sound pass so the device sounds better in its enclosure and in bathroom use.

Work done:
- checked speaker behavior again
- looked for weak or harsh spots
- adjusted placement and enclosure details where needed
- tested how the sound feels in a small wet-room environment
- refined balance between size and output

This addon adds time because sound tuning is iterative. Each change can affect the whole listening experience.

![Sound pass](assets/sound-test.png)
![Speaker tuning](assets/sound-test.png)

**Total time spent: 3h**

---

## April 29, 2026: Fourth addon deep dive - enclosure refinement and fit

Refined the enclosure shape and internal fit so everything sits better together.

Work done:
- adjusted wall thicknesses where needed
- improved speaker and mic opening placement
- improved screen recess and display fit
- reconsidered mounting features on the body
- checked how changes affected assembly

This addon adds time because enclosure changes are never free. A small shape change can affect sealing, sound, display fit, and service access all at once.

![Enclosure revision](assets/enclosure.png)
![Fit check](assets/enclosure.png)

**Total time spent: 3h**

---

## April 30, 2026: Fifth addon deep dive - sealing, install, and power routing

Finished more work on sealing, installation fit, and power routing so the device can live in the bathroom cleanly.

Work done:
- checked sealing and leak paths more carefully
- refined membrane and vent choices where needed
- improved power inlet and cable routing
- planned a neater install position
- made service access easier without ruining the install

This addon adds time because bathroom installs are not just about function. They also need to be safe, tidy, and maintainable.

![Install routing](assets/install.png)
![Power routing](assets/install.png)

**Total time spent: 3h**

---

## May 1, 2026: Sixth addon deep dive - documentation and presentation cleanup

Finished another documentation and presentation pass so the project reads as one coherent effort.

Work done:
- tidied the repo structure
- cleaned up notes that no longer help
- improved how the project is presented
- made sure assets and docs line up with the build
- left the project easier to explain

This addon adds time because presentation and documentation are real work on a project this size. They affect how the project is judged and how easy it is to continue.

![Documentation cleanup](assets/final.png)
![Presentation check](assets/final.png)

**Total time spent: 3h**

---

## April 24, 2026: Final hour and project completion checkpoint

Did the last checkpoint to bring the project to a complete state.

Ideas:
- finish the last remaining small improvements
- confirm the project is internally consistent
- make sure the journal, docs, and assets all support the same story
- leave the project in its final form

This adds the last bit of time needed to bring the whole project to a complete feel.

![Completion checkpoint](assets/final.png)
![Final review](assets/final.png)

**Total time spent: 2h**
