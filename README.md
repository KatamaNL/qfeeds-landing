# Q-Feeds Landing Page

Marketing landing page for [Q-Feeds](https://qfeeds.com/) -- threat intelligence feeds for firewalls.

## Tech Stack

- Single-file HTML (`index.html`) with inline CSS and vanilla JavaScript
- No build tools, no dependencies
- Fonts: Google Fonts (Barlow Condensed, Inter, JetBrains Mono)
- Hosted via GitHub Pages or static hosting

## Features

- Dark-themed cybersecurity design
- Animated terminal simulation (live threat feed)
- Scrolling threat ticker bar
- Scroll-reveal animations (IntersectionObserver)
- Animated counter stats
- Responsive layout (breakpoints at 900px and 600px)
- TrustIndex review widget integration
- Pricing section with three tiers (Community / Plus / Premium)

## Sections

1. **Nav** -- fixed, blurred background
2. **Hero** -- headline, CTA buttons, animated terminal
3. **Trust bar** -- key metrics (2,500+ sources, 20 min updates, <5 min setup, EU hosted)
4. **Ticker** -- scrolling threat IP feed
5. **Integrations** -- Palo Alto, Check Point, OPNsense, Fortinet, Sophos logos
6. **Wave transitions** -- decorative image-based section dividers
7. **Features** -- four feature cards with icons
8. **Stats** -- animated counters
9. **Pricing** -- three-tier pricing grid
10. **Reviews** -- TrustIndex widget
11. **How It Works** -- three-step flow
12. **Final CTA** -- conversion section
13. **Footer** -- links to qfeeds.com

## Local Development

Open `index.html` in a browser. No build step required.

For a local server:

```bash
python3 -m http.server 8000
# or
npx serve .
```

## Deployment

Push to `main` branch. Images and links reference assets on `qfeeds.com`.

## Repository

- GitHub: [KatamaNL/qfeeds-landing](https://github.com/KatamaNL/qfeeds-landing)
- Maintained by: Katama (Herriaan)
- Client: Q-Feeds B.V.
