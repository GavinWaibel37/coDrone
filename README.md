CoDrone Questions + Answers:

## Lesson 1: ##
- What was the battery percentage on your first run?
  * The battery was at 96%; I charged it before starting.
- What happens if you remove the hover() line, and why?
  * The drone will lift off, then automatically land.
- What did you change in section 6, and what did the drone do?
  * I changed how long it hovered and the drone go more unsteady as time went on.

## Lesson 2: ##
- Your measurement table from step 1 — asked for, measured, difference, across three runs.
   * 1: 81, R, 45, L, 72, R, 69 (Measurements of the course... drone overshot a lot)
   * 2: 71, R, 39, L, 65, R, 50 (Decreased based on prior run... drone undershot the finish and was still way to the left)
   * 3: 65, R, 24, L, 60, R, 52 (Almost perfect. Ended slightly to the left)
- What you expected from the two turn_degree(90) calls in step 2, and what really happened.
   * I expected it to turn 90 degrees each time. It actually did nothing.
- Your course sketch with the leg lengths, and how close the drone stayed to it.
   * The drone strayed a couple of inches off the line every time. The result was fairly consistent, though.

## Lesson 3: ##
- What RGB numbers did you use for the color you invented, and what does it look like?
   * The color was whitish: RGB(100, 100, 100, 100)
- What does time.sleep() do, and what happens to your color sequence without it?
   * Time.sleep() is a delay. If it's not included, it will go through the color sequence so fast you won't notice it.
- Which stages of your flight got which color in section 5?
   * Cyan started, Purple in flight, green for landing, all accompanied by beeps
