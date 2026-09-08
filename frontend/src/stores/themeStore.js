import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useThemeStore = defineStore('theme', () => {
  const currentTheme = ref(localStorage.getItem('kkevo-theme') || 'dark');

  function initTheme() {
    if (currentTheme.value === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }

  function toggleTheme() {
    if (currentTheme.value === 'dark') {
      currentTheme.value = 'light';
      document.documentElement.classList.remove('dark');
    } else {
      currentTheme.value = 'dark';
      document.documentElement.classList.add('dark');
    }
    localStorage.setItem('kkevo-theme', currentTheme.value);
  }

  return {
    currentTheme,
    initTheme,
    toggleTheme,
  };
});
