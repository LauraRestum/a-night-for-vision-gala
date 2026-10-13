# A Night For Vision: Gala Guest Portal

Guest-facing companion site for the 2026 Envision Gala (Saturday, October 24th, 2026, Wichita Art Museum).
Static site: one `index.html`, plus `audio/` (ElevenLabs narration, MP3), `img/` (photos cropped from the Through My Eyes banners), and `docs/` (large print program PDF, tagged, linked from the Program page). No build step.

## How the page is organized
- Everything lives in `index.html`: styles at the top, markup in the middle, one script at the bottom.
- Views are sections with `data-view` (home, welcome, map, stories, story, program, watch, give). Navigation uses bare hash links (`#map`, `#story3`).
- Editable content sits at the top of the script:
  - `SPOTS`: map locations (Rotunda, Beren Room, Great Hall, Upper Gallery, Bottom of the Stairs), each with `what`, `when`, `directions`, and optional `audio`.
  - `STORIES`: Through My Eyes stories. Each has `name`, `hook` (banner title), `text` (paragraphs separated by blank lines; on-screen text must match the recording word for word), `audio`, `images` (with alt text), `looks` (visual description of the person) and `looksAudio`, and optional `note`.
  - `VIDEOS`: the five gala videos; `ad` holds the audio-described link when available.
  - `PAGE_AUDIO`: recordings for page-level Listen buttons (welcome, menu, evening, fundaneed, aruba).
  - `GIVE_URL`: the GiveSmart giving page.

## Rules to keep (accessibility and brand)
- WCAG 2.2 AA. Test with axe and a real screen reader (VoiceOver, TalkBack) after changes.
- Sound never starts on its own; only after a tap. Do not add spoken "Playing" announcements (they talk over the audio).
- Tapping a name in Through My Eyes waits about 1.4 seconds, plays the description, then the story, so VoiceOver can read the heading first.
- On-screen text must match each recording exactly (for guests who are deaf or hard of hearing).
- No grey type, no text smaller than 16px, keep the A minus and A plus text-size buttons working up to 200%.
- Population language: "people who are blind or have low vision." Never "visually impaired" in our own copy (participant quotes stay as printed).
- No em dashes. Dates use ordinals (October 24th). Montserrat (with Gotham fallback) only.
- Paid vendors are credited with "by," never "courtesy of."
- Donor-facing names: Bicknell Envision Vision Rehabilitation Center, Gigi & Carl Allen Envision Research Institute, Cathy G. Hudson Envision Child Development Center.

## Open items
- Audio-described video links for the Watch page (Adah is in; four to go: Program Legacy, Water Street, Heather's Camp, Level Up).
- Optional recording for Bottom of the Stairs.
- Museum Wi-Fi details, if signal upstairs is weak.
