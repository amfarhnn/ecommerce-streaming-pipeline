# Figma Animation Templates for Your Pipeline

## Template 1: Event Journey Through Pipeline (Recommended)

### Animation Storyboard
```
Frame 1 (0-0.5s): Event Generated
  - Highlight: Data Source box
  - Action: Pulse animation (scale 1.0 → 1.1 → 1.0)
  - Color: Yellow glow
  
Frame 2 (0.5-1s): Producer Processing
  - Highlight: Producer box
  - Action: Fade in + slide right
  - Connection: Data Source → Producer arrow glows
  
Frame 3 (1-1.8s): Publishing to Kafka
  - Highlight: Redpanda box
  - Action: Scale up from producer
  - Arrow animation: Dashed line animation effect
  - Info: Show "ecommerce-events" topic
  
Frame 4 (1.8-2.5s): Consumer Receiving
  - Highlight: Consumer box
  - Action: Slide left from Redpanda
  - Color: Orange glow
  
Frame 5 (2.5-3.2s): Transformation Pipeline
  - Sequence: Validate → Enrich → Filter
  - Each step: 0.3s duration with fade transition
  - Show intermediate data shape
  - Highlight high_value flag addition
  
Frame 6 (3.2-4s): Database Insertion
  - Highlight: Database section
  - Split action: Data to EVENTS table + PRODUCT_SALES_SUMMARY
  - Show sample row appearing
  - Animation: Slide up into tables
  
Frame 7 (4-4.7s): Analytics Query
  - Highlight: Analytics Engine
  - Show query results appearing
  - Animation: Fade in + counter
  
Frame 8 (4.7-5.5s): CSV Export
  - Highlight: Export outputs
  - Show 3 CSV files appearing
  - Animation: Cascade effect (staggered fade-in)
  
Frame 9 (5.5-6s): Complete
  - All components light up green (success)
  - Arrow glow fades
  - Fade to slightly dimmed view
  - Shows system is ready for next event
```

### Figma Setup Instructions

**Step 1: Create Component Variants**
```
Components to create:
- Event Source (default, active, processing)
- Arrow (static, glowing, animated dashes)
- Database Table (empty, filled, updating)
- Query Result (hidden, visible, populated)
```

**Step 2: Set Up Prototyping**
```
Action: After delay
Transition: Smart animate
Duration: 500ms
Easing: Ease-out
```

**Step 3: Frame-by-Frame Build**
```
Frame 1: Event Generated
  └─ Component: Data Source (active state)
  └─ Arrow to Producer: glow effect

Frame 2: Producer Active
  └─ Component: Producer (active state)
  └─ Show glow around box

Frame 3: To Redpanda
  └─ Component: Redpanda (active state)
  └─ Show queue buffer visual

Frame 4: Consumer Processing
  └─ Component: Consumer (active state)
  └─ Show message received indicator

Frame 5: Transformation A
  └─ Component: Validate step (active)
  └─ Show input data box

Frame 6: Transformation B
  └─ Component: Enrich step (active)
  └─ Show high_value flag being added

Frame 7: Transformation C
  └─ Component: Filter step (active)
  └─ Show output data box

Frame 8: Database Insert
  └─ Component: Database (active)
  └─ Show row appearing in table
  └─ Show product summary updating

Frame 9: Analytics Query
  └─ Component: Analytics (active)
  └─ Show CSV results

Frame 10: Export Complete
  └─ All components light green
```

---

## Template 2: Real-Time Aggregation Animation

### Purpose
Shows how product_sales_summary table updates in real-time

### Keyframes

```
Total Duration: 4 seconds

0s-0.5s: Initial state
  - PRODUCT_SALES_SUMMARY shown with current values
  - Laptop: 2 purchases, $2599.98
  - Smartphone: 4 purchases, $3999.96

0.5s: First purchase arrives
  - Highlight: Laptop row
  - Animation: Row background flash (yellow)
  - Values update:
    Laptop: 2→3 purchases (counter animation)
    Revenue: $2599.98→$3899.97

1.5s: Second purchase arrives
  - Highlight: Smartphone row
  - Animation: Row background flash (yellow)
  - Values update:
    Smartphone: 4→5 purchases
    Revenue: $3999.96→$4999.95

2.5s: Third purchase arrives (different product)
  - Highlight: Monitor row (new row appears)
  - Animation: Row slides in from bottom
  - Values:
    Monitor: 1 purchase, $299.99

3.5s: Aggregate totals update
  - Show total row if included
  - All counters complete
  - Glow effect fades

4s: Loop ready or fade
  - Option A: Loop back to start
  - Option B: Show "Ready for next event"
```

### Figma Implementation

```jsx
// Component Structure
Table
├─ Header Row
│  ├─ Product | Purchases | Revenue
├─ Data Row (Laptop)
│  ├─ "Laptop" | Counter(3) | Currency($3899.97)
├─ Data Row (Smartphone)
│  ├─ "Smartphone" | Counter(5) | Currency($4999.95)
├─ Data Row (Monitor)
│  ├─ "Monitor" | Counter(1) | Currency($299.99)
└─ Total Row (optional)
   ├─ "TOTAL" | Counter(9) | Currency($9199.91)

// Animation Sequence
Frame 1: Initial table
Frame 2: Laptop row highlight + counter animation
Frame 3: Smartphone row highlight + counter animation
Frame 4: Monitor row appears + counter animation
Frame 5: Total row updates
Frame 6: All glow fades
Frame 7: Loop to Frame 1
```

---

## Template 3: Error Retry Visualization

### Purpose
Shows fault tolerance and retry mechanism

### Storyboard

```
Duration: 6 seconds

Frame 1 (0-0.5s): Event at Database
  - Event box positioned at DB insert
  - Arrow shows data flowing
  - All green

Frame 2 (0.5-1s): Error Occurs
  - Database component turns red
  - Event box gets red border
  - Error message appears: "Connection Failed"
  - Sound cue (optional): Error beep

Frame 3 (1-1.5s): Retry Attempt 1
  - Counter shows "Retry 1/3"
  - Event resets/bounces back
  - Color: Yellow (warning)
  - Small animation: arrow reverses then forward again

Frame 4 (1.5-2s): Error Again
  - Database red again
  - Retry message updates
  - Event component pulses red

Frame 5 (2-2.5s): Retry Attempt 2
  - Counter shows "Retry 2/3"
  - Repeat bounce animation
  - Color still yellow

Frame 6 (2.5-3s): Error Third Time
  - Database red (harder/darker)
  - Retry counter critical state

Frame 7 (3-3.5s): Retry Attempt 3 (Final)
  - Counter shows "Retry 3/3"
  - Bounce animation slower/heavier
  - Tension builds...

Frame 8 (3.5-4s): Success!
  - Database turns green
  - Event component turns green
  - Green checkmark overlay
  - Glow effect expands
  - Sound cue: Success ding

Frame 9 (4-4.5s): Data Persisted
  - Show row appearing in table
  - Confirmation message: "Event persisted"

Frame 10 (4.5-6s): Completion
  - All components settle
  - System ready state
  - Optional: Loop back to Frame 1
```

### Figma Setup

```
Components:
├─ Database Box (states: normal, error, success)
├─ Event Box (states: normal, error, warning, success)
├─ Retry Counter (1/3, 2/3, 3/3, complete)
├─ Status Message (hidden, error text, success text)
└─ Checkmark Icon (appears on success)

Interactions:
- Frame → Next frame: Smart animate, 500ms
- Final frame → First frame: Auto-play loop
```

---

## Template 4: Multi-Event Concurrent Processing

### Purpose
Shows pipeline handling multiple events in parallel

### Layout

```
Column 1: Event A (Purchase - Laptop $1999)
Column 2: Event B (Page View - Monitor)
Column 3: Event C (Add to Cart - Keyboard)

Timeline:
0s:     All events spawn
0-1s:   Event A → Producer
0-2s:   Event B → Producer (staggered 0.5s)
0-3s:   Event C → Producer (staggered 1.0s)
1-2s:   Event A → Kafka
1.5-2.5s: Event B → Kafka
2-3s:   Event C → Kafka
2-3s:   Event A → Consumer
2.5-3.5s: Event B → Consumer
3-4s:   Event C → Consumer
3-4s:   Event A → Transform
3.5-4.5s: Event B → Transform
4-5s:   Event C → Transform
4-5s:   Event A → Database
4.5-5.5s: Event B → Database
5-6s:   Event C → Database
6s:     All events complete (glow up)
```

### Figma Components

```
Event Container (for each event)
├─ Event Icon (color-coded: purchase=red, view=blue, cart=green)
├─ Event Data (product name, price)
├─ Progress Indicator (current stage)
└─ Status Badge (processing, complete)

Pipeline Stages
├─ Producer Column
├─ Kafka Column
├─ Consumer Column
├─ Transform Column
├─ Database Column
└─ Export Column

Each event moves through columns with:
- Staggered start times
- Color-coded boxes
- Status updates
- Completion glow
```

---

## Export & Format Specifications

### For README/Documentation

```
Format: GIF (Animated)
Resolution: 1200 x 800px (maintain 16:9)
Frame Rate: 30 FPS (smooth but small file)
Duration: 4-6 seconds
Loop: Infinite
Colors: Use project colors (see color scheme)
File Size Goal: <8MB

Command (using FFmpeg):
ffmpeg -i input.mp4 -vf "fps=30,scale=1200:-1" output.gif
```

### For Presentations (MP4)

```
Format: MP4 (H.264)
Resolution: 1920 x 1280px (16:9)
Frame Rate: 30 FPS
Duration: 4-6 seconds
Codec: libx264 (high quality)
Bitrate: 2500k (good quality)

Command:
ffmpeg -i input.mov -c:v libx264 -preset slow output.mp4
```

### For Web Embedding

```html
<!-- GIF -->
<img src="pipeline-animation.gif" alt="Pipeline Animation" width="100%" />

<!-- Video (better compression) -->
<video width="100%" autoplay muted loop>
  <source src="pipeline-animation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

---

## Figma Export Settings

### Export from Figma Frames

**Method 1: Built-in GIF Exporter**
```
Figma Plugins:
1. Install "Export as PNG/GIF"
2. Select all frames
3. Export as GIF
4. Settings:
   - Frame Rate: 30 FPS
   - Scale: 1x
   - Delay: 0ms between frames
```

**Method 2: Manual Frame Screenshots**
```
Steps:
1. Export each frame as PNG
2. Name them: frame_001.png, frame_002.png, etc.
3. Use ImageMagick or FFmpeg to combine:
   convert -delay 3 -loop 0 frame_*.png animation.gif
```

**Method 3: Record Screen (Loom/Screenflow)**
```
Steps:
1. Open prototype view
2. Record screen
3. Export as MP4
4. Convert to GIF using FFmpeg
5. Optimize with GIF compressor
```

---

## Color & Styling Consistency

### Color Palette (from your diagram)
```
Primary Colors:
- Data Source Yellow: #FFC107
- Producer Green: #81C784
- Kafka Purple: #BA68C8
- Consumer Orange: #FF7043
- Transform Green: #66BB6A
- Database Purple: #CE93D8
- Analytics Blue: #64B5F6

Accent Colors:
- Success Green: #4CAF50
- Error Red: #E53935
- Warning Yellow: #FFEB3B
- Info Blue: #2196F3
- Glow: Semi-transparent white overlay
```

### Text Styling
```
Titles: 24-28px, Bold, Dark Gray
Labels: 12-14px, Regular, Medium Gray
Data: 11-13px, Monospace, Dark Gray
```

---

## Performance Tips

### Animation Optimization
1. **Use component variants** instead of duplicating
2. **Smart animate** automatically handles transitions
3. **Simplify paths** for smoother animations
4. **Use opacity** instead of visibility changes when possible
5. **Limit simultaneous animations** (max 3-4)

### File Size Optimization
```
For GIF:
- Reduce color palette to 256 colors
- Use ImageMagick: magick optimize animation.gif
- Target: 5-8MB for ~5 second animation

For MP4:
- Use libx264 codec
- Bitrate: 1500-3000k
- Target: 10-20MB for ~5 second video
```

---

## Testing Checklist

- [ ] Animation plays smoothly at 30 FPS
- [ ] Colors are accurate to design
- [ ] Text is readable throughout
- [ ] Timing matches storyboard
- [ ] Loop works seamlessly
- [ ] File size is acceptable (<8MB)
- [ ] Works on mobile view
- [ ] No glitches or jumps
- [ ] Sound cues (if used) sync correctly
- [ ] Exported format matches use case

---

**Next Steps:**
1. Choose one template above (Template 1: Event Journey recommended)
2. Import your SVG from Draw.io into Figma
3. Create components for each pipeline stage
4. Build animation frames following the storyboard
5. Test and export
6. Embed in your project documentation

Good luck with your animation! 🎬
