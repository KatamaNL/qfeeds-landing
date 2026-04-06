# Changelog

## v1.1.0 (2026-04-06)

### Performance
- Reduced Google Fonts from 3 families/8 weights to 2 families/4 weights
- Async font loading via preload pattern
- Replaced JetBrains Mono with system monospace stack
- Deferred decorative JS (terminal, ticker, counters) via requestIdleCallback
- Lazy load TrustIndex widget (IntersectionObserver on reviews section)
- Added image dimensions, fetchpriority, and decoding hints

### Added
- FAQ section with 6 questions (FortiGate setup, Suricata, pricing, EASM)
- FAQ navigation link
- JSON-LD structured data (Organization, SoftwareApplication, FAQPage)

## v1.0.0 (2026-03-18)

Initial release of the Q-Feeds landing page.

### Added
- Single-page landing with dark cybersecurity theme
- Hero section with animated terminal simulation
- Trust bar with key metrics
- Scrolling threat ticker
- Integrations section (Fortinet, OPNsense, Sophos, Palo Alto, Check Point)
- Decorative wave transitions between sections
- Feature section (IP Reputation, Domain Blocklists, TAXII/STIX, EASM)
- Animated stat counters
- Three-tier pricing grid (Community / Plus / Premium)
- TrustIndex review widget
- "How It Works" three-step section
- Final CTA section
- Responsive layout (900px + 600px breakpoints)
- Scroll-reveal animations via IntersectionObserver

### Changed
- Consolidated two landing page variants into single `index.html`
- Tuned integrations section spacing and padding
- Adjusted wave transition visuals
