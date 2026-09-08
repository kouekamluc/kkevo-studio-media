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
          navy: {
            950: '#05080F', // deep navy-black canvas
            900: '#090E17', // elevated card surface
            800: '#111827', // borders & secondary containers
            700: '#1E293B', // subtle dividers
            600: '#334155',
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
            light: '#F8FAFC',
            dim: '#94A3B8',
          },
          status: {
            fact: '#00D26A',
            claim: '#0066FF',
            allegation: '#F59E0B',
            analysis: '#8B5CF6',
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
        'kkevo-glow': '0 0 25px -5px rgba(0, 102, 255, 0.15)',
        'kkevo-green': '0 0 25px -5px rgba(0, 210, 106, 0.15)',
        'kkevo-card': '0 4px 20px -2px rgba(0, 0, 0, 0.5)',
      }
    },
  },
  plugins: [],
}
