# Conductive Labs MRCC - Guide

**The Essential MIDI Routing Hub for Professional Studios**

![Conductive Labs MRCC](https://github.com/Shadoe-42/music/raw/main/studio/images/conductive_labs/mrcc/front_panel.jpg)
*Conductive Labs MRCC - 11x17 MIDI routing matrix with USB host ports, 5-pin DIN connections, and comprehensive routing control via front panel interface*

---

## What This Unlocks From Your Existing Gear

### **MIDI Controllers & Keyboards:**
- **Vintage synthesizers** - Classic synths with MIDI suddenly become part of unified studio systems
- **MIDI keyboards and controllers** - Any MIDI controller can trigger multiple devices simultaneously
- **Drum machines** - TR-808, TR-909, modern drum machines all sync and route through one hub
- **Digital pianos** - Stage pianos become MIDI controllers for entire studio setups
- **Wind controllers and alternative interfaces** - Breath controllers, guitar-to-MIDI converters integrated seamlessly

### **DAW and Computer Integration:**
- **Any DAW software** - Logic, Ableton, Pro Tools, FL Studio becomes central MIDI command center
- **Multiple computer setups** - Mac + PC workflows with MIDI routing between systems
- **Software synthesizers** - Virtual instruments controlled by hardware without computer switching
- **Laptop performances** - Portable setups with hardware integration for live shows
- **Multi-user studios** - Multiple workstations sharing MIDI device access

### **Hardware Synthesizers & Sound Modules:**
- **Modular synthesizers** - Eurorack systems with MIDI-to-CV modules become part of MIDI networks
- **Rack-mount sound modules** - Vintage Proteus, JV-1000, modern Blofeld units all accessible
- **Grooveboxes** - MPC units, Elektron boxes, Roland MC series in complex routing scenarios
- **Multi-timbral synthesizers** - Access all 16 parts of complex synths through organized routing
- **Vintage gear collections** - Every piece of MIDI-equipped vintage gear becomes instantly accessible

### **Live Performance Equipment:**
- **Stage keyboards** - Multiple keyboards controlling different synths without manual cable swapping
- **Performance controllers** - Breath controllers, ribbon controllers, expression pedals affecting multiple targets
- **Backing track systems** - Computers, samplers, sequencers all synchronized and routed properly
- **Monitor mixing** - MIDI control of digital mixers and monitor systems
- **Lighting and effects** - MIDI-controlled lighting systems, effects processors integrated into performances

### **Studio Infrastructure:**
- **Digital mixing consoles** - MIDI control integration with comprehensive routing
- **Effects processors** - MIDI-controlled effects units accessible from multiple sources
- **Monitoring systems** - MIDI-controlled monitor switching and room correction
- **Recording interfaces** - Multiple MIDI streams to DAW systems without computer bottlenecks
- **Remote control systems** - Studio control rooms with MIDI routing to multiple live rooms

**Discovery moment:** Your entire MIDI-equipped studio becomes one unified instrument where any controller can trigger any sound source, everything stays in sync, and complex routing happens with button presses instead of cable swapping.

---

## Quick Start: Get Your First MIDI Routing in 5 Minutes

**What is MRCC?** A front-panel configurable MIDI router that connects 12 inputs to 17 outputs with no computer required. Features USB host ports for modern devices, traditional 5-pin DIN for vintage gear, and comprehensive filtering and processing options.

### Your First Basic Routing
1. **Connect MIDI controller** → Any input port (USB host ports A-D or 5-pin inputs 1-6)
2. **Connect sound module** → Any output port (5-pin outputs 1-12 or USB PC port)
3. **Press input button** → Input LED lights green
4. **Press output button** → Output LED lights blue (route is made)
5. **Play your controller** → Sound module should respond

**Important:** MRCC routes MIDI data - you still need audio connections for sound!

---

## Essential Parameters (The MIDI Routing Matrix)

### **Input Ports - The MIDI Sources**

#### **5-Pin DIN Inputs (1-6)**
- **What they accept:** Traditional MIDI cables from keyboards, drum machines, sequencers
- **Compatibility:** Any device with standard MIDI OUT or THRU
- **Visual feedback:** Green LED when receiving MIDI data
- **Applications:** Vintage synths, hardware sequencers, traditional MIDI controllers

#### **USB Host Ports (A-D) - Input Side**
- **What they accept:** USB MIDI class-compliant devices (keyboards, controllers, interfaces)
- **Virtual cables:** Each port supports 4 virtual MIDI cables for complex routing
- **Power delivery:** Bus-powered devices work directly (keyboards, small controllers)
- **Visual feedback:** Port LED shows connection status, routing LEDs show activity
- **Applications:** Modern MIDI controllers, USB keyboards, computer interfaces

### **Output Ports - The MIDI Destinations**

#### **5-Pin DIN Outputs (1-12)**
- **What they drive:** Sound modules, synthesizers, effects processors, drum machines
- **MIDI spec compliance:** Standard 5V MIDI output drives long cable runs
- **Multiple destinations:** One input can route to multiple outputs simultaneously
- **Visual feedback:** Blue LED when selected, dimmer blue when routed

#### **USB PC Port - Output Side**
- **What it connects to:** Computer DAW systems for recording and virtual instruments
- **Virtual cables:** 12 virtual MIDI cables for complex DAW routing
- **Bidirectional:** Also functions as input when computer sends MIDI back to hardware

#### **Remote Routing (Y Button)**
- **What it enables:** Extended routing to MRCC Remote-7 or second MRCC unit
- **Connection:** CAT5 cable (NOT Ethernet) up to 50 feet
- **Visual feedback:** Yellow LEDs indicate remote routing destinations

---

## Routing Scenarios

### **Scenario 1: Basic - DAW Controls Hardware Synthesizers**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Computer + DAW  │    │ Conductive Labs  │    │ Hardware Synths │
│                 │    │      MRCC        │    │                 │
│ Logic Pro       │    │                  │    │ Moog Subsequent │
│ Track 1: Bass ○─┼────┼─ USB PC Port     │    │ MIDI In    ◀────┼─ Output 1 ○
│ Track 2: Lead   │    │                  │    │                 │
│ Track 3: Pad    │    │ Route Status:    │    │ Dave Smith Rev2 │
│                 │    │ PC → 1,2,3       │    │ MIDI In    ◀────┼─ Output 2 ○
│ MIDI Tracks ○───┼────┼─ (Virtual cables)│    │                 │
│ (Multi-channel) │    │                  │    │ Roland JV-1000  │
└─────────────────┘    │ LEDs show active │    │ MIDI In    ◀────┼─ Output 3 ○
                       │ routing paths    │    │                 │
                       └──────────────────┘    └─────────────────┘
```

**Connection Details:**
| DAW Track | Virtual Cable | MRCC Route | Hardware Destination |
|-----------|---------------|------------|---------------------|
| **Bass Track** | Cable 1 | PC → Output 1 | **Moog Subsequent** |
| **Lead Track** | Cable 2 | PC → Output 2 | **Dave Smith Rev2** |
| **Pad Track** | Cable 3 | PC → Output 3 | **Roland JV-1000** |

**Main Example:** DAW + MRCC → Multiple hardware synthesizers (professional hardware integration)
**Alternative Options:**
- **Budget:** USB MIDI splitter, MIDI Solutions Quadra Thru
- **Different character:** Expert Sleepers FH-2 for modular integration, iConnectivity mio series
- **Premium:** MOTU MIDI Express XT, Professional studio patch bays

### **Scenario 2: Intermediate - MPC X Controls Hardware Studio**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Akai MPC X      │    │ Conductive Labs  │    │ Hardware Devices│
│                 │    │      MRCC        │    │                 │
│ Multi-channel   │    │                  │    │ Roland TR-909   │
│ MIDI Out   ○────┼────┼─ 5-Pin Input 1   │    │ MIDI In    ◀────┼─ Output 4 ○
│                 │    │                  │    │                 │
│ Tracks 1-16     │    │ Route Matrix:    │    │ Elektron Rytm   │
│ Individual      │    │ In1 → Multiple   │    │ MIDI In    ◀────┼─ Output 5 ○
│ Channel Control │    │ Destinations     │    │                 │
└─────────────────┘    │                  │    │ Moog Minitaur   │
                       │ Clock Sync to    │    │ MIDI In    ◀────┼─ Output 6 ○
                       │ All Devices      │    │                 │
                       └──────────────────┘    └─────────────────┘
```

**Hardware Integration:**
| MPC Channel | MRCC Route | Hardware Device | Musical Function |
|-------------|------------|-----------------|------------------|
| **Ch 9** | Input 1 → Output 6 | **Moog Minitaur** | **Analog bass** |
| **Ch 10** | Input 1 → Output 7 | **Dave Smith OB-6** | **Polyphonic** |
| **Ch 11** | Input 1 → Output 4 | **Roland TR-909** | **Classic drums** |
| **Ch 12** | Input 1 → Output 5 | **Elektron Rytm** | **Modern percussion** |

**Main Example:** MPC X + MRCC → Multiple hardware devices (hardware-centric production)
**Alternative Options:**
- **Budget:** MIDI Solutions T8 splitter, Individual MIDI cables from MPC
- **Different character:** Kenton MIDI Thru-5, Roland UM-ONE mk2 for computer integration
- **Premium:** Studio patch bay system, Professional MIDI matrices

### **Scenario 3: Advanced - Multi-Controller Studio Network**
```
┌─────────────────────────────────────────────────────────────────┐
│                    PROFESSIONAL STUDIO NETWORK                 │
├─ Controllers ──────────┬─ MRCC Hub ──────┬─ Sound Generation ──┤
│                        │                 │                     │
│ Performance Controllers│ Complex Routing │ Synthesizer Rack    │
│ • Keyboards           │ • USB Host A-D  │ • Multi-timbral     │
│ • Expression Pedals    │ • 5-Pin 1-6     │ • Polyphonic        │
│ • Alternative Control  │ • Virtual Cables│ • Drum Machines     │
│                        │ • Filtering     │ • Modular Systems   │
│ Primary Sequencers     │ • Remote Routing│ Recording/Monitoring│
│ • Elektron Octatrack   │ • Activity LEDs │ • Studio Computer   │
│ • Polyend Tracker      │ • Program Change│ • Secondary Systems │
│ • DAW Systems         │ • Clock Sync    │ • Backup Recording  │
└────────────────────────┴─────────────────┴─────────────────────┘
```

**Professional Features:**
- **Any controller can trigger any sound source** with button-press routing changes
- **Master clock distribution** keeps all devices synchronized
- **Filtering prevents conflicts** between different device types
- **Virtual cable routing** enables complex DAW integration
- **Remote extension** provides additional I/O for expanded studios

**Main Example:** Multiple controllers + MRCC → Professional studio network (complex routing matrix)
**Alternative Options:**
- **Budget:** Multiple MIDI splitters, Manual patch bay system
- **Different character:** Software-based routing via computer, Hardware sequencer routing
- **Premium:** Professional studio MIDI matrices, Automated patch bay systems

### **Scenario 4: Expert - Live Performance + Studio Integration**
```
┌─────────────────────────────────────────────────────────────────┐
│                      LIVE + STUDIO WORKFLOW                    │
├─ Stage Setup ──────────┬─ MRCC Control ──┬─ Destinations ──────┤
│                        │                 │                     │
│ Main Performance       │ Real-time       │ Stage Hardware      │
│ • Nord Stage 3         │ • Routing       │ • Moog Sub 37      │
│ • Expression Pedals    │ • Scene Changes │ • Novation Summit   │
│ • Controller Surfaces  │ • Layer Control │ • Roland JD-XA      │
│                        │ • Filter Bypass │                     │
│ Backup Systems         │ Remote Y Button │ Studio Integration  │
│ • Sequencer/Click      │ • FOH Console   │ • Computer DAW      │
│ • Computer/Ableton     │ • Monitor Mix   │ • Recording I/O     │
│ • Emergency Sounds     │ • Control Room  │ • Backup Systems    │
└────────────────────────┴─────────────────┴─────────────────────┘
```

**Live Performance Benefits:**
- **Hardware-based reliability** eliminates computer dependency for live shows
- **Real-time routing changes** enable dynamic performance arrangements
- **Professional failsafe systems** provide backup for critical performances
- **Studio compatibility** - live setup becomes studio setup without reconfiguration

**Main Example:** Live performance rig + MRCC → Studio integration (professional workflow)
**Alternative Options:**
- **Budget:** Software routing via laptop, Individual MIDI cables per performance
- **Different character:** Hardware sequencer as hub, Modular system with MIDI-to-CV
- **Premium:** Complete studio integration systems, Professional touring MIDI rigs

---

## Advanced Techniques

### **Virtual Cable Routing**
Multiple virtual MIDI cables over single USB connection enable complex routing scenarios where different DAW tracks or software instruments can access different hardware devices independently.

### **MIDI Filtering and Processing**
- **Clock filtering:** Prevents tempo conflicts between devices
- **Message type filtering:** Controls which MIDI messages pass through specific routes
- **Channel filtering:** Routes specific MIDI channels to dedicated devices
- **Program Change routing:** Enables scene changes across entire studio

### **Remote Routing Extension**
CAT5 cable connection (up to 50 feet) extends MRCC to additional rooms, stage locations, or rack positions for comprehensive studio and live integration.

---

## Common Use Cases

1. **🎹 DAW Hardware Integration:** Computer controls multiple hardware synthesizers individually
2. **🥁 Hardware Production Hub:** MPC or hardware sequencer controls entire hardware studio
3. **🎵 Multi-Controller Network:** Multiple musicians/controllers access shared hardware resources
4. **🎤 Live Performance Rig:** Stage keyboards control hardware rack with real-time routing
5. **🏠 Studio Infrastructure:** Central MIDI hub for professional studio with multiple rooms
6. **🔄 Vintage Gear Integration:** Classic MIDI equipment becomes part of modern workflows
7. **⚡ Backup and Redundancy:** Professional reliability with multiple routing paths and failsafes
8. **🎛️ Complex Filtering:** Clean MIDI streams and prevent device conflicts in large setups

---

## Pairs Well With

### **MIDI Controllers & Keyboards:**
- **Arturia KeyLab series:** Professional controllers with comprehensive MIDI control
- **Native Instruments Komplete Kontrol:** Advanced integration with software/hardware workflow
- **Novation SL MkIII:** Advanced controller features with MRCC routing capabilities
- **Push 2/Push 3:** Ableton integration with hardware control through MRCC routing

### **Hardware Synthesizers:**
- **Moog synthesizers:** Classic analog sounds with modern MIDI integration
- **Dave Smith/Sequential instruments:** Professional polyphonic synthesis
- **Elektron boxes:** Advanced sequencing and synthesis with MIDI routing
- **Roland System-8/Jupiter-X:** Modern digital synthesis with comprehensive MIDI

### **DAW Integration:**
- **Logic Pro:** Advanced MIDI routing and virtual instrument control
- **Ableton Live:** Performance-oriented workflow with hardware integration
- **Pro Tools:** Professional recording with hardware synthesizer integration
- **Cubase/Nuendo:** Comprehensive MIDI features with external hardware support

### **Studio Infrastructure:**
- **Audio interfaces:** Professional I/O for recording hardware synthesizer audio
- **Digital mixers:** MIDI control integration for comprehensive studio control
- **Monitor controllers:** Studio monitoring with MIDI-controlled switching
- **Patch bays:** Audio signal routing to complement MIDI routing capabilities

---

## Beginner "Gotchas" & Pro Tips

### **⚠️ Common Mistakes:**

**"MIDI vs Audio confusion"**
- **MRCC routes MIDI data only** - you still need audio cables for sound!
- **Solution:** Connect MIDI for control, audio cables for sound to your interface/mixer

**"USB Host vs Device confusion"**
- **Host ports (A-D)** connect to keyboards, controllers (devices that need a computer)
- **Device port (PC)** connects to computers (the computer acts as host)
- **Solution:** Controllers → Host ports, Computers → Device port

**"Virtual cable mysteries"**
- **Each USB connection can carry multiple virtual MIDI cables**
- **DAW tracks can route to different virtual cables for individual hardware control**
- **Solution:** Set up virtual cable routing in your DAW for multi-device control

### **🎵 Pro Tips:**

**MRCC LED Language:**
- **Green LEDs = Active inputs** (receiving MIDI data)
- **Blue LEDs = Selected outputs** (routing destinations)
- **Yellow LEDs = Remote routing** (extended via CAT5 cable)
- **Activity monitoring:** LEDs show real-time MIDI flow for troubleshooting

**Routing Efficiency:**
- **One input can route to multiple outputs** simultaneously
- **Multiple inputs can route to same output** (automatic merging)
- **Route removal:** Press dimly lit output button twice to disconnect

**Professional Workflow:**
- **Label your ports** using MRCC's labeling system for complex studios
- **Use filtering** to prevent MIDI conflicts in large setups
- **Clock source hierarchy:** Establish one master clock source for timing

**Advanced Integration:**
- **Remote Y routing** extends capabilities to additional rooms
- **Program Change routing** enables scene changes across entire studio
- **Backup routing paths** provide professional reliability for critical applications

---

## Why This Device Rocks

### **The Philosophy:**
MRCC proves that **hardware-based MIDI routing** eliminates the complexity and reliability issues of software-based solutions. It's not just a MIDI splitter - it's a complete MIDI infrastructure that makes every MIDI device in your studio instantly accessible from every controller.

### **The Innovation:**
- **Front-panel routing** requires no computer configuration or software
- **USB Host ports** enable modern controllers to work without computers
- **Professional I/O count** handles large studios with comprehensive device collections
- **Visual feedback system** makes complex routing obvious and troubleshoot-friendly
- **Remote extension** provides professional studio infrastructure capabilities

### **The Practical Benefits:**
- **Studio efficiency:** Any controller can access any sound source instantly
- **Live performance reliability:** Hardware-based routing eliminates computer dependency
- **Professional workflows:** Scales from bedroom studios to professional facilities
- **Future-proof design:** Handles vintage 5-pin devices and modern USB simultaneously

### **Perfect For:**
- **DAW users** wanting hardware synthesizer integration without computer bottlenecks
- **Hardware producers** using MPC, Elektron, or other hardware-centric workflows
- **Live performers** needing reliable hardware control without computer dependency
- **Professional studios** requiring comprehensive MIDI infrastructure
- **Vintage gear collectors** integrating classic equipment into modern workflows

### **The Magic:**
MRCC **thinks in MIDI networks** rather than point-to-point connections. It transforms studios from collections of individual devices into unified instruments where creativity flows through routing rather than cable management.

---

## Advanced Learning Path

### **Recommended Study Progression:**
1. **Start with basic routing:** Single controller to single device, understand LED feedback
2. **Add multi-device routing:** One controller triggering multiple devices simultaneously
3. **Explore DAW integration:** Virtual cable routing for professional recording workflows
4. **Master filtering:** Clean up complex MIDI streams, prevent device conflicts
5. **Advanced studio integration:** Multi-controller networks with professional routing
6. **Live performance:** Real-time routing changes and professional reliability systems

### **Skill Development Milestones:**
- **Beginner:** Basic input-to-output routing with visual feedback understanding
- **Intermediate:** Multi-device routing with DAW integration and virtual cables
- **Advanced:** Complex studio networks with filtering, labeling, and professional workflows
- **Expert:** Live performance integration with backup systems and remote routing

### **Professional Applications:**
- **Studio infrastructure:** Central MIDI hub for professional recording facilities
- **Live performance:** Hardware-based reliability for touring and performance
- **Production workflows:** Hardware integration with DAW-based production
- **Educational systems:** Teaching MIDI concepts with hands-on hardware routing

### **Integration Opportunities:**
- **Modular synthesizers:** MIDI-to-CV modules integrate Eurorack systems
- **Vintage collections:** Classic MIDI gear becomes accessible in modern workflows
- **Multi-room studios:** Remote routing enables distributed studio architectures
- **Collaborative music:** Multiple musicians accessing shared hardware resources

---

**Bottom Line:** MRCC isn't just a MIDI router - it's **MIDI infrastructure** that transforms any collection of MIDI devices into a unified creative instrument. Every studio with more than one MIDI device benefits from the routing flexibility and professional reliability that MRCC provides.

---

*Visit [Conductive Labs](https://conductivelabs.com) for complete documentation, firmware updates, and community support*
