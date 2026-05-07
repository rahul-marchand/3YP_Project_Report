# Rahul-led Logbook Entries

## MT VAC - Rahul

V.1 New prototype concept agreed and workstreams allocated for Hilary.

**Current project vision:** A low-cost, oculomotor-based, objective mTBI screening tool focused on grassroots youth sport. We measure pupillary light reflex and smooth pursuit under controlled head-to-camera geometry, packaged into a single hardware unit so that parents, coaches and teachers can deploy it pitchside without trained personnel. Following the week 8 post-mortem, vergence has been deprioritised: it depended on a binocular setup that the new single-phone topology cannot easily support, and we would rather concentrate our remaining bandwidth on the two biomarkers we can measure well.

**Goals:** Convene a single consolidation meeting over the vacation to firm up what the new prototype actually is – the headset architecture, the optical path, the illumination path, and the software topology – and to allocate Hilary workstreams against that design so each of us can begin in week 1 without further blocking discussions.

**Meeting report:** Building on the week 8 conclusion that the two-phone Cardboard setup was unviable, the meeting opened with sketching the replacement. The agreed concept is a single-phone, head-mounted unit: the phone sits in front of the user with its rear camera looking through a beamsplitter that folds the eye image off-axis into the sensor, while the phone screen continues straight through the splitter to present the stimulus. Illumination is moved off the phone entirely and into dedicated LEDs inside the housing, run from their own driver so that intensity and wavelength are known and stable rather than inheriting whatever the phone screen happens to do. We discussed wavelength briefly and agreed NIR is the right direction (invisible to the user, decouples imaging from the visible stimulus path), but left the exact selection to the optics and electronics workstreams to converge on against the camera response curve.

With the architecture settled, we mapped out the four workstreams it implies and assigned owners. Victor takes optics: beamsplitter type and geometry, lens path to bring the eye into focus given the phone camera's minimum focus distance, and focal length characterisation. Eesh takes electronics: LED driver, illumination control, power budget. Rahul takes ML for PLR: data collection pipeline, model architecture for pupil diameter, and the labelling strategy to back it. Suleiman takes the smooth pursuit software path and runs a parallel investigation into on-device inference engines, since we agreed early that patient video cannot leave the device for either latency or regulatory reasons.

We also flagged the two cross-cutting items that none of the four workstreams owns by default but which everyone needs: a system-level requirements document deriving frame rate, illumination, resolution and timing constraints from the biomarker physics, and a CAD envelope inside which all the hardware lives. We assigned the requirements document to Eesh as a week 1 deliverable; CAD will sit unowned for now and be picked up by whoever finds themselves the natural integrator once the workstreams have run for a couple of weeks.

**Targets for HT week 1:** Each owner to scope their workstream and produce a first-pass plan. Eesh to additionally produce the system requirements document so that the optical, electronic and software workstreams have shared targets to design against from week 2 onwards.

---

## HT Week 1 - Rahul

1.1 First meeting back. Workstream kickoffs around the new single-phone architecture, and a check-in on team capacity.

**Current project vision:** Single-phone, headset-mounted, oculomotor screening tool measuring PLR and smooth pursuit. The hardware unit houses the optics, illumination and IMU; the phone provides the camera, stimulus display and on-device ML inference. The market wedge remains youth grassroots sport, where the gap between clinic-grade and pitchside-viable tools is widest.

**Goals:** Get each of the four workstreams (system requirements, optics, illumination/electronics, ML, inference engine) properly scoped. Establish what a "first-pass plan" looks like for each so that the team reconvenes in week 2 with comparable artefacts.

**Meeting report:** Eesh opened with system requirements. Working back from the biomarker physics: PLR needs at minimum 30 fps capture (preferably 60) under controlled NIR illumination, with stable pupil contrast across iris colour and ambient conditions; smooth pursuit needs accurate gaze tracking on the same camera path. Eesh tabled a draft requirements sheet and committed to refining it next week into something the optical and electronic workstreams can design against. Victor reported on lens and focal length testing for the beamsplitter path, having ordered a small set of candidate lenses to characterise on the bench. Suleiman started splitting his time between scoping the smooth pursuit software (stimulus design, gaze tracking approach) and surveying inference engines, with the expected shortlist of TensorFlow Lite, Core ML and ONNX Runtime mobile, and noted that the engine choice will likely be downstream of whichever model architecture Rahul converges on.

Rahul had a tough week and made limited forward progress on the ML workstream, and committed to spending week 2 catching up so that the data collection pipeline and a candidate model are on the table before mid-term. The team agreed that the dependency chain – model architecture choice feeds into Suleiman's inference engine selection, which feeds into Eesh's compute requirements – means the ML workstream needs to move first, and that unblocking it is the highest priority going into week 2.

**Targets for next week:** Eesh to firm up the system requirements document. Victor to continue lens characterisation. Suleiman to continue the inference engine survey and begin scoping the EEM go-to-market work in parallel. Rahul to produce a data collection plan and a first model architecture.

---

## HT Week 2 - Rahul

2.1 ML for PLR architecture decision, camera workstream kickoff, continued optics testing.

**Current project vision:** Unchanged. Single-phone headset for PLR and smooth pursuit, youth grassroots sport.

**Goals:** Get the ML workstream out of the blocker position it sat in last week, give Eesh a concrete camera path to start specifying, and have Victor's optics work move from candidate-list to a shortlisted geometry.

**Meeting report:** Rahul opened with the ML for PLR plan. Two architectural options were on the table: (a) a segmentation network producing a pupil mask from which diameter is geometrically derived, or (b) a regression head producing pupil diameter directly from the cropped eye region. Option (a) is interpretable but expensive at inference time and brittle under glare and partial occlusion (eyelid, eyelashes). Option (b) is faster, more robust under noise, and can be trained end-to-end against ground truth captured from a higher-fidelity reference setup. The team agreed to pursue (b) with a MobileNet-class backbone, on the understanding that interpretability can be partially recovered via saliency analysis if the regulatory pathway demands it. Data collection is the next major unblock, and Rahul sketched a pipeline using a benchtop reference camera plus controlled LED stimulus to generate paired (eye image, pupil diameter) data.

Eesh moved onto the camera workstream, working from the PLR requirements: NIR-sensitive sensor, ability to lock exposure and disable auto-white-balance, and a frame rate that does not collapse under low-light NIR conditions. He started enumerating which of the candidate phones in the youth-accessible price range actually expose this level of camera control through their APIs, since this materially constrains the addressable hardware.

Victor continued lens testing and reported initial focal length findings; the candidate lens set is narrowing. Suleiman continued on the inference engine survey and began the smooth pursuit software in earnest – stimulus design (target trajectory, speed, contrast), gaze tracking approach, and how the smooth pursuit data would flow through whichever inference engine the team settled on. He also began background reading on EEM GTM strategy in parallel.

**Targets for next week:** Rahul to begin the data collection setup and produce an initial baseline model on a small dataset. Eesh to finalise the camera shortlist. Victor to converge on a beamsplitter geometry. Suleiman to make a recommendation on the inference engine.

---

## HT Week 3 - Rahul

3.1 Mid-term progress presentation followed by debrief and the next round of allocations.

**Presentation feedback:** This was an interim progress update rather than a full design review, so the panel focused on the depth of each individual workstream rather than the overall product pitch. Each member received targeted feedback on their own strand. The feedback on the PLR ML strand clustered around three points: the choice of pupil diameter regression over segmentation had not been adequately justified beyond inference cost (the panel wanted a written-up comparison with citations to the existing smartphone pupillometry literature); the data collection plan needed a clearer story on labelling, particularly subject diversity (iris colour, ambient lighting) which the literature flags as failure modes for phone-camera pupillometry; and the eventual ML output needed a well-defined interface so that downstream processing layers had something stable to consume. The smooth pursuit strand drew similar push-back on stimulus parameter choices and on whether the gaze tracking accuracy budget was achievable on the chosen camera path. The optics and electronics strands drew analogous depth questions. The cross-cutting takeaway across all four was the same: each workstream had progressed in isolation but the seams between them were under-defined.

**Current project vision:** Unchanged at the product level. The internal architecture is now firming up: dichroic beamsplitter optics path (Victor pivoting from a standard beamsplitter this week), NIR illumination from dedicated LEDs (Eesh next week), pupil diameter regression model for PLR (Rahul), gaze tracking and post-processing for smooth pursuit (Suleiman), and a shared on-device inference engine running both models (Suleiman).

**Meeting report:** The debrief converged on the same diagnosis the panel had given: each workstream had advanced on its own terms but the seams between them were under-defined. We walked through the seams one at a time and assigned each to whoever was best placed to close it. On the smooth pursuit side, Suleiman picks up the filter and confidence signal layer that turns the raw gaze track into a clinically interpretable output – this is the join where noisy per-frame predictions become a measurement, and was the strand the panel pushed hardest on. The illumination-to-optics seam goes to Eesh, who starts on the LED and driver design from the NIR specifications already in the requirements document, with eye safety as the binding constraint given the user population. The optics-to-camera seam is being addressed by Victor's pivot from a standard beamsplitter to a dichroic one, on the basis that the dichroic separation of NIR (eye imaging) from visible (stimulus path) is cleaner and cheaper in optical-budget terms than the polarising alternative. The hardware integration seam – getting the optical path, LED placement, IMU position and phone interface all to live inside one printable enclosure – is picked up by Rahul as a CAD workstream, which gives the other three something concrete to design against and runs in parallel with the PLR ML data collection pipeline now that the latter has a plan.

Alongside the engineering work, the EEM strand is being kept active in parallel: Victor on the value proposition and PMF write-up plus early outreach to schools and parents, Suleiman scoping GTM. The intent is to avoid another week 4-style imbalance where the engineering and commercial sides drift out of step.

**Targets for next week:** Suleiman to make progress on the filter and continue scoping the EEM GTM strand. Eesh on illumination design with safety leading. Victor to clear up the value proposition and PMF write-up alongside the dichroic optics work, and to start outreach to schools and parents for early demand signal. Rahul to produce a first CAD pass with the headset envelope, optical path placeholder, phone mount and rough LED positions.
