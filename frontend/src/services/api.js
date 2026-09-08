const API_BASE = '/api/v1';

async function fetchJSON(url, options = {}) {
  const defaultHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  const response = await fetch(url, {
    ...options,
    headers: {
      ...defaultHeaders,
      ...options.headers,
    },
  });

  if (!response.ok) {
    let errData;
    try {
      errData = await response.json();
    } catch {
      errData = { message: response.statusText };
    }
    const error = new Error(errData.message || `HTTP ${response.status}: ${response.statusText}`);
    error.data = errData;
    error.status = response.status;
    throw error;
  }

  return response.json();
}

export const api = {
  // Homepage consolidated feed
  getHomepage() {
    return fetchJSON(`${API_BASE}/articles/homepage/`);
  },

  // Breaking Alert
  getBreakingAlert() {
    return fetchJSON(`${API_BASE}/articles/breaking/`);
  },

  // Articles
  getArticles(params = {}) {
    const query = new URLSearchParams();
    Object.entries(params).forEach(([key, val]) => {
      if (val !== undefined && val !== null && val !== '') {
        query.append(key, val);
      }
    });
    const qs = query.toString();
    return fetchJSON(`${API_BASE}/articles/${qs ? '?' + qs : ''}`);
  },

  getArticle(slug) {
    return fetchJSON(`${API_BASE}/articles/${slug}/`);
  },

  // Taxonomy
  getCategories() {
    return fetchJSON(`${API_BASE}/categories/`);
  },

  getCountries(params = {}) {
    const query = new URLSearchParams(params).toString();
    return fetchJSON(`${API_BASE}/countries/${query ? '?' + query : ''}`);
  },

  getCountry(slug) {
    return fetchJSON(`${API_BASE}/countries/${slug}/`);
  },

  getTopics(params = {}) {
    const query = new URLSearchParams(params).toString();
    return fetchJSON(`${API_BASE}/topics/${query ? '?' + query : ''}`);
  },

  getTopic(slug) {
    return fetchJSON(`${API_BASE}/topics/${slug}/`);
  },

  // Video
  getVideos(params = {}) {
    const query = new URLSearchParams(params).toString();
    return fetchJSON(`${API_BASE}/videos/${query ? '?' + query : ''}`);
  },

  getVideo(slug) {
    return fetchJSON(`${API_BASE}/videos/${slug}/`);
  },

  // Live Blogs
  getLiveBlogs() {
    return fetchJSON(`${API_BASE}/live-blogs/`);
  },

  getLiveBlog(slug) {
    return fetchJSON(`${API_BASE}/live-blogs/${slug}/`);
  },

  // Corrections Ledger
  getCorrections() {
    return fetchJSON(`${API_BASE}/corrections/`);
  },

  // Newsletter
  subscribeNewsletter(email, preferences = {}) {
    return fetchJSON(`${API_BASE}/newsletter/subscribe/`, {
      method: 'POST',
      body: JSON.stringify({ email, preferences }),
    });
  },

  // Reader Bookmarks
  getBookmarks() {
    return fetchJSON(`${API_BASE}/community/bookmarks/`);
  },

  addBookmark(articleId) {
    return fetchJSON(`${API_BASE}/community/bookmarks/`, {
      method: 'POST',
      body: JSON.stringify({ article: articleId }),
    });
  },

  // Newsroom Editorial
  getNewsroomStats() {
    return fetchJSON(`${API_BASE}/analytics/newsroom-stats/`);
  },

  getEditorialArticles() {
    return fetchJSON(`${API_BASE}/editorial/articles/`);
  },

  transitionArticleStatus(articleId, newStatus) {
    return fetchJSON(`${API_BASE}/editorial/articles/${articleId}/transition_status/`, {
      method: 'POST',
      body: JSON.stringify({ status: newStatus }),
    });
  },

  // Auth
  getCurrentUser() {
    return fetchJSON(`${API_BASE}/auth/me/`);
  },

  login(email, password) {
    return fetchJSON(`${API_BASE}/auth/login/`, {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  },

  logout() {
    return fetchJSON(`${API_BASE}/auth/logout/`, {
      method: 'POST',
    });
  },
};
