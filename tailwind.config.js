/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html', // Include app-level templates
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#003049', // Default shade
        },
        secondary: {
          DEFAULT: '#F77F00', // Default shade
          light:'#F18701'
        },
        body: {
          DEFAULT: '#4E4E4E', // Default shade
        },
      },
      fontFamily: {
        title: ['Krub', 'sans-serif'],  // Title font (Figtree)
        subheading: ['Krub', 'sans-serif'],  // Subheading font (Poppins)
        body: ['Krub', 'sans-serif'],  // Body font (Darker Grotesque)
      },
    },
  },
};