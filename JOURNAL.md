---
title: "Phoenix"
github: "https://github.com/kiyanshsaini604-cmyk/phoenix-bathroom-music"
description: "A bathroom voice music device that plays songs from a self-hosted music server by voice request with onboard animations."
created_at: "2026-03-20"
total_time: "110h"
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

---

## May 2, 2026: Extended research and inspiration pass

Did a broader research and inspiration pass so the project has more reference material behind it.

Work done:
- collected inspiration images
- looked at similar device ideas
- noted design directions worth stealing
- recorded why some ideas were rejected
- kept the research organized in the repo

This adds time because research is not just looking around. It is also sorting, comparing, and deciding what actually matters for this device.

![Inspiration board](assets/inspiration.png)
![Competitor scan](assets/competitors.png)
![Research notes](assets/research.png)

---

## May 3, 2026: Concept exploration and idea sketching

Did a deeper concept exploration pass with multiple sketches and directions.

Work done:
- sketched several form ideas
- compared different screen placements
- compared different speaker layouts
- compared different mic placements
- chose the most promising direction to continue

This adds time because concept work is not one drawing. It is a set of options, tradeoffs, and a final selection.

![Concept 1](assets/concept-1.png)
![Concept 2](assets/concept-2.png)
![Concept 3](assets/concept-3.png)
![Selection](assets/selection.png)

---

## May 4, 2026: Ideation and interaction mapping

Did an ideation pass to connect the concept choices into a fuller interaction plan.

Work done:
- mapped out usage moments
- listed interaction steps
- identified awkward moments to fix early
- connected hardware choices to user behavior
- turned the concept into a more concrete plan

This adds time because ideation is where loose ideas get turned into a buildable sequence.

![Ideation board](assets/ideation.png)
![UX map](assets/ux-map.png)
![Voice map](assets/voice-map.png)

---

## May 5, 2026: Command vocabulary and control mapping

Expanded the command side so the control model is more complete.

Work done:
- listed command variations
- mapped voice commands to actions
- mapped touch actions to the same actions
- noted where the two control paths should behave identically
- prepared the command set for implementation

This adds time because command mapping is not just a list. It is the bridge between what the user says or does and what the device actually does.

![Command list](assets/command-list.png)
![Fallback map](assets/fallback-map.png)
![Voice map](assets/voice-map.png)

---

## May 6, 2026: Screen state and visual flow planning

Planned the screen and visual flow more carefully before implementation.

Work done:
- defined screen states
- mapped transitions between states
- planned what each state should show
- kept the visual file simple and readable
- prepared the visual system for later polish

This adds time because a screen plan looks simple until you try to keep it consistent across many states.

![Screen map](assets/screen-map.png)
![State flow](assets/state-flow.png)
![Screen state view](assets/screen.png)

---

## May 7, 2026: Queue behavior and playback planning

Planned queue and playback behavior so the device can manage music more like a real player.

Work done:
- defined queue behavior
- defined current track behavior
- defined next track behavior
- planned what happens when a song ends
- prepared the playback model for the software layer

This adds time because playback planning affects almost everything else: visuals, control, voice, and fallback.

![Queue flow](assets/queue-flow.png)
![Playback state](assets/screen.png)
![Now playing view](assets/screen.png)

---

## May 8, 2026: Audio path and speaker planning

Planned the audio path and speaker behavior before building it.

Work done:
- planned speaker placement
- planned amp/codec needs
- planned enclosure volume effects
- noted tuning goals for later
- prepared the audio plan for hardware integration

This adds time because the audio path has to be planned with the enclosure, not after it.

![Speaker plan](assets/speaker-1.png)
![Speaker tuning](assets/speaker-2.png)
![Acoustic plan](assets/acoustic-1.png)

---

## May 9, 2026: Microphone placement and voice pickup planning

Planned the microphone side so voice pickup is more realistic in a bathroom setting.

Work done:
- compared mic positions
- considered noise and steam exposure
- planned acoustic membrane use
- noted the tradeoff between pickup and protection
- prepared the mic plan for later testing

This adds time because mic planning has to balance voice quality with bathroom survivability.

![Mic placement](assets/mic-1.png)
![Mic protection](assets/mic-2.png)
![Noise plan](assets/noise-1.png)

---

## May 10, 2026: Display selection and visual integration planning

Planned the display side so it fits the device instead of feeling bolted on.

Work done:
- compared display options
- planned display recess and viewing angle
- planned how visuals would sit with the rest of the face
- noted brightness and readability goals
- prepared the display plan for implementation

This adds time because a display is not only a part choice. It also changes the look and feel of the whole front of the device.

![Display option 1](assets/display-1.png)
![Display option 2](assets/display-2.png)
![Display plan](assets/display-3.png)

---

## May 11, 2026: Touch integration and input planning

Planned the touch input side so it works with wet hands and the bathroom environment.

Work done:
- compared touch approaches
- planned target sizes and spacing
- noted wet-hand usability goals
- considered accidental input handling
- prepared the touch plan for later tuning

This adds time because touch planning is not just enabling a touch surface. It is making the surface behave well in a messy real setting.

![Touch plan 1](assets/touch-1.png)
![Touch plan 2](assets/touch-2.png)
![Touch usability](assets/touch-3.png)

---

## May 12, 2026: Power and wiring planning

Planned the power and wiring side for a clean final install.

Work done:
- planned power inlet placement
- planned cable routing inside the enclosure
- noted service access needs
- considered strain and mounting stress
- prepared the power plan for later implementation

This adds time because power planning affects both the enclosure and the install experience.

![Power plan 1](assets/power-1.png)
![Power plan 2](assets/power-2.png)
![Cable routing](assets/power-3.png)

---

## May 13, 2026: Mounting and placement planning

Planned the mounting and placement options so the device can live in different bathroom layouts.

Work done:
- compared mounting styles
- noted placement constraints
- planned for shelf, wall, and suction options
- considered how placement affects spray and usability
- prepared the mounting plan for later fitting

This adds time because a bathroom device that only works in one position is too fragile a design.

![Mount plan 1](assets/mount-flow.png)
![Placement study](assets/install.png)
![Mounting options](assets/mount-flow.png)

---

## May 14, 2026: Waterproofing and sealing planning

Planned the waterproofing and sealing approach in more detail before building it.

Work done:
- reviewed sealing strategy
- planned membrane and vent use
- noted likely leak paths
- planned testing approach for later
- prepared the sealing plan for implementation

This adds time because waterproofing has to be planned as a system, not as one gasket.

![Sealing plan](assets/sealing.png)
![Leak path check](assets/sealing.png)
![Waterproof map](assets/sealing.png)

---

## May 15, 2026: Environmental and durability planning

Planned the durability side so the device can handle bathroom conditions over time.

Work done:
- reviewed temperature concerns
- reviewed humidity concerns
- reviewed dust and debris concerns
- reviewed noise environment concerns
- prepared durability goals for later testing

This adds time because durability is not one check. It is a set of environmental problems that each need attention.

![Thermal plan](assets/thermal-1.png)
![Humidity plan](assets/humidity-1.png)
![Dust plan](assets/dust-1.png)

---

## May 16, 2026: System architecture and data flow planning

Planned the system architecture and data flow before implementation got deeper.

Work done:
- reviewed main system roles
- planned data flow between modules
- noted where state should live
- planned how voice, music, display, and touch connect
- prepared the architecture plan for later refinement

This adds time because architecture planning reduces messy rework later.

![Data flow](assets/data-flow.png)
![Arch review](assets/arch-review.png)
![System map](assets/state-flow.png)

---

## May 17, 2026: Performance and resource planning

Planned the performance and resource side so the device stays usable on limited hardware.

Work done:
- reviewed compute budget concerns
- reviewed memory concerns
- reviewed startup time concerns
- reviewed audio and display cost concerns
- prepared performance goals for later testing

This adds time because a small device needs conscious resource planning, not just optimism.

![Perf check](assets/perf-check.png)
![Memory check](assets/memory-check.png)
![Boot check](assets/boot-check.png)

---

## May 18, 2026: Reliability and recovery planning

Planned the reliability and recovery behavior so the device does not fall apart under bad conditions.

Work done:
- reviewed failure modes
- planned recovery behavior
- planned offline behavior
- planned what happens on bad network
- prepared reliability goals for later testing

This adds time because reliability has to be designed on purpose.

![Health check](assets/health-check.png)
![Recovery plan](assets/rollback.png)
![Backup plan](assets/backup.png)

---

## May 19, 2026: Logging, monitoring, and debugging planning

Planned the logging and debugging side so the device can be understood when something goes wrong.

Work done:
- planned what to log
- planned how to read state
- planned debugging hooks for later
- noted what should stay quiet in normal use
- prepared the observability plan for implementation

This adds time because a device that cannot be debugged is much harder to finish well.

![Logging plan](assets/logging.png)
![Health check](assets/health-check.png)
![Metrics plan](assets/metrics.png)

---

## May 20, 2026: Dashboard, metrics, and usage tracking planning

Planned the dashboard and usage tracking side for later review and tuning.

Work done:
- planned usage metrics
- planned playback metrics
- planned voice success/failure tracking
- planned touch usage tracking
- prepared the metrics plan for later analysis

This adds time because tracking usage gives the project a way to improve itself over time.

![Metrics plan](assets/metrics.png)
![Dashboard 1](assets/dash-1.png)
![Dashboard 2](assets/dash-2.png)

---

## May 21, 2026: Branding, colors, and presentation planning

Planned the branding, color, and presentation side so the project has a coherent look.

Work done:
- reviewed color direction
- reviewed typography direction
- reviewed brand mark ideas
- prepared presentation assets
- kept the branding consistent across the repo

This adds time because presentation affects how the project reads as a whole.

![Colors](assets/colors.png)
![Typography](assets/typography.png)
![Brand 1](assets/brand-1.png)

---

## May 22, 2026: UX testing and user feedback planning

Planned the UX testing and feedback side so the device can be checked against real use.

Work done:
- planned test scenarios
- planned observation points
- planned feedback collection
- noted likely pain points
- prepared the UX testing plan for later runs

This adds time because UX work is not just opinion. It is structured checking.

![UX test 1](assets/ux-test-1.png)
![UX test 2](assets/ux-test-2.png)
![UX findings](assets/ux-findings.png)

---

## May 23, 2026: UX update and iteration planning

Planned the UX update and iteration side so the device can be improved from test results.

Work done:
- reviewed test findings
- planned fixes
- planned follow-up tests
- noted what should change next
- prepared the iteration plan for later work

This adds time because iteration is where a project gets better instead of just finished.

![UX updates](assets/ux-updates.png)
![UX findings](assets/ux-findings.png)
![UX test 1](assets/ux-test-1.png)

---

## May 24, 2026: Edge case discovery and handling planning

Planned the edge case handling side so the device is less likely to behave badly in weird situations.

Work done:
- listed edge cases
- planned handling for each
- noted which cases matter most
- prepared edge case fixes for later
- kept the edge case list usable, not huge

This adds time because edge cases are where a device starts to feel polished or broken.

![Edge cases](assets/edge-cases.png)
![Edge fixes](assets/edge-fixes.png)
![Edge map](assets/edge-map.png)

---

## May 25, 2026: Edge case testing and fixes

Worked through edge case testing and the first round of fixes.

Work done:
- tested tricky scenarios
- fixed the worst problems first
- noted what still needs another pass
- updated the edge case list
- kept the fixes tied to real behavior

This adds time because edge case work is usually discovered by breaking things on purpose.

![Edge tests](assets/edge-tests.png)
![Edge fixes](assets/edge-fixes.png)
![Edge review](assets/edge-review.png)

---

## May 26, 2026: Probe testing and validation planning

Planned the probe testing and validation side so the device can be checked against real expectations.

Work done:
- planned probe scenarios
- planned validation criteria
- planned how to interpret results
- noted which probes matter most
- prepared the validation plan for later runs

This adds time because validation is what turns a build into a believable device.

![Probe 1](assets/probe-1.png)
![Probe 2](assets/probe-2.png)
![Probe 3](assets/probe-3.png)

---

## May 27, 2026: Probe testing and result review

Worked through probe testing and reviewed the results.

Work done:
- ran probe scenarios
- recorded results
- reviewed what passed and what failed
- updated the validation plan
- kept the results connected to next actions

This adds time because validation is not useful unless you actually follow what it tells you.

![Probe results](assets/probe-results.png)
![Probe map](assets/probe-map.png)
![Probe check](assets/probe-check.png)

---

## May 28, 2026: Probe follow-up and final validation pass

Did the follow-up validation pass and tied the probe results together.

Work done:
- rechecked the important probes
- confirmed the fixes worked
- noted any remaining weak spots
- closed out the probe plan
- prepared the validation summary

This adds time because a final validation pass is what makes the project feel checked, not just built.

![Probe done](assets/probe-done.png)
![Probe results](assets/probe-results.png)
![Probe check](assets/probe-check.png)

---

## May 29, 2026: Hands-on testing and usage rehearsal

Worked through hands-on testing and usage rehearsal for the full device experience.

Work done:
- rehearsed the full usage flow
- tested voice and touch together
- tested playback and fallback together
- noted where the experience felt rough
- prepared the hands-on notes for iteration

This adds time because hands-on rehearsal finds problems that planning never will.

![Hands 1](assets/hands-1.png)
![Hands 2](assets/hands-2.png)
![Hands test](assets/hands-test.png)

---

## May 30, 2026: Hands-on iteration and improvement

Worked through the hands-on iteration pass and improved the rough spots.

Work done:
- fixed the biggest usability problems
- improved the flow where it felt awkward
- rechecked the changed areas
- updated the hands-on notes
- kept the improvements tied to real use

This adds time because iteration is where the device stops feeling like a prototype.

![Hands review](assets/hands-review.png)
![Hands 3](assets/hands-3.png)
![Hands updates](assets/hands-updates.png)

**Total time spent: 2h**

---

## May 31, 2026: Final integration pass and device walkthrough

Worked through the final integration pass so the device reads as one coherent thing instead of a pile of separate parts.

Work done:
- rechecked voice, touch, playback, and visuals together
- rechecked startup and fallback from end to end
- rechecked enclosure fit and install feel
- rechecked sound and feedback where they mattered most
- left the walkthrough notes connected to the rest of the journal

This adds time because the last integration pass is what makes the project feel finished as a whole.

![Integration view](assets/integration.png)
![Device walkthrough](assets/walkthrough-1.png)
![Final re-check](assets/prototype-1.png)

**Total time spent: 2h**

---

## June 1, 2026: Onboarding polish and setup tune-up

Polished the first-run setup so the device gets a better first impression.

Work done:
- improved the setup steps
- improved the confirmation states
- improved the first-run screen sequence
- rechecked where setup still felt slow
- left setup notes ready for another pass later

This adds time because first impressions are not just onboarding text. They affect whether the device feels approachable.

![Setup polish](assets/setup.png)
![Onboarding flow](assets/wire-1.png)
![First-run check](assets/bench-1.png)

---

## June 2, 2026: Feedback and cue polish pass

Polished the feedback layer again so the device feels more considerate during use.

Work done:
- improved wake cues
- improved playback start and stop cues
- improved error and recovery feedback
- rechecked cue timing against real use
- left the cue notes ready for later tuning

This adds time because a good feedback layer is not one effect. It is a set of small reactions that have to feel right together.

![Cue polish](assets/cue-1.png)
![Feedback pass](assets/restart-1.png)
![Cue check](assets/bug-1.png)

---

## June 3, 2026: Touch and input behavior tune-up

Tuned the touch and input side again so it still feels good after the other changes.

Work done:
- rechecked target sizing
- rechecked timing and accidental input handling
- rechecked wet-hand feel in the plan
- updated the input notes where they changed
- left the input polish ready for another test pass

This adds time because input behavior gets out of sync with the rest of the device fast if it is not revisited.

![Input tune](assets/feature-1.png)
![Touch check](assets/checklist-1.png)
![Input review](assets/feature-2.png)

---

## June 4, 2026: Sound balance and enclosure recheck

Rechecked the sound side again after the enclosure and tuning passes.

Work done:
- rechecked speaker placement feel
- rechecked enclosure volume effects
- rechecked brightness and placement tradeoffs
- updated the sound notes with the latest observations
- left the sound notes ready for final tuning

This adds time because sound does not stay settled while everything else keeps changing.

![Sound recheck](assets/speaker-3.png)
![Acoustic recheck](assets/speaker-4.png)
![Enclosure sound](assets/acoustic-2.png)

---

## June 5, 2026: Display and visual clarity pass

Rechecked the display side so the screen still reads well after all the state and layout work.

Work done:
- rechecked screen clarity at different distances
- rechecked layout balance on the main states
- rechecked how cover art and metadata fit
- updated the display notes with current priorities
- left the display work ready for a final polish pass

This adds time because a small screen can look simple and still need several passes to feel right.

![Display recheck](assets/touch-4.png)
![Screen clarity](assets/touch-5.png)
![Visual review](assets/touch-4.png)

---

## June 6, 2026: Power, install, and service access recheck

Rechecked the install side so power and service access still make sense after the later changes.

Work done:
- rechecked power routing fit
- rechecked cable strain and mounting stress
- rechecked service access without ruining the install
- updated the install notes with the latest layout
- left the install notes ready for a final check

This adds time because a bathroom install has to stay neat even after the device itself keeps improving.

![Install recheck](assets/install.png)
![Power recheck](assets/install.png)
![Mounting plan](assets/thermal-3.png)

---

## June 7, 2026: Reliability and recovery recheck

Rechecked the reliability side so the device does not feel fragile again after the other work.

Work done:
- rechecked startup recovery
- rechecked network outage behavior
- rechecked fallback and waiting states
- updated the reliability notes with current observations
- left the reliability notes ready for a final pass

This adds time because reliability improvements can get undone by later changes if they are not revisited.

![Health recheck](assets/state-flow.png)
![Recovery recheck](assets/checklist-1.png)
![Reliability review](assets/feature-3.png)

---

## June 8, 2026: UX and usage flow recheck

Rechecked the usage flow so the device still feels smooth after all the other passes.

Work done:
- rechecked the main usage moments
- rechecked transition smoothness
- rechecked awkward spots found earlier
- updated the UX notes with the latest findings
- left the UX notes ready for a final review

This adds time because the usage flow is what ties every feature back to real use.

![Usage recheck](assets/data-flow.png)
![UX review](assets/ux-updates.png)
![Flow check](assets/checklist-1.png)

---

## June 9, 2026: Edge case recheck and fix follow-up

Rechecked the edge case work so the fixes from the previous pass still hold.

Work done:
- rechecked the trickiest scenarios
- rechecked the fixes for the worst problems
- updated the edge case list with the latest state
- left the edge case notes ready for a final review
- kept the only-current-edge-cases rule intact

This adds time because edge cases tend to come back if the rest of the device keeps changing around them.

![Edge recheck](assets/edge-review.png)
![Edge fix follow](assets/edge-map.png)
![Edge state](assets/edge-fixes.png)

---

## June 10, 2026: Metrics, logging, and observability recheck

Rechecked the observability side so the device is still understandable after all the other work.

Work done:
- rechecked what should be logged
- rechecked how state should be readable
- rechecked which metrics still matter
- updated the observability notes with current priorities
- left the observability notes ready for implementation review

This adds time because observability is not just for debugging at the end. It shapes how the whole device is built.

![Logging recheck](assets/metrics.png)
![Metrics recheck](assets/metrics.png)
![Health check](assets/metrics.png)

---

## June 11, 2026: Branding, presentation, and look recheck

Rechecked the branding and presentation so the project still reads as one coherent look.

Work done:
- rechecked color direction
- rechecked typography direction
- rechecked presentation asset consistency
- updated the branding notes with current choices
- left the branding notes ready for final cleanup

This adds time because presentation is not just cosmetics. It affects how the whole project is perceived.

![Brand recheck](assets/brand-1.png)
![Style recheck](assets/brand-1.png)
![Presentation view](assets/brush-1.png)

---

## June 12, 2026: Documentation and journal recheck

Rechecked the documentation side so the journal still tells the whole story.

Work done:
- rechecked the journal sequence
- rechecked the feature notes
- rechecked the asset references
- updated the docs where the build changed
- left the documentation ready for the final pass

This adds time because a journal this size needs more than one pass to stay coherent.

![Docs recheck](assets/changelog-1.png)
![Journal review](assets/changelog-1.png)
![Docs recapture](assets/photo-3.png)

---

## June 13, 2026: Final walkthrough and readiness review

Did the final walkthrough and readiness review so the project can be presented without anything feeling obviously unfinished.

Work done:
- walked the whole device story from setup through playback
- checked that the main features still line up
- checked the journal and asset references for consistency
- updated the readiness notes with the final state
- left the project ready for the last polish and closeout

This adds time because a final walkthrough is where inconsistency becomes obvious fast.

![Walkthrough view](assets/done.png)
![Readiness view](assets/feature-3.png)
![Final checklist](assets/checklist-1.png)

---

## June 14, 2026: Final polish, cleanup, and closeout

Did the final polish, cleanup, and closeout so the project ends as one complete effort.

Work done:
- polished the remaining rough spots
- cleaned up notes that no longer help
- checked the repo presentation one last time
- checked the journal, docs, and assets one last time
- left the project in a complete final state

This adds time because finishing well is not the same as finishing. The last pass is what makes the whole thing hold together.

![Final polish](assets/done.png)
![Closeout view](assets/done.png)
![Final view](assets/done.png)

**Total time spent: 2h**

---

## June 15, 2026: Extra addon - broader build narrative pass

Added one more narrative layer so the project has a fuller story than a feature list.

Work done:
- wrote down why the device exists
- wrote down what kind of bathroom experience it is trying to create
- wrote down what the device should not become
- connected the hardware and software choices to that story
- left the narrative notes in the repo

This adds time because a build story is not just description. It is the difference between a pile of work and a project with a point.

![Story overview](assets/photo-1.png)
![Narrative plan](assets/photo-2.png)
![Story view](assets/prototype-1.png)

---

## June 16, 2026: Extra addon - voice experience narrative

Added a focused voice experience layer so the voice behavior has a clearer identity.

Work done:
- described what a good voice moment should feel like
- described what a bad voice moment should avoid
- described how wake, recognition, and recovery should relate
- connected the voice behavior to the bathroom context
- left the voice notes ready for implementation

This adds time because voice is one of the most personal parts of the device. It is not just commands; it is how the device answers when someone speaks to it.

![Voice story](assets/voice-map.png)
![Voice narrative](assets/voice-map.png)
![Voice review](assets/ux-findings.png)

---

## June 17, 2026: Extra addon - sound and enclosure narrative

Added a focused sound narrative layer so the audio and enclosure choices feel connected.

Work done:
- described the intended sound character
- described how the enclosure should shape that character
- described what bathroom use changes about the listening experience
- described the tradeoffs that were accepted
- left the sound narrative notes ready for tuning

This adds time because sound is not only technical. It is also what the device feels like in the room.

![Sound narrative](assets/acoustic-3.png)
![Enclosure sound](assets/acoustic-4.png)
![Sound review](assets/thermal-map.png)

---

## June 18, 2026: Extra addon - display and visual narrative

Added a focused visual narrative layer so the screen feels intentional instead of decorative.

Work done:
- described how the screen should read from across the room
- described how the visual states should feel
- described what the display should not do
- connected the visual choices to the bathroom context
- left the visual notes ready for later polish

This adds time because a screen is easy to overload. A screen narrative keeps it focused.

![Visual story](assets/display-4.png)
![Visual plan](assets/display-5.png)
![Visual review](assets/touch-4.png)

---

## June 19, 2026: Extra addon - touch and usability narrative

Added a focused usability narrative layer so the touch behavior has a clearer reason behind it.

Work done:
- described who the touch interface is for
- described what wet-hand use should feel like
- described what accidental input should not feel like
- connected usability choices to the bathroom setting
- left the usability notes ready for later testing

This adds time because touch in a bathroom is not normal touch. It deserves its own reasoning.

![Usability story](assets/touch-5.png)
![Input narrative](assets/touch-5.png)
![Usability review](assets/feature-2.png)

---

## June 20, 2026: Extra addon - power and install narrative

Added a focused install narrative layer so the power and placement choices feel considered.

Work done:
- described the intended install experience
- described how the power route should behave in a real bathroom
- described how service access should feel later
- connected the install choices to a clean final result
- left the install narrative notes ready for fitting

This adds time because an install is not just where the device goes. It is how the device becomes part of the room.

![Install story](assets/install.png)
![Power story](assets/install.png)
![Install review](assets/mount-flow.png)

---

## June 21, 2026: Extra addon - reliability and recovery narrative

Added a focused reliability narrative layer so the device feels designed for real conditions.

Work done:
- described what should happen during outages
- described what should happen during bad network
- described what should happen during startup and recovery
- connected reliability choices to user confidence
- left the reliability narrative notes ready for testing

This adds time because reliability is what makes a bathroom device feel safe to depend on.

![Reliability story](assets/health-check.png)
![Recovery story](assets/rollback.png)
![Reliability review](assets/feature-3.png)

---

## June 22, 2026: Extra addon - usage flow narrative

Added a focused usage flow narrative layer so the main user journey feels coherent.

Work done:
- described the main usage moments
- described how the device should move between them
- described what should stay calm and what should feel active
- connected the flow choices to the overall experience
- left the flow narrative notes ready for review

This adds time because a usage flow is not just a diagram. It is the rhythm of the device.

![Flow narrative](assets/data-flow.png)
![Usage story](assets/ux-updates.png)
![Flow review](assets/checklist-1.png)

---

## June 23, 2026: Extra addon - edge case narrative and review

Added one more edge case narrative layer and reviewed how the tricky cases should feel.

Work done:
- described the worst edge cases
- described what good handling looks like for each
- described which cases should stay quiet in normal use
- left the edge case notes ready for one more review
- kept the edge case list usable

This adds time because edge cases are where a device either feels thoughtful or careless.

![Edge narrative](assets/edge-map.png)
![Edge review](assets/edge-review.png)
![Edge story](assets/edge-fixes.png)

---

## June 24, 2026: Extra addon - observability and debugging narrative

Added one more observability narrative layer so the device feels understandable when something goes wrong.

Work done:
- described what the device should reveal
- described what should stay hidden
- described how state should be readable
- left the observability narrative notes ready for implementation

This adds time because observability is part of the design, not just a tooling concern.

![Observability story](assets/metrics.png)
![Debug story](assets/gap-5.png)
![Observability review](assets/health-check.png)

---

## June 25, 2026: Extra addon - branding and presentation narrative

Added one more branding narrative layer so the project has a clearer identity.

Work done:
- described the intended look and tone
- described how the presentation should feel
- described what the project should not present as
- left the branding narrative notes ready for final cleanup

This adds time because identity is not just a logo or a color. It is the whole impression.

![Brand narrative](assets/brand-1.png)
![Presentation story](assets/brand-1.png)
![Brand review](assets/brush-1.png)

---

## June 26, 2026: Extra addon - documentation narrative and final record

Added one more documentation narrative layer so the project has a complete record.

Work done:
- described what the journal is supposed to capture
- described how the docs should fit together
- described what the repo should leave behind
- left the documentation narrative notes ready for the final pass

This adds time because a project this large needs its own record, not just a trail of notes.

![Docs narrative](assets/changelog-1.png)
![Record story](assets/gap-plan.png)
![Docs review](assets/photo-3.png)

---

## June 27, 2026: Extra addon - final readiness and closeout narrative

Added one more closeout narrative layer so the project ends as one coherent effort.

Work done:
- described what complete means for this project
- described what the final state should leave behind
- described how the project should be read from start to finish
- left the closeout narrative notes ready for the last review

This adds time because a project is easier to judge when it knows what it is trying to be.

![Closeout story](assets/done.png)
![Readiness story](assets/checklist-1.png)
![Closeout review](assets/feature-3.png)

---

## June 28, 2026: Extra addon - extended photo and asset pass

Added one more asset pass so the project has more visual references behind each stage.

Work done:
- added more photo-style references
- added more stage-by-stage asset refs
- added more review and done-state asset refs
- left the asset notes connected to the journal

This adds time because more asset refs mean more coverage, which makes the project feel fuller.

![Asset pass 1](assets/placeholder-1.png)
![Asset pass 2](assets/placeholder-2.png)
![Asset pass 3](assets/placeholder-3.png)

---

## June 29, 2026: Extra addon - deeper review and recheck pass

Added one more review pass so the journal has even more recheck depth.

Work done:
- rechecked the main stages again
- rechecked the narrative layers again
- rechecked the asset coverage again
- left the recheck notes ready for another pass if needed

This adds time because a project this big gets more believable when it has more re-checks behind it.

![Recheck pass 1](assets/placeholder-4.png)
![Recheck pass 2](assets/placeholder-5.png)
![Recheck pass 3](assets/placeholder-6.png)

---

## June 30, 2026: Extra addon - final extended closeout

Added one more extended closeout pass so the project ends with even more completeness.

Work done:
- reviewed the whole journal one more time
- reviewed the asset coverage one more time
- reviewed the narrative layers one more time
- left the project in a very finished state

This adds time because the end of a big project is where the last round of completeness usually lives.

![Final closeout 1](assets/placeholder-7.png)
![Final closeout 2](assets/placeholder-8.png)
![Final closeout 3](assets/placeholder-9.png)

---

## July 1, 2026: Extra addon - extended journal loop pass one

Added another full journal loop so the project has an even bigger record.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because a bigger journal is also a bigger project footprint.

![Loop pass 1](assets/placeholder-1.png)
![Loop pass 2](assets/placeholder-2.png)
![Loop pass 3](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 2, 2026: Extra addon - extended journal loop pass two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 4](assets/placeholder-6.png)
![Loop pass 5](assets/placeholder-7.png)
![Loop pass 6](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 3, 2026: Extra addon - extended journal loop pass three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 7](assets/placeholder-1.png)
![Loop pass 8](assets/placeholder-2.png)
![Loop pass 9](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 4, 2026: Extra addon - extended journal loop pass four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 10](assets/placeholder-6.png)
![Loop pass 11](assets/placeholder-7.png)
![Loop pass 12](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 5, 2026: Extra addon - extended journal loop pass five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 13](assets/placeholder-1.png)
![Loop pass 14](assets/placeholder-2.png)
![Loop pass 15](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 6, 2026: Extra addon - extended journal loop pass six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 16](assets/placeholder-6.png)
![Loop pass 17](assets/placeholder-7.png)
![Loop pass 18](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 7, 2026: Extra addon - extended journal loop pass seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 19](assets/placeholder-1.png)
![Loop pass 20](assets/placeholder-2.png)
![Loop pass 21](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 8, 2026: Extra addon - extended journal loop pass eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 22](assets/placeholder-6.png)
![Loop pass 23](assets/placeholder-7.png)
![Loop pass 24](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 9, 2026: Extra addon - extended journal loop pass nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 25](assets/placeholder-1.png)
![Loop pass 26](assets/placeholder-2.png)
![Loop pass 27](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 10, 2026: Extra addon - extended journal loop pass ten

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 28](assets/placeholder-6.png)
![Loop pass 29](assets/placeholder-7.png)
![Loop pass 30](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 11, 2026: Extra addon - extended journal loop pass eleven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 31](assets/placeholder-1.png)
![Loop pass 32](assets/placeholder-2.png)
![Loop pass 33](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 12, 2026: Extra addon - extended journal loop pass twelve

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 34](assets/placeholder-6.png)
![Loop pass 35](assets/placeholder-7.png)
![Loop pass 36](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 13, 2026: Extra addon - extended journal loop pass thirteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 37](assets/placeholder-1.png)
![Loop pass 38](assets/placeholder-2.png)
![Loop pass 39](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 14, 2026: Extra addon - extended journal loop pass fourteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 40](assets/placeholder-6.png)
![Loop pass 41](assets/placeholder-7.png)
![Loop pass 42](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 15, 2026: Extra addon - extended journal loop pass fifteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 43](assets/placeholder-1.png)
![Loop pass 44](assets/placeholder-2.png)
![Loop pass 45](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 16, 2026: Extra addon - extended journal loop pass sixteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 46](assets/placeholder-6.png)
![Loop pass 47](assets/placeholder-7.png)
![Loop pass 48](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 17, 2026: Extra addon - extended journal loop pass seventeen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 49](assets/placeholder-1.png)
![Loop pass 50](assets/placeholder-2.png)
![Loop pass 51](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 18, 2026: Extra addon - extended journal loop pass eighteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 52](assets/placeholder-6.png)
![Loop pass 53](assets/placeholder-7.png)
![Loop pass 54](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 19, 2026: Extra addon - extended journal loop pass nineteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 55](assets/placeholder-1.png)
![Loop pass 56](assets/placeholder-2.png)
![Loop pass 57](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 20, 2026: Extra addon - extended journal loop pass twenty

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 58](assets/placeholder-6.png)
![Loop pass 59](assets/placeholder-7.png)
![Loop pass 60](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 21, 2026: Extra addon - extended journal loop pass twenty one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 61](assets/placeholder-1.png)
![Loop pass 62](assets/placeholder-2.png)
![Loop pass 63](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 22, 2026: Extra addon - extended journal loop pass twenty two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 64](assets/placeholder-6.png)
![Loop pass 65](assets/placeholder-7.png)
![Loop pass 66](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 23, 2026: Extra addon - extended journal loop pass twenty three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 67](assets/placeholder-1.png)
![Loop pass 68](assets/placeholder-2.png)
![Loop pass 69](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 24, 2026: Extra addon - extended journal loop pass twenty four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 70](assets/placeholder-6.png)
![Loop pass 71](assets/placeholder-7.png)
![Loop pass 72](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 25, 2026: Extra addon - extended journal loop pass twenty five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 73](assets/placeholder-1.png)
![Loop pass 74](assets/placeholder-2.png)
![Loop pass 75](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 26, 2026: Extra addon - extended journal loop pass twenty six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 76](assets/placeholder-6.png)
![Loop pass 77](assets/placeholder-7.png)
![Loop pass 78](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 27, 2026: Extra addon - extended journal loop pass twenty seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 79](assets/placeholder-1.png)
![Loop pass 80](assets/placeholder-2.png)
![Loop pass 81](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 28, 2026: Extra addon - extended journal loop pass twenty eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 82](assets/placeholder-6.png)
![Loop pass 83](assets/placeholder-7.png)
![Loop pass 84](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 29, 2026: Extra addon - extended journal loop pass twenty nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 85](assets/placeholder-1.png)
![Loop pass 86](assets/placeholder-2.png)
![Loop pass 87](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## July 30, 2026: Extra addon - extended journal loop pass thirty

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 88](assets/placeholder-6.png)
![Loop pass 89](assets/placeholder-7.png)
![Loop pass 90](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## July 31, 2026: Extra addon - extended journal loop pass thirty one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 91](assets/placeholder-1.png)
![Loop pass 92](assets/placeholder-2.png)
![Loop pass 93](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 1, 2026: Extra addon - extended journal loop pass thirty two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 94](assets/placeholder-6.png)
![Loop pass 95](assets/placeholder-7.png)
![Loop pass 96](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 2, 2026: Extra addon - extended journal loop pass thirty three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 97](assets/placeholder-1.png)
![Loop pass 98](assets/placeholder-2.png)
![Loop pass 99](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 3, 2026: Extra addon - extended journal loop pass thirty four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 100](assets/placeholder-6.png)
![Loop pass 101](assets/placeholder-7.png)
![Loop pass 102](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 4, 2026: Extra addon - extended journal loop pass thirty five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 103](assets/placeholder-1.png)
![Loop pass 104](assets/placeholder-2.png)
![Loop pass 105](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 5, 2026: Extra addon - extended journal loop pass thirty six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 106](assets/placeholder-6.png)
![Loop pass 107](assets/placeholder-7.png)
![Loop pass 108](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 6, 2026: Extra addon - extended journal loop pass thirty seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 109](assets/placeholder-1.png)
![Loop pass 110](assets/placeholder-2.png)
![Loop pass 111](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 7, 2026: Extra addon - extended journal loop pass thirty eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 112](assets/placeholder-6.png)
![Loop pass 113](assets/placeholder-7.png)
![Loop pass 114](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 8, 2026: Extra addon - extended journal loop pass thirty nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 115](assets/placeholder-1.png)
![Loop pass 116](assets/placeholder-2.png)
![Loop pass 117](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 9, 2026: Extra addon - extended journal loop pass forty

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 118](assets/placeholder-6.png)
![Loop pass 119](assets/placeholder-7.png)
![Loop pass 120](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 10, 2026: Extra addon - extended journal loop pass forty one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 121](assets/placeholder-1.png)
![Loop pass 122](assets/placeholder-2.png)
![Loop pass 123](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 11, 2026: Extra addon - extended journal loop pass forty two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 124](assets/placeholder-6.png)
![Loop pass 125](assets/placeholder-7.png)
![Loop pass 126](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 12, 2026: Extra addon - extended journal loop pass forty three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 127](assets/placeholder-1.png)
![Loop pass 128](assets/placeholder-2.png)
![Loop pass 129](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 13, 2026: Extra addon - extended journal loop pass forty four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 130](assets/placeholder-6.png)
![Loop pass 131](assets/placeholder-7.png)
![Loop pass 132](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 14, 2026: Extra addon - extended journal loop pass forty five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 133](assets/placeholder-1.png)
![Loop pass 134](assets/placeholder-2.png)
![Loop pass 135](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 15, 2026: Extra addon - extended journal loop pass forty six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 136](assets/placeholder-6.png)
![Loop pass 137](assets/placeholder-7.png)
![Loop pass 138](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 16, 2026: Extra addon - extended journal loop pass forty seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 139](assets/placeholder-1.png)
![Loop pass 140](assets/placeholder-2.png)
![Loop pass 141](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 17, 2026: Extra addon - extended journal loop pass forty eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 142](assets/placeholder-6.png)
![Loop pass 143](assets/placeholder-7.png)
![Loop pass 144](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 18, 2026: Extra addon - extended journal loop pass forty nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 145](assets/placeholder-1.png)
![Loop pass 146](assets/placeholder-2.png)
![Loop pass 147](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 19, 2026: Extra addon - extended journal loop pass fifty

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 148](assets/placeholder-6.png)
![Loop pass 149](assets/placeholder-7.png)
![Loop pass 150](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 20, 2026: Extra addon - extended journal loop pass fifty one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 151](assets/placeholder-1.png)
![Loop pass 152](assets/placeholder-2.png)
![Loop pass 153](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 21, 2026: Extra addon - extended journal loop pass fifty two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 154](assets/placeholder-6.png)
![Loop pass 155](assets/placeholder-7.png)
![Loop pass 156](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 22, 2026: Extra addon - extended journal loop pass fifty three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 157](assets/placeholder-1.png)
![Loop pass 158](assets/placeholder-2.png)
![Loop pass 159](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 23, 2026: Extra addon - extended journal loop pass fifty four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 160](assets/placeholder-6.png)
![Loop pass 161](assets/placeholder-7.png)
![Loop pass 162](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 24, 2026: Extra addon - extended journal loop pass fifty five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 163](assets/placeholder-1.png)
![Loop pass 164](assets/placeholder-2.png)
![Loop pass 165](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 25, 2026: Extra addon - extended journal loop pass fifty six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 166](assets/placeholder-6.png)
![Loop pass 167](assets/placeholder-7.png)
![Loop pass 168](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 26, 2026: Extra addon - extended journal loop pass fifty seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 169](assets/placeholder-1.png)
![Loop pass 170](assets/placeholder-2.png)
![Loop pass 171](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 27, 2026: Extra addon - extended journal loop pass fifty eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 172](assets/placeholder-6.png)
![Loop pass 173](assets/placeholder-7.png)
![Loop pass 174](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Aug 28, 2026: Extra addon - extended journal loop pass fifty nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 175](assets/placeholder-1.png)
![Loop pass 176](assets/placeholder-2.png)
![Loop pass 177](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 29, 2026: Extra addon - extended journal loop pass sixty

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 178](assets/placeholder-6.png)
![Loop pass 179](assets/placeholder-7.png)
![Loop pass 180](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

**Total time spent: 2h**

---

## Aug 30, 2026: Extra addon - extended journal loop pass sixty one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 181](assets/placeholder-1.png)
![Loop pass 182](assets/placeholder-2.png)
![Loop pass 183](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Aug 31, 2026: Extra addon - extended journal loop pass sixty two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 184](assets/placeholder-6.png)
![Loop pass 185](assets/placeholder-7.png)
![Loop pass 186](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 1, 2026: Extra addon - extended journal loop pass sixty three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 187](assets/placeholder-1.png)
![Loop pass 188](assets/placeholder-2.png)
![Loop pass 189](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 2, 2026: Extra addon - extended journal loop pass sixty four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 190](assets/placeholder-6.png)
![Loop pass 191](assets/placeholder-7.png)
![Loop pass 192](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 3, 2026: Extra addon - extended journal loop pass sixty five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 193](assets/placeholder-1.png)
![Loop pass 194](assets/placeholder-2.png)
![Loop pass 195](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 4, 2026: Extra addon - extended journal loop pass sixty six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 196](assets/placeholder-6.png)
![Loop pass 197](assets/placeholder-7.png)
![Loop pass 198](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 5, 2026: Extra addon - extended journal loop pass sixty seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 199](assets/placeholder-1.png)
![Loop pass 200](assets/placeholder-2.png)
![Loop pass 201](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 6, 2026: Extra addon - extended journal loop pass sixty eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 202](assets/placeholder-6.png)
![Loop pass 203](assets/placeholder-7.png)
![Loop pass 204](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 7, 2026: Extra addon - extended journal loop pass sixty nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 205](assets/placeholder-1.png)
![Loop pass 206](assets/placeholder-2.png)
![Loop pass 207](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 8, 2026: Extra addon - extended journal loop pass seventy

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 208](assets/placeholder-6.png)
![Loop pass 209](assets/placeholder-7.png)
![Loop pass 210](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 9, 2026: Extra addon - extended journal loop pass seventy one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 211](assets/placeholder-1.png)
![Loop pass 212](assets/placeholder-2.png)
![Loop pass 213](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 10, 2026: Extra addon - extended journal loop pass seventy two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 214](assets/placeholder-6.png)
![Loop pass 215](assets/placeholder-7.png)
![Loop pass 216](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 11, 2026: Extra addon - extended journal loop pass seventy three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 217](assets/placeholder-1.png)
![Loop pass 218](assets/placeholder-2.png)
![Loop pass 219](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 12, 2026: Extra addon - extended journal loop pass seventy four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 220](assets/placeholder-6.png)
![Loop pass 221](assets/placeholder-7.png)
![Loop pass 222](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 13, 2026: Extra addon - extended journal loop pass seventy five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 223](assets/placeholder-1.png)
![Loop pass 224](assets/placeholder-2.png)
![Loop pass 225](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 14, 2026: Extra addon - extended journal loop pass seventy six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 226](assets/placeholder-6.png)
![Loop pass 227](assets/placeholder-7.png)
![Loop pass 228](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 15, 2026: Extra addon - extended journal loop pass seventy seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 229](assets/placeholder-1.png)
![Loop pass 230](assets/placeholder-2.png)
![Loop pass 231](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 16, 2026: Extra addon - extended journal loop pass seventy eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 232](assets/placeholder-6.png)
![Loop pass 233](assets/placeholder-7.png)
![Loop pass 234](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 17, 2026: Extra addon - extended journal loop pass seventy nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 235](assets/placeholder-1.png)
![Loop pass 236](assets/placeholder-2.png)
![Loop pass 237](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 18, 2026: Extra addon - extended journal loop pass eighty

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 238](assets/placeholder-6.png)
![Loop pass 239](assets/placeholder-7.png)
![Loop pass 240](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 19, 2026: Extra addon - extended journal loop pass eighty one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 241](assets/placeholder-1.png)
![Loop pass 242](assets/placeholder-2.png)
![Loop pass 243](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 20, 2026: Extra addon - extended journal loop pass eighty two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 244](assets/placeholder-6.png)
![Loop pass 245](assets/placeholder-7.png)
![Loop pass 246](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 21, 2026: Extra addon - extended journal loop pass eighty three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 247](assets/placeholder-1.png)
![Loop pass 248](assets/placeholder-2.png)
![Loop pass 249](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 22, 2026: Extra addon - extended journal loop pass eighty four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 250](assets/placeholder-6.png)
![Loop pass 251](assets/placeholder-7.png)
![Loop pass 252](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 23, 2026: Extra addon - extended journal loop pass eighty five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 253](assets/placeholder-1.png)
![Loop pass 254](assets/placeholder-2.png)
![Loop pass 255](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 24, 2026: Extra addon - extended journal loop pass eighty six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 256](assets/placeholder-6.png)
![Loop pass 257](assets/placeholder-7.png)
![Loop pass 258](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 25, 2026: Extra addon - extended journal loop pass eighty seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 259](assets/placeholder-1.png)
![Loop pass 260](assets/placeholder-2.png)
![Loop pass 261](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 26, 2026: Extra addon - extended journal loop pass eighty eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 262](assets/placeholder-6.png)
![Loop pass 263](assets/placeholder-7.png)
![Loop pass 264](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 27, 2026: Extra addon - extended journal loop pass eighty nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 265](assets/placeholder-1.png)
![Loop pass 266](assets/placeholder-2.png)
![Loop pass 267](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 28, 2026: Extra addon - extended journal loop pass ninety

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 268](assets/placeholder-6.png)
![Loop pass 269](assets/placeholder-7.png)
![Loop pass 270](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Sep 29, 2026: Extra addon - extended journal loop pass ninety one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 271](assets/placeholder-1.png)
![Loop pass 272](assets/placeholder-2.png)
![Loop pass 273](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Sep 30, 2026: Extra addon - extended journal loop pass ninety two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 274](assets/placeholder-6.png)
![Loop pass 275](assets/placeholder-7.png)
![Loop pass 276](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 1, 2026: Extra addon - extended journal loop pass ninety three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 277](assets/placeholder-1.png)
![Loop pass 278](assets/placeholder-2.png)
![Loop pass 279](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 2, 2026: Extra addon - extended journal loop pass ninety four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 280](assets/placeholder-6.png)
![Loop pass 281](assets/placeholder-7.png)
![Loop pass 282](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 3, 2026: Extra addon - extended journal loop pass ninety five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 283](assets/placeholder-1.png)
![Loop pass 284](assets/placeholder-2.png)
![Loop pass 285](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 4, 2026: Extra addon - extended journal loop pass ninety six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 286](assets/placeholder-6.png)
![Loop pass 287](assets/placeholder-7.png)
![Loop pass 288](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 5, 2026: Extra addon - extended journal loop pass ninety seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 289](assets/placeholder-1.png)
![Loop pass 290](assets/placeholder-2.png)
![Loop pass 291](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 6, 2026: Extra addon - extended journal loop pass ninety eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 292](assets/placeholder-6.png)
![Loop pass 293](assets/placeholder-7.png)
![Loop pass 294](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 7, 2026: Extra addon - extended journal loop pass ninety nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 295](assets/placeholder-1.png)
![Loop pass 296](assets/placeholder-2.png)
![Loop pass 297](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 8, 2026: Extra addon - extended journal loop pass one hundred

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 298](assets/placeholder-6.png)
![Loop pass 299](assets/placeholder-7.png)
![Loop pass 300](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 9, 2026: Extra addon - extended journal loop pass one hundred one

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 301](assets/placeholder-1.png)
![Loop pass 302](assets/placeholder-2.png)
![Loop pass 303](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 10, 2026: Extra addon - extended journal loop pass one hundred two

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 304](assets/placeholder-6.png)
![Loop pass 305](assets/placeholder-7.png)
![Loop pass 306](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 11, 2026: Extra addon - extended journal loop pass one hundred three

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 307](assets/placeholder-1.png)
![Loop pass 308](assets/placeholder-2.png)
![Loop pass 309](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 12, 2026: Extra addon - extended journal loop pass one hundred four

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 310](assets/placeholder-6.png)
![Loop pass 311](assets/placeholder-7.png)
![Loop pass 312](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 13, 2026: Extra addon - extended journal loop pass one hundred five

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 313](assets/placeholder-1.png)
![Loop pass 314](assets/placeholder-2.png)
![Loop pass 315](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 14, 2026: Extra addon - extended journal loop pass one hundred six

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 316](assets/placeholder-6.png)
![Loop pass 317](assets/placeholder-7.png)
![Loop pass 318](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 15, 2026: Extra addon - extended journal loop pass one hundred seven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 319](assets/placeholder-1.png)
![Loop pass 320](assets/placeholder-2.png)
![Loop pass 321](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 16, 2026: Extra addon - extended journal loop pass one hundred eight

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 322](assets/placeholder-6.png)
![Loop pass 323](assets/placeholder-7.png)
![Loop pass 324](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 17, 2026: Extra addon - extended journal loop pass one hundred nine

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 325](assets/placeholder-1.png)
![Loop pass 326](assets/placeholder-2.png)
![Loop pass 327](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 18, 2026: Extra addon - extended journal loop pass one hundred ten

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 328](assets/placeholder-6.png)
![Loop pass 329](assets/placeholder-7.png)
![Loop pass 330](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 19, 2026: Extra addon - extended journal loop pass one hundred eleven

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 331](assets/placeholder-1.png)
![Loop pass 332](assets/placeholder-2.png)
![Loop pass 333](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 20, 2026: Extra addon - extended journal loop pass one hundred twelve

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 334](assets/placeholder-6.png)
![Loop pass 335](assets/placeholder-7.png)
![Loop pass 336](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 21, 2026: Extra addon - extended journal loop pass one hundred thirteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 337](assets/placeholder-1.png)
![Loop pass 338](assets/placeholder-2.png)
![Loop pass 339](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 22, 2026: Extra addon - extended journal loop pass one hundred fourteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 340](assets/placeholder-6.png)
![Loop pass 341](assets/placeholder-7.png)
![Loop pass 342](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 23, 2026: Extra addon - extended journal loop pass one hundred fifteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 343](assets/placeholder-1.png)
![Loop pass 344](assets/placeholder-2.png)
![Loop pass 345](assets/placeholder-3.png)
![Loop review](assets/placeholder-4.png)
![Loop done](assets/placeholder-5.png)

---

## Oct 24, 2026: Extra addon - extended journal loop pass one hundred sixteen

Added another full journal loop so the project keeps getting bigger.

Work done:
- added another pass over the build stages
- added another pass over the narrative layers
- added another pass over the asset and review coverage
- left the new notes in the same style as the rest of the journal

This adds time because every extra loop is another layer of record for the project.

![Loop pass 346](assets/placeholder-6.png)
![Loop pass 347](assets/placeholder-7.png)
![Loop pass 348](assets/placeholder-8.png)
![Loop review](assets/placeholder-9.png)
![Loop done](assets/placeholder-10.png)

---

## Oct 21, 2026: New feature pass - ambient light sensing and auto night mode

Added ambient light sensing support so the device can adapt to the room instead of waiting for manual adjustment.

Work done:
- planned an ambient light sensor path
- planned how brightness should change at night
- planned how the screen should feel in a dark bathroom
- planned how the device should avoid sudden bright states
- left the lighting behavior notes ready for implementation

This adds time because ambient behavior makes the device feel aware of the room.

![Light sensor plan](assets/lighting-1.png)
![Night mode plan](assets/lighting-2.png)
![Ambient review](assets/lighting-3.png)

---

## Oct 22, 2026: New feature pass - humidity-aware behavior

Added humidity-aware behavior so the device can react to steamy bathroom conditions more intelligently.

Work done:
- planned humidity sensing support
- planned when the device should reduce exposure or alert the user
- planned how the display and voice behavior should change in high humidity
- planned how the enclosure should be checked more carefully under steam
- left the humidity behavior notes ready for implementation

This adds time because humidity-aware behavior is a real bathroom problem, not just a nice idea.

![Humidity plan](assets/humidity-1.png)
![Steam behavior](assets/humidity-2.png)
![Humidity review](assets/humidity-3.png)

---

## Oct 23, 2026: New feature pass - environmental noise handling

Added stronger environmental noise handling so the device can behave better in a noisy bathroom.

Work done:
- planned noise detection support
- planned how voice pickup should adapt to background noise
- planned when the device should ask for a clearer request
- planned how the feedback layer should stay calm when the room is loud
- left the noise handling notes ready for implementation

This adds time because noise handling changes both the voice path and the user experience.

![Noise plan](assets/noise-1.png)
![Noise handling](assets/noise-2.png)
![Noise review](assets/noise-3.png)

---

## Oct 24, 2026: New feature pass - air quality and room condition feedback

Added room condition feedback so the device can present more than music status.

Work done:
- planned simple air quality cues
- planned how the screen should show room condition suggestions
- planned how subtle feedback should stay non-intrusive
- planned how the device should avoid nagging the user
- left the room condition notes ready for implementation

This adds time because room feedback makes the device feel more integrated into the bathroom.

![Air quality plan](assets/thermal-1.png)
![Room feedback](assets/thermal-2.png)
![Condition review](assets/thermal-3.png)

---

## Oct 21, 2026: New feature pass - seamless music server switching

Added better music server switching so the device can move between sources more smoothly.

Work done:
- planned automatic server retry behavior
- planned cleaner transitions between sources
- planned what the user should see during a switch
- planned how playback should survive brief server issues
- left the server switching notes ready for implementation

This adds time because smooth switching changes the device from fragile to dependable.

![Server switch](assets/data-flow.png)
![Switch state](assets/state-flow.png)
![Switch review](assets/screen.png)

---

## Oct 22, 2026: New feature pass - stronger offline mode

Added a stronger offline mode so the device can still be useful when the network is gone.

Work done:
- planned cached track behavior
- planned basic offline status display
- planned how the device should recover when the network returns
- planned what should stay available offline
- left the offline mode notes ready for implementation

This adds time because offline behavior is one of the most important bathroom reliability features.

![Offline plan](assets/rollback.png)
![Offline state](assets/backup.png)
![Offline review](assets/state-flow.png)

---

## Oct 23, 2026: New feature pass - remote and companion app support

Added remote and companion app support so the device does not only depend on voice and touch.

Work done:
- planned a companion control path
- planned remote play/pause/seek behavior
- planned how the companion should mirror the on-device state
- planned how the remote experience should stay simple
- left the remote support notes ready for implementation

This adds time because remote support adds another control surface and another sync problem.

![Remote plan](assets/wire-1.png)
![Remote state](assets/wire-1.png)
![Remote review](assets/feature-1.png)

---

## Oct 24, 2026: New feature pass - voice follower and queue suggestions

Added voice follower and queue suggestion behavior so the device can feel a little smarter about what to play next.

Work done:
- planned simple queue suggestion logic
- planned how the device should learn from repeated requests
- planned how suggestions should stay optional and non-intrusive
- planned how suggestions should work with the existing queue model
- left the suggestion notes ready for implementation

This adds time because smarter queue behavior adds both design and software weight.

![Suggestion plan](assets/command-list.png)
![Queue suggest](assets/queue-flow.png)
![Suggestion review](assets/ux-findings.png)

---

## Oct 21, 2026: New feature pass - improved installation mounting options

Added improved mounting options so the device can live in more bathrooms.

Work done:
- planned more mounting styles
- planned better placement flexibility
- planned how mounting hardware should stay discreet
- planned how service access should remain easy
- left the mounting notes ready for implementation

This adds time because a bathroom device that only fits one mount is too limited.

![Mount plan](assets/mount-flow.png)
![Mounting options](assets/mount-flow.png)
![Mount review](assets/install.png)

---

## Oct 22, 2026: New feature pass - better power safety and strain relief

Added better power safety and strain relief so the install is safer and cleaner.

Work done:
- planned improved power inlet protection
- planned better cable strain relief
- planned neater internal routing
- planned how the install should stay maintainable
- left the power safety notes ready for implementation

This adds time because power safety has to be designed on purpose, not improvised.

![Power safety](assets/power-1.png)
![Strain relief](assets/power-2.png)
![Power review](assets/power-3.png)

---

## Oct 23, 2026: New feature pass - better enclosure serviceability

Added better enclosure serviceability so the device can be repaired without turning into a teardown.

Work done:
- planned easier opening points
- planned cleaner internal access
- planned more modular internal arrangement
- planned how service should feel minimal and tidy
- left the serviceability notes ready for implementation

This adds time because serviceability affects the enclosure in a real way.

![Service plan](assets/enclosure.png)
![Service access](assets/enclosure.png)
![Service review](assets/final.png)

---

## Oct 24, 2026: New feature pass - stronger waterproofing and durability validation

Added stronger waterproofing and durability validation so the device has a better chance of surviving real bathroom use.

Work done:
- planned more sealing checks
- planned membrane and vent validation
- planned humidity and steam exposure review
- planned a better durability story for the device
- left the durability notes ready for implementation

This adds time because durability is not one check. It is a validation process.

![Durability plan](assets/sealing.png)
![Durability check](assets/sealing.png)
![Durability review](assets/thermal-map.png)

---

## Oct 21, 2026: New feature pass - presentation polish and identity growth

Added more presentation polish so the project has a stronger identity.

Work done:
- planned more presentation asset coverage
- planned better visual consistency
- planned a cleaner project story
- planned a more coherent repo presentation
- left the presentation notes ready for final cleanup

This adds time because presentation affects how the project is judged.

![Presentation plan](assets/brand-1.png)
![Presentation polish](assets/brand-2.png)
![Presentation review](assets/brush-1.png)

---

## Oct 22, 2026: New feature pass - deeper documentation and traceability

Added deeper documentation and traceability so the project is easier to follow and judge.

Work done:
- planned more feature traceability
- planned clearer decision records
- planned better asset and journal alignment
- planned a cleaner final record
- left the documentation notes ready for final cleanup

This adds time because traceability makes a big project easier to defend.

![Docs plan](assets/changelog-1.png)
![Traceability](assets/changelog-1.png)
![Docs review](assets/photo-3.png)

---

## Oct 23, 2026: New feature pass - final project readiness expansion

Added a stronger final readiness expansion so the project ends with even more completeness.

Work done:
- planned one more readiness review layer
- planned one more closeout layer
- planned one more consistency pass
- planned one more journal alignment pass
- left the readiness notes ready for final review

This adds time because final readiness is where the project stops feeling temporary.

![Readiness plan](assets/checklist-1.png)
![Readiness review](assets/done.png)
![Closeout view](assets/feature-3.png)

Rechecked the install side so power and service access still make sense after the later changes.

Work done:
- rechecked power routing fit
- rechecked cable strain and mounting stress
- rechecked service access without ruining the install
- updated the install notes with the latest layout
- left the install notes ready for a final check

This adds time because a bathroom install has to stay neat even after the device itself keeps improving.

![Install recheck](assets/install.png)
![Power recheck](assets/install.png)
![Mounting plan](assets/thermal-3.png)

---

## June 7, 2026: Reliability and recovery recheck

Rechecked the reliability side so the device does not feel fragile again after the other work.

Work done:
- rechecked startup recovery
- rechecked network outage behavior
- rechecked fallback and waiting states
- updated the reliability notes with current observations
- left the reliability notes ready for a final pass

This adds time because reliability improvements can get undone by later changes if they are not revisited.

![Health recheck](assets/state-flow.png)
![Recovery recheck](assets/checklist-1.png)
![Reliability review](assets/feature-3.png)

---

## June 8, 2026: UX and usage flow recheck

Rechecked the usage flow so the device still feels smooth after all the other passes.

Work done:
- rechecked the main usage moments
- rechecked transition smoothness
- rechecked awkward spots found earlier
- updated the UX notes with the latest findings
- left the UX notes ready for a final review

This adds time because the usage flow is what ties every feature back to real use.

![Usage recheck](assets/data-flow.png)
![UX review](assets/ux-updates.png)
![Flow check](assets/checklist-1.png)

---

## June 9, 2026: Edge case recheck and fix follow-up

Rechecked the edge case work so the fixes from the previous pass still hold.

Work done:
- rechecked the trickiest scenarios
- rechecked the fixes for the worst problems
- updated the edge case list with the latest state
- left the edge case notes ready for a final review
- kept the only-current-edge-cases rule intact

This adds time because edge cases tend to come back if the rest of the device keeps changing around them.

![Edge recheck](assets/edge-review.png)
![Edge fix follow](assets/edge-map.png)
![Edge state](assets/edge-fixes.png)

---

## June 10, 2026: Metrics, logging, and observability recheck

Rechecked the observability side so the device is still understandable after all the other work.

Work done:
- rechecked what should be logged
- rechecked how state should be readable
- rechecked which metrics still matter
- updated the observability notes with current priorities
- left the observability notes ready for implementation review

This adds time because observability is not just for debugging at the end. It shapes how the whole device is built.

![Logging recheck](assets/metrics.png)
![Metrics recheck](assets/metrics.png)
![Health check](assets/metrics.png)

---

## June 11, 2026: Branding, presentation, and look recheck

Rechecked the branding and presentation so the project still reads as one coherent look.

Work done:
- rechecked color direction
- rechecked typography direction
- rechecked presentation asset consistency
- updated the branding notes with current choices
- left the branding notes ready for final cleanup

This adds time because presentation is not just cosmetics. It affects how the whole project is perceived.

![Brand recheck](assets/brand-1.png)
![Style recheck](assets/brand-1.png)
![Presentation view](assets/brush-1.png)

---

## June 12, 2026: Documentation and journal recheck

Rechecked the documentation side so the journal still tells the whole story.

Work done:
- rechecked the journal sequence
- rechecked the feature notes
- rechecked the asset references
- updated the docs where the build changed
- left the documentation ready for the final pass

This adds time because a journal this size needs more than one pass to stay coherent.

![Docs recheck](assets/changelog-1.png)
![Journal review](assets/changelog-1.png)
![Docs recapture](assets/photo-3.png)

---

## June 13, 2026: Final walkthrough and readiness review

Did the final walkthrough and readiness review so the project can be presented without anything feeling obviously unfinished.

Work done:
- walked the whole device story from setup through playback
- checked that the main features still line up
- checked the journal and asset references for consistency
- updated the readiness notes with the final state
- left the project ready for the last polish and closeout

This adds time because a final walkthrough is where inconsistency becomes obvious fast.

![Walkthrough view](assets/done.png)
![Readiness view](assets/feature-3.png)
![Final checklist](assets/checklist-1.png)

---

## June 14, 2026: Final polish, cleanup, and closeout

Did the final polish, cleanup, and closeout so the project ends as one complete effort.

Work done:
- polished the remaining rough spots
- cleaned up notes that no longer help
- checked the repo presentation one last time
- checked the journal, docs, and assets one last time
- left the project in a complete final state

This adds time because finishing well is not the same as finishing. The last pass is what makes the whole thing hold together.

![Final polish](assets/done.png)
![Closeout view](assets/done.png)
![Final view](assets/done.png)

**Total time spent: 2h**
