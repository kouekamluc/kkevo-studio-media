/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        kkevo: {
          canvas: {
            dark: '#06090E',   // Ultra-deep OLED newsroom black
            light: '#F8FAFC',  // Crisp institutional paper white
          },
          surface: {
            dark: '#0B111C',   // Elevated card background
            light: '#FFFFFF',  // Pure white card in light mode
            elevated: '#111A29',
          },
          border: {
            dark: '#162235',   // Crisp dark border
            light: '#E2E8F0',  // Crisp light border
            subtle: 'rgba(255, 255, 255, 0.08)',
          },
          navy: {
            950: '#06090E',
            900: '#0B111C',
            850: '#111A29',
            800: '#172438',
            700: '#233652',
            600: '#384E6E',
          },
          blue: {
            DEFAULT: '#0066FF',
            glow: '#388BFD',
            dark: '#0047BA',
          },
          green: {
            DEFAULT: '#00D26A',
            glow: '#26E881',
            dark: '#00A853',
          },
          cyan: {
            DEFAULT: '#00F0FF',
            dim: '#06B6D4',
          },
          silver: {
            DEFAULT: '#E2E8F0',
            light: '#FFFFFF',
            dim: '#94A3B8',
          },
          status: {
            fact: '#00D26A',
            claim: '#0066FF',
            allegation: '#F59E0B',
            analysis: '#A855F7',
            correction: '#EF4444',
          }
        }
      },
      fontFamily: {
        headline: ['Outfit', 'Cabinet Grotesk', 'Newsreader', 'Georgia', 'serif'],
        sans: ['Plus Jakarta Sans', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      letterSpacing: {
        brand: '0.12em',
        kicker: '0.18em',
      },
      boxShadow: {
        'kkevo-card': '0 4px 20px -2px rgba(0, 0, 0, 0.4)',
        'kkevo-card-hover': '0 12px 35px -5px rgba(0, 0, 0, 0.6), 0 0 20px -5px rgba(0, 102, 255, 0.15)',
        'kkevo-glow': '0 0 30px -5px rgba(0, 102, 255, 0.25)',
        'kkevo-green': '0 0 30px -5px rgba(0, 210, 106, 0.25)',
      }
    },
  },
  plugins: [],
}
