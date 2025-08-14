<template>
  <div id="app">
    <!-- Header -->
    <header class="header">
      <div class="container">
        <h1>🤖🐜 RoboHormiga</h1>
        <p>AI-Powered News Aggregation Platform</p>
      </div>
    </header>

    <!-- Main Content -->
    <main class="container">
      <!-- Site Notice -->
      <Notice
        v-if="showNotice"
        type="info"
        title="Welcome to RoboHormiga!"
        message="This is a demo platform that scrapes news headlines and displays them in a modern interface. The scraper collects data from BBC News and processes it for enhanced readability."
        :dismissible="true"
        @dismiss="showNotice = false"
      />

      <!-- Loading State -->
      <div v-if="loading" class="loading">
        Loading latest news
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error">
        <h3>⚠️ Unable to Load News</h3>
        <p>{{ error }}</p>
        <button @click="loadNews" class="retry-btn">Try Again</button>
      </div>

      <!-- News Content -->
      <div v-else>
        <!-- News Stats -->
        <div v-if="newsData" class="news-stats">
          <p>
            <strong>{{ newsData.total_articles }}</strong> articles from 
            <strong>{{ newsData.source }}</strong>
            <span v-if="newsData.last_updated"> • Last updated: {{ formatDate(newsData.last_updated) }}</span>
          </p>
        </div>

        <!-- No News Available -->
        <div v-if="!newsData || newsData.articles.length === 0" class="no-news">
          <h3>📰 No News Available</h3>
          <p>Run the scraper to fetch the latest headlines:</p>
          <code>cd scraper && python news_scraper.py</code>
        </div>

        <!-- News Grid -->
        <div v-else class="news-grid">
          <article
            v-for="(article, index) in newsData.articles"
            :key="index"
            class="news-card"
          >
            <h3>
              <a
                :href="article.url"
                target="_blank"
                rel="noopener noreferrer"
                v-if="article.url"
              >
                {{ article.title }}
              </a>
              <span v-else>{{ article.title }}</span>
            </h3>
            <div class="news-meta">
              <span>{{ article.source }}</span>
              <span v-if="article.scraped_at"> • {{ formatDate(article.scraped_at) }}</span>
            </div>
          </article>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <p>&copy; 2025 RoboHormiga • Built with Vue 3 & Vite • MIT License</p>
      </div>
    </footer>
  </div>
</template>

<script>
import Notice from './Notice.vue'

export default {
  name: 'App',
  components: {
    Notice
  },
  data() {
    return {
      newsData: null,
      loading: true,
      error: null,
      showNotice: true
    }
  },
  mounted() {
    this.loadNews()
  },
  methods: {
    async loadNews() {
      this.loading = true
      this.error = null

      try {
        // Try to fetch news.json from the scraper directory
        const response = await fetch('../scraper/news.json')
        
        if (!response.ok) {
          throw new Error(`Failed to fetch news data (${response.status})`)
        }

        const data = await response.json()
        this.newsData = data
        
      } catch (err) {
        console.error('Error loading news:', err)
        this.error = err.message || 'Failed to load news data'
        
        // Provide fallback sample data for demo purposes
        this.newsData = {
          last_updated: new Date().toISOString(),
          total_articles: 3,
          source: 'Sample Data',
          articles: [
            {
              title: 'Welcome to RoboHormiga - Your AI News Platform',
              url: '',
              source: 'RoboHormiga',
              scraped_at: new Date().toISOString()
            },
            {
              title: 'Run the Python scraper to fetch real BBC News headlines',
              url: '',
              source: 'Setup Instructions',
              scraped_at: new Date().toISOString()
            },
            {
              title: 'This demo shows how scraped news data will be displayed',
              url: '',
              source: 'Demo Content',
              scraped_at: new Date().toISOString()
            }
          ]
        }
      } finally {
        this.loading = false
      }
    },
    
    formatDate(dateString) {
      if (!dateString) return ''
      
      try {
        const date = new Date(dateString)
        return date.toLocaleString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
        })
      } catch (err) {
        return dateString
      }
    }
  }
}
</script>

<style>
.news-stats {
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 2rem;
  text-align: center;
  color: #6b7280;
}

.no-news {
  text-align: center;
  padding: 3rem 1rem;
  background: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.no-news h3 {
  color: #374151;
  margin-bottom: 1rem;
}

.no-news code {
  display: inline-block;
  background: #1f2937;
  color: #10b981;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-family: 'Monaco', 'Menlo', monospace;
  margin-top: 1rem;
}

.retry-btn {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
  transition: background-color 0.2s;
}

.retry-btn:hover {
  background: #2563eb;
}
</style>