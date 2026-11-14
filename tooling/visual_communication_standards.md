# Visual Communication Standards

**Quick reference for daily-use patterns + comprehensive framework for systematic visual communication**

---

## **Why Visual Standards Matter**

These standards serve `project_philosophy.md`'s generational teaching obligation. Visual communication must work for users we'll never meet, using technology that doesn't exist yet.

**Not just aesthetics - system integrity:** Clear, consistent visual language enables learning across time. Diagrams that work today must work in 2075 when explaining how people thought about electronic music in the early 21st century.

**Interconnection through visual language:** Every diagram shows how signals connect, how modules integrate, how systems emerge from components - the fundamental interconnectedness that makes music technology comprehensible.

**Why systematic visual standards:** From `framework_overview.md` - maintaining system integrity through disciplined process. Visual consistency is process discipline applied to communication. Arbitrary diagram styles degrade system integrity the same way skipping workflow steps does.

**For framework context:** See `guide_creation_framework.md` for where visual standards integrate with guide requirements.

---

## **🚀 Quick Reference: 5 Essential Patterns**

### **1. GitHub Image Integration (Most Common)**
```markdown
![Device Name](https://github.com/Shadoe-42/music/raw/main/[category]/images/[manufacturer]/[device_name]/front_panel.jpg)
*Device description and key interface elements*

# Examples by category:
![Module Name](https://github.com/Shadoe-42/music/raw/main/modular/images/[manufacturer]/[module_name]/front_panel.jpg)
![Synthesizer Name](https://github.com/Shadoe-42/music/raw/main/synthesizers/images/[manufacturer]/[synth_name]/front_panel.jpg)
![Studio Device](https://github.com/Shadoe-42/music/raw/main/infrastructure/images/[manufacturer]/[device_name]/front_panel.jpg)
```

### **2. Signal Type Labels (Every Guide)**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate
```

**Note:** Emoji color coding (🔴🔵🟡) was the prior standard but was retired April 2026 due to portability concerns. Emoji rendering depends on unicode support and cannot be guaranteed across all environments and future systems. Plain text labels carry the same meaning without any rendering dependency. All new guides use the plain text standard. Existing guides will be updated in a future audit phase.

### **3. Basic ASCII Module Box (Standard Format)**
```
┌─────────────────┐
│   Module Name   │
│                 │
│ Input ◀─────────┼── Signal In
│       ║         │
│ Output ○────────┼── Signal Out
│        ║        │
└────────║────────┘
         ║
   Signal Type
```

### **4. Simple Signal Flow (Left-to-Right)**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

Source → Process → Destination
  │        │        │
  VCO   → Filter → Output
```

### **5. Patch Setup Format (Standard for All Patch Sections)**
```
Source Module         ---[A]---> Destination
Another Source        ---[C]---> Another Destination
Trigger Source        ---[G]---> Gate Input
```

Use fenced code blocks (triple backticks) for all patch Setup sections. Column-align source names to a consistent width within each patch. Inline notes are allowed in parentheses after the destination: `---[A]---> ch1 IN  (normals to all channels)`. This format uses pure ASCII and renders correctly in any monospace environment: terminal, text editor, Vim, GitHub, or otherwise.

### **6. Core ASCII Symbols**
- **○** = Output jack
- **◀** = Input jack
- **──** = Audio cable [A]
- **║** = CV cable [C]
- **┈┈** = Gate cable [G]
- **┼** = Connection point

---

## **📖 Comprehensive Reference**

## **Module Image Integration**

**Note on image caption formatting:** Always add two trailing spaces after the image link to force the caption onto a new line below the image rather than rendering inline beside it.

```markdown
![Module Name](url)  
*Caption text here*
```

### **Image Sourcing Standards**
- **Primary source:** ModularGrid community images
- **Format requirement:** JPEG for universal compatibility
- **Quality standard:** High-resolution front panel images
- **Community acceptance:** ModularGrid sourcing is established practice in modular forums

### **Technical Specifications**
- **File format:** JPEG (.jpg)
- **Resolution target:** ~390px width for module panels (maintains detail while manageable file size)
- **File size limit:** Under 50KB for reasonable loading performance
- **Naming convention:** Use ModularGrid filename or descriptive module name
- **Storage location:** `~/claude/Music/modular/images/[module_name]/`

### **Integration Placement Strategy**

**Option A: Quick Start Integration**
```markdown
## Quick Start: Get Your First Sound in 5 Minutes

![Module Name Front Panel](images/module_name/front_panel.jpg)
*Module Name - Front Panel Reference showing key jacks and controls*

**What is the [Module Name]?** Module description...
```

**Option B: Reference Panel Section**
```markdown
## Module Reference

![Full Module Panel](images/module_name/full_panel.jpg)
*Click image for detailed view*

Signal types: [A]=Audio  [C]=CV  [G]=Gate

**Interface Layout:**
Audio In (bottom left) → Signal processing [A]
CV1 (top) → Primary control modulation [C]
CV2 (middle) → Secondary control modulation [C]
```

**Option C: Combined Approach**
```markdown
![Module Panel](images/module_name/panel.jpg)
*Module front panel reference*

Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─VCO─────┐    ┌─Filter──┐
│ Out ○───┼────┼─▶Audio  │ [A]
│     ║   │    │   ║     │
│ CV  ◀───┼────┼── CV1   │ [C]
│     ║   │    │   ║     │
└─────║───┘    └───║─────┘
```

### **Image Integration Guidelines**

**Educational Enhancement:**
- **Visual verification:** Photos confirm ASCII diagram accuracy
- **Interface familiarization:** Users see actual jack locations and control layout
- **Learning support:** Combine visual + textual + diagrammatic instruction
- **Reference value:** Quick visual confirmation during patching

**Quality Standards:**
- **Interface accuracy:** Images must show clear jack names and control labels
- **Visual clarity:** All important controls must be clearly visible
- **Consistent lighting:** Professional appearance with good contrast
- **Orientation:** Standard front-panel view, properly aligned

**Implementation Protocol:**
1. **Source from ModularGrid:** Use established community resource
2. **Verify image quality:** Ensure clarity and proper resolution
3. **Test integration:** Apply to one guide first, evaluate effectiveness
4. **Systematic application:** Roll out to all guides using workflow checklist
5. **Documentation:** Track image sources and maintain file organization

### **File Organization Standards**

**Multi-Category Directory Structure:**
```
~/claude/Music/
├── modular/
│   └── images/
│       ├── [manufacturer]/
│       │   └── [module_name]/
│       │       ├── front_panel.jpg
│       │       └── detail_shots/ (if needed)
│       └── example_structure/
│           ├── erica_synths/
│           │   └── black_polyvoks_vcf/
│           │       └── front_panel.jpg
│           └── expert_sleepers/
│               └── disting_mk4/
│                   ├── front_panel.jpg
│                   └── algorithm_display.jpg
├── synthesizers/
│   └── images/
│       └── [manufacturer]/
│           └── [instrument_name]/
│               ├── front_panel.jpg
│               └── detail_shots/ (if needed)
│       └── example_structure/
│           ├── sequential/
│           │   └── take_5/
│           │       └── front_panel.jpg
│           └── moog/
│               └── subsequent_37/
│                   └── front_panel.jpg
├── infrastructure/
│   └── images/
│       └── [manufacturer]/
│           └── [device_name]/
│               └── front_panel.jpg
└── [other_categories]/
    └── images/
        └── [manufacturer]/
            └── [device_name]/
```

### **GitHub Repository Integration**

**For GitHub repositories, use GitHub raw URL format:**
```markdown
![Module Name](https://github.com/Shadoe-42/music/raw/main/modular/images/[module_name]/front_panel.jpg)
*Module description and key interface elements*
```

**GitHub Raw URL Structure:**
- **Base:** `https://github.com/{username}/{repository}/raw/{branch}/`
- **Category-specific paths:**
  - **Modular:** `modular/images/[manufacturer]/[module_name]/front_panel.jpg`
  - **Synthesizers:** `synthesizers/images/[manufacturer]/[instrument_name]/front_panel.jpg` 
  - **Studio gear:** `infrastructure/images/[manufacturer]/[device_name]/front_panel.jpg`
- **Complete examples:**
  - `https://github.com/Shadoe-42/music/raw/main/modular/images/erica_synths/black_polyvoks_vcf/front_panel.jpg`
  - `https://github.com/Shadoe-42/music/raw/main/synthesizers/images/sequential/take_5/front_panel.jpg`

**Implementation Examples:**

**Modular Gear:**
```markdown
![Erica Synths Black Polyvoks VCF](https://github.com/Shadoe-42/music/raw/main/modular/images/erica_synths/black_polyvoks_vcf/front_panel.jpg)
*Erica Synths Black Polyvoks VCF - Front panel showing CV1, CV2, Audio In, and Filter Out*

![4ms MetaModule](https://github.com/Shadoe-42/music/raw/main/modular/images/4ms/metamodule/front_panel.jpg)
*4ms MetaModule - Main unit with core functionality*

![Expert Sleepers Disting mk4](https://github.com/Shadoe-42/music/raw/main/modular/images/expert_sleepers/disting_mk4/front_panel.jpg)
*Expert Sleepers Disting mk4 - Multi-algorithm digital processor*
```

**Complete Synthesizers:**
```markdown
![Sequential Take 5](https://github.com/Shadoe-42/music/raw/main/synthesizers/images/sequential/take_5/front_panel.jpg)
*Sequential Take 5 - 5-voice analog polysynth with Prophet-5 heritage*

![Moog Subsequent 37](https://github.com/Shadoe-42/music/raw/main/synthesizers/images/moog/subsequent_37/front_panel.jpg)
*Moog Subsequent 37 - Paraphonic analog synthesizer with classic Moog filter*
```

**Studio Equipment:**
```markdown
![Focusrite Scarlett 2i2](https://github.com/Shadoe-42/music/raw/main/infrastructure/images/focusrite/scarlett_2i2/front_panel.jpg)
*Focusrite Scarlett 2i2 - USB audio interface with two inputs*
```

### **Integration with Existing Standards**
- **Signal type labels:** Images work alongside [A][C][G] signal identification
- **ASCII diagrams:** Photos verify diagram accuracy and provide visual context
- **Enhanced format:** Images support budget/premium alternative visualization
- **Learning progression:** Visual complexity can match skill development levels

---

## **ASCII Symbol Library**

### **Core Symbols**
- **Output jack:** `○` (circle)
- **Input jack:** `◀` (left arrow)  
- **Module boundary:** `┌┐└┘` (box drawing characters)
- **Audio cable:** `──` (double dash, represents red cables)
- **CV cable:** `║` (double line, represents blue cables)
- **Gate/Trigger cable:** `┈┈` (dotted line, represents yellow cables)
- **Connection point:** `┼` (cross)
- **Signal flow direction:** `→` `←` `↑` `↓` (arrows)

### **Advanced Symbols**
- **Multiple output:** `○○○` (multiple circles)
- **Normalized connection:** `(○)` (parentheses around jack)
- **Optional connection:** `[○]` (brackets around jack)
- **Variable control:** `∼` (tilde for modulation)
- **Attention/Important:** `⚠` (warning symbol)

---

## **Signal Type Hierarchy**

### **Signal Type Labeling Standard**

**Label format:** `[A]` = Audio, `[C]` = CV, `[G]` = Gate

Plain text labels carry the signal type meaning without any unicode or rendering dependency. This ensures diagrams remain readable in any environment; terminal, text editor, plain text viewer, or future systems.

**Audio signals [A]:** Primary signal path
**CV signals [C]:** Control voltage
**Gate/Trigger signals [G]:** Timing and logic

### **Signal Labels Inline**
Always label signal types on connections. Two formats depending on diagram style:

**Linear flow format:**
```
Source ---[A]---> Destination     (audio signal)
Source ---[C]---> Destination     (CV signal)
Source ---[G]---> Destination     (gate/trigger)
```

**Box diagram format (confirmed standard for multi-module patch diagrams):**
```
│ Source OUT ○──┼─[A]─┼─▶ Destination IN                │
│ Source OUT ○──┼─[C]─┼─▶ Destination CV                │
│ Source OUT ○──┼─[G]─┼─▶ Destination Gate              │
```

For cross-box connections (output leaving a module box to an external destination):
```
│            Destination IN ○──[A]──▶ External In
│            Destination CV ○──[C]──▶ External CV
```

The label sits on the connection line itself; not at the endpoint; so the signal type is readable while tracing the connection, before arriving at the destination.

### **Recommended Signal Flow Format**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─ VCO ──────────┐    ┌─ Filter ────────┐
│ Out ○──┼─[A]─┼─▶ Audio In            │
│                │                     │
│ CV  ◀──┼─[C]─┼── CV1                 │
└────────────────┘                     │
                    Audio Out ○──[A]──▶ Output
                    └────────────────────┘
```

---

## **Module Representation Standards**

### **Standard Module Box Format**
```
┌─────────────────┐
│   Module Name   │
│                 │
│ Input1 ◀────────┼── Signal In
│        ║        │
│ Output ○────────┼── Signal Out
│        ║        │
└────────║────────┘
         ║
    Signal Type
```

### **Multi-Function Module Format**
```
┌─────────────────┐
│   Disting mk4   │
│ (Algorithm:     │
│  Quantizer)     │
│                 │
│ A Input ◀───────┼── CV In
│         ║       │
│ X Output ○──────┼── Quantized CV
│          ║      │
└──────────║──────┘
           ║
     CV (Blue)
```

### **Utility Module Format**
```
┌─────────────────┐
│ Function        │
│ Junction        │
│ (CV Processor)  │
│                 │
│ A In ◀──────────┼── CV Input
│      ║          │
│ Sum Out ○───────┼── Processed CV
│         ║       │
└─────────║───────┘
          ║
    CV (Blue)
```

---

## **Signal Flow Guidelines**

### **Left-to-Right Progression**
Always show signal flow from left (source) to right (destination):
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

Source → Process → Destination
  │        │        │
  VCO   → Filter → Output
```

### **Multi-Stage Processing**
For complex patches, use clear horizontal progression:
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─VCO─┐    ┌─Filter─┐    ┌─VCA─┐    ┌─Output─┐
│     ○────┼─ Audio ◀────┼─ Out ○───┼─ Mix   │ [A]
│     ║    │        ║    │     ║    │        │
└─────║────┘        ║    └─────║────┘        │
      ║             ║          ║             │
  [C] 1V/Oct   [C] CV Input  [C] Env Input  [A] Audio Out
```

### **Feedback Loops**
Show feedback clearly with return paths:
```
Signal types: [A]=Audio  [C]=CV

┌─VCO─┐    ┌─Filter─┐
│ Out ○────┼─ Audio ◀─┐ [A]
│     ║    │        ║ │
│ FM  ◀────┼─ CV Out ○─┘ [C]
│     ║    │        ║
└─────║────┘        ║
      ║        [C] Feedback
   [C] 1V/Oct
```

### **Patch Setup Diagram Format**

Two formats are in use. Choose based on diagram purpose.

**Format 1: Fenced Code Block (standard for all patch Setup sections)**

Use for the connection list in every patch example Setup section. Pure ASCII, renders correctly in any monospace environment (terminal, Vim, Sublime, GitHub). Column-align source names within each patch.

```
Oscillator OUT        ---[A]---> Filter IN
Envelope OUT          ---[C]---> Filter CV
Gate OUT              ---[G]---> Envelope GATE
Filter OUT            ---[A]---> VCA IN
```

Arrow convention: `---[A]--->` for audio, `---[C]--->` for CV, `---[G]--->` for gate/trigger. Inline clarifying notes in parentheses after the destination are permitted when needed:

```
Oscillator OUT        ---[A]---> Ceres ch1 IN  (normals to all channels)
Envelope OUT          ---[C]---> ch1 CV
LFO (triangle) OUT    ---[C]---> ch2 CV
LFO (square) OUT      ---[C]---> ch3 CV
Ceres ch6 MIX OUT     ---[A]---> Mixer
```

**Format 2: Bordered Box (reserved for complex multi-output architecture diagrams)**

Use when illustrating module architecture, multi-module signal chains, or feedback paths where the spatial relationships between inputs and outputs matter. These diagrams use Unicode box-drawing characters and are appropriate for the Architecture sections of complex guides. Do not use this format for patch Setup connection lists.

```
┌─VCO─────┐    ┌─Filter──┐
│ Out ○───┼────┼─▶Audio  │ [A]
│ CV  ◀───┼────┼── CV1   │ [C]
└─────────┘    └─────────┘
```

**Rule:** Patch Setup sections always use Format 1. Architecture and overview diagrams use Format 2 where warranted.

---

## **Patch Complexity Visualization**

### **Difficulty Indicators**

**Beginner (Basic):**
```
Simple: A → B → C
Source → Process → Output
```

**Intermediate:**
```
Moderate: A → B ← C
          ↓   ↑
          D → E
```

**Advanced:**
```
Complex:  A → B ← C
          ↓   ↑   ↓
          D → E → F
          ↑       ↓
          H ← G ←─┘
```

**Expert:**
```
Very Complex: Multiple interconnected modules with feedback loops,
              cross-modulation, and multi-function integration
```

### **Learning Progression Map**
```
Basic → Intermediate → Advanced → Expert
  │         │            │         │
  │    ┌────┴────┐       │         │
  │    │         │       │         │
  ▼    ▼         ▼       ▼         ▼
Tone  Mod      Sync   Complex   Multi-
      │         │      Routing  Module
      │         │        │      Systems
      └─────────┼────────┘
                │
         Performance
         Applications
```

---

## **Module Alternative Visualization**

### **Enhanced Format Integration**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

Main Example: Maths Ch1 → Filter CV1
     │
     ├─Budget: ┌─2HP LFO─┐ 
     │         │ LFO1 ○──┼─→ Filter CV1
     │         └─────────┘   [C] CV
     │
     ├─Different: ┌─Batumi──┐ 
     │            │ Phase ○─┼─→ Filter CV1
     │            └─────────┘   [C] CV
     │
     └─Premium: ┌─Quadrax─┐ 
                │ Ch1 ○───┼─→ Filter CV1
                └─────────┘   [C] CV
```

### **Alternative Ecosystem View**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─────────────────────────────────────────────────┐
│              Alternative Ecosystem               │
│                                                 │
│ Budget    │ Main      │ Different  │ Premium    │
│ Tier      │ Example   │ Character  │ Tier       │
│           │           │            │            │
│ 2HP LFO   │   Maths   │  Batumi    │  Quadrax   │
│ Doepfer   │  Function │  Geometric │  Complex   │
│ A-143-3   │ Generator │   Phases   │ Functions  │
│           │           │            │            │
│ $40-80    │ $300-350  │ $250-300   │ $400-450   │
└─────────────────────────────────────────────────┘
```

---

## **System Integration Visualization**

### **Complete Signal Chain Context**
```
┌─Sequencer─┐  ┌─VCO─────┐  ┌─Filter──┐  ┌─VCA─┐  ┌─Output─┐
│ Gate ○────┼──┼─▶Gate   │  │         │  │     │  │       │
│      ║    │  │  ║      │  │ Audio◀──┼──┼─○Out│  │ ◀─────│
│ CV ○──────┼──┼─▶1V/Oct │  │      ║  │  │  ║  │  │   ║   │
│      ║    │  │  ║      │  │ CV1◀────┼──┼──┘  │  │   ║   │
└──────║────┘  └──║──────┘  └─────║───┘  └─────┘  └───║───┘
       ║          ║               ║                   ║
   CV (Blue)  Audio (Red)    CV (Blue)           Audio (Red)
```

### **Multi-Module Ecosystem**
```
┌─────────────────────────────────────────────────────────────┐
│           Complete Synthesis Ecosystem (26HP)               │
│                                                             │
│ ┌─Function─┐ ┌─Bloom──┐ ┌─Disting─┐ ┌─Polyvoks─┐           │
│ │Junction  │ │Generativ│ │mk4     │ │Filter   │           │
│ │(CV Proc) │ │e       │ │(Algo)  │ │(Acid)   │           │
│ │          │ │        │ │        │ │         │           │
│ │ Sum ○────┼─┼─CV1 ◀──┼─┼─X Out ○┼─┼─CV1 ◀───┼─── Mathematical Control │
│ │     ║    │ │    ║   │ │      ║ │ │     ║   │           │
│ │ A ◀──────┼─┼─Gate1  │ │ Y Out ○┼─┼─CV2 ◀───┼─── Generative Control   │
│ │     ║    │ │    ║   │ │      ║ │ │     ║   │           │
│ └─────║────┘ └────║───┘ └──────║─┘ └─────║───┘           │
│       ║          ║             ║         ║               │
│   CV (Blue)  CV (Blue)    CV (Blue)  Audio (Red)         │
│                                                           │
│ Mathematical + Generative + Algorithmic → Legendary Acid │
└─────────────────────────────────────────────────────────────┘
```

---

## **Performance and Real-Time Control**

### **Live Control Indicators**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─Controller─┐    ┌─Module─┐
│ Knob   ∼───┼────┼─▶CV In │  ∼ = Real-time control [C]
│        ║   │    │   ║   │
│ Slider ∼───┼────┼─▶Mod  │  Manual performance control [C]
│        ║   │    │   ║   │
└────────║───┘    └───║───┘
         ║            ║
    [C] Performance   [C] Module Response
```

### **Touch/Manual Control**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─Module─────┐
│ Touch   [T]│  [T] = Touch/tactile control
│ Pad     ║  │
│         ▼  │  Direct physical interaction
│ CV Out  ○──┼─→ Performance CV [C]
│         ║  │
└─────────║──┘
          ║
   [C] Performance CV
```

---

## **Implementation Guidelines**

### **1. Consistency Requirements**
- **Same symbols throughout guide:** Never mix symbol systems within a guide
- **Consistent spacing:** Maintain uniform spacing in all diagrams
- **Signal labeling:** Always label signal types (Audio/CV/Gate)
- **Module naming:** Use exact manufacturer terminology

### **2. Readability Standards**
- **Maximum width:** Keep diagrams under 80 characters for readability
- **Vertical alignment:** Align modules and connections cleanly
- **White space:** Use adequate spacing between elements
- **Visual hierarchy:** Most important signals should be most prominent

### **3. Educational Progression**
- **Start simple:** Basic patches use minimal visual complexity
- **Add complexity gradually:** Each patch level adds visual elements
- **Maintain clarity:** Never sacrifice understanding for visual appeal
- **Guide learning:** Visual complexity should match conceptual complexity

### **4. Integration Requirements**
- **Enhanced format compliance:** All visual elements must include specific alternatives
- **Cross-reference capability:** Diagrams should connect to other guide concepts
- **Framework adherence:** Follow all established quality and efficiency standards
- **Systematic application:** Standards must be replicable across all guides

---

## **Quality Verification**

### **Visual Standards Checklist**
- [ ] **Symbol consistency:** All symbols from approved library
- [ ] **Signal hierarchy:** Audio/CV/Gate properly differentiated
- [ ] **Module accuracy:** Real jack names and interface elements
- [ ] **Flow clarity:** Left-to-right signal progression
- [ ] **Alternative integration:** Budget/premium options visually clear
- [ ] **Complexity appropriate:** Visual complexity matches skill level
- [ ] **Educational value:** Diagrams enhance rather than confuse understanding

### **Before/After Comparison Protocol**
When implementing visual standards:
1. **Document current state:** Screenshot or copy existing visual approach
2. **Apply standards systematically:** Use this framework consistently
3. **Compare effectiveness:** Evaluate clarity improvement
4. **Document lessons learned:** Update standards based on implementation experience
5. **Replicate successful patterns:** Apply proven improvements to other guides

---

## **Cross-Reference Integration**

### **Framework Integration**
- **Quality System:** Visual standards are part of overall quality verification
- **Guide Creation Framework:** Visual requirements integrated into content standards
- **Accountability Tracking:** Track time spent on visual implementation vs improvement
- **Failure Patterns:** Document visual communication failures and prevention

### **Implementation Process**
1. **Apply visual standards** using this framework
2. **Follow workflow checklist** for all visual implementation operations
3. **Track efficiency** of visual improvements vs. content clarity gains
4. **Document successes** in quality system for replication
5. **Update standards** based on real-world application experience

---

**This framework provides systematic visual communication standards for immediate implementation and long-term consistency across all modular synthesizer guides.**

---

*Integrates with: `guide_creation_framework.md`, `quality_system.md`, `workflow_checklist.md`, and all other tooling directory systems.*