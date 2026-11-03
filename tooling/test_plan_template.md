# Test Plan Template

**Status:** Active
**Applies to:** every file in `modular/test_plans/`
**Version:** 1.0, November 2026

---

## Purpose

A guide written before the module is in hand carries ⚠️ markers and a draft status block. A test plan is how those markers are cleared. It turns "untested" into a list of specific checks, each tied to the sentence it can clear, so that clearing a marker is a recorded result and never a feeling.

Test plans are working documents, not guides. They carry no YAML, are not listed in the README, and are not audited as guides. They live in `modular/test_plans/<maker>_<module>_test_plan.md`, one file per module, and they stay in the repository after the tests are done as the record of what was verified, when, and on what firmware.

---

## Two kinds of plan

**Verification plan.** The guide exists and makes predictions. Each test checks one prediction. Use this when a draft guide exists (Oneiroi, Fold 6, Pizza, GTE).

**Discovery plan.** No manual and no guide exist. Each test is a question, and the result becomes the source for the guide. Use this when the maker publishes nothing usable (Kharper). A discovery plan converts to a verification plan once the guide is drafted: the answers become predictions, and the remaining questions stay as discovery rows.

Both kinds share the same header, measurement block, and closing steps. Only the test table differs.

---

## Required structure

### 1. Header

| Field | Value |
|---|---|
| Module | Maker and name |
| Guide | Path of the guide, or "none yet" |
| Plan type | Verification or discovery |
| Firmware | Version, read from the module or its boot indication |
| Tested on | Date or dates |
| Sources | Manual revision, retailer pages, transcripts, with dates |

### 2. Tools

List what each test needs, once: scope and spectrum (Mordax Data), multimeter, tuner, sequencer with 1V/octave output, MIDI source, stereo mixer. A test that needs a tool not listed here is a planning error.

### 3. Measurement block (every plan, run first)

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth, panel back to furthest point, power cable fitted | Tape measure | |
| M2 | Current on +12V, -12V, +5V where present | Multimeter in the supply line | |
| M3 | Power connector polarity marking | Visual and photograph | |
| M4 | Front-panel photograph | Square on, even light, no hands, no cables | |
| M5 | Firmware version | Boot indication, menu, or USB | |

M4 is the image-capture step. A photograph taken here is an `own` image and is recorded in `modular/images/SOURCES.md` if it is added to the repository. A phone shot with a hand or a blanket in frame does not count.

### 4. Test table

**Verification plan columns:**

| ID | Setup | Prediction | Pass criterion | Result | Clears |
|---|---|---|---|---|---|

- **Setup:** the exact cables and knob positions, copied from the guide section under test. If the setup cannot be built from the guide as written, that is itself a failure and is recorded.
- **Prediction:** the guide's own sentence, copied or tightly paraphrased. Never a new claim.
- **Pass criterion:** a number or an observable. "Sounds right" is not a criterion. Use a reading (Hz, cents, volts, mA), a visible state (an LED color, a scope shape), or a yes/no event.
- **Result:** the date and what happened, in a few words. A number where there is one.
- **Clears:** the guide line, section, or draft-block item this test settles.

**Discovery plan columns:**

| ID | Question | How to find out | Result |
|---|---|---|---|

### 5. Test order

State the order and the reason. Measurement block first. Then the tests that other tests depend on (pitch before timbre, clock lock before anything clocked). Then the rest.

### 6. Failure handling

A failed prediction is not an inconvenience. It is the reason the plan exists.

1. Record what the hardware did in the Result column, with the date.
2. Correct the guide text so it describes the hardware. Do not soften the wording and leave the claim standing.
3. If the failure came from the manual, note the disagreement here and in the guide, with the manual revision.
4. A failed test keeps its ⚠️ until the corrected text has been re-tested.

### 7. Closing steps

When every test behind a draft status block's open items has a result:

- [ ] Remove the draft status block from the guide.
- [ ] Remove each ⚠️ the plan cleared, and only those.
- [ ] Update the guide's Key Specifications for any measured value (depth, current), noting that the measurement is the user's own.
- [ ] Commit the guide changes separately from the plan results.
- [ ] Leave the plan in place, marked "Complete" with the date.

---

## Rules

- Predictions come from the guide, never from the tester's memory of how similar modules behave.
- One test, one setup, one result. A test that checks three things is three tests.
- A result without a date is not a result.
- Safety first for anything loud or feedback-prone: start with the mixer low and say so in the setup.
- Do not test two untested modules together. If a test needs a second module, it must be one the guide already treats as verified.
- Photograph or note anything unexpected, even if no test covers it. Surprises become Common Mistakes.
