import { defineStore } from 'pinia';

export const useAlertStore = defineStore('alert', {
  state: () => ({
    alerts: [],
  }),

  actions: {
    notify({ title, message, type = 'info', duration = 3500 }) {
      const id = Date.now() + Math.random().toString(36).substr(2, 5);
      const alertItem = { id, title, message, type };
      this.alerts.push(alertItem);

      if (duration > 0) {
        setTimeout(() => {
          this.dismiss(id);
        }, duration);
      }
      return id;
    },

    success(title, message = '', duration = 3500) {
      return this.notify({ title, message, type: 'success', duration });
    },

    info(title, message = '', duration = 3500) {
      return this.notify({ title, message, type: 'info', duration });
    },

    warning(title, message = '', duration = 4500) {
      return this.notify({ title, message, type: 'warning', duration });
    },

    error(title, message = '', duration = 5000) {
      return this.notify({ title, message, type: 'error', duration });
    },

    dismiss(id) {
      const idx = this.alerts.findIndex(a => a.id === id);
      if (idx !== -1) {
        this.alerts.splice(idx, 1);
      }
    },

    clear() {
      this.alerts = [];
    }
  }
});
