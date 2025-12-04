# Multi-Platform Social Sentiment Evolution Analysis

A comprehensive data science project analyzing 150,000+ social media posts across six major platforms to understand sentiment patterns, engagement dynamics, and viral content characteristics.

## 📊 Project Overview

This project performs an in-depth analysis of multi-platform social media data to uncover insights about:
- Content engagement patterns across different platforms
- Sentiment analysis and its impact on user interaction
- Optimal posting strategies for maximum reach
- Factors influencing content virality
- Toxicity scores and their relationship with engagement

## 🗂️ Dataset

**File:** `multi_platform_social_sentiment_evolution.csv`

- **Size:** 150,000+ posts
- **Platforms:** Twitter, Reddit, Instagram, YouTube, TikTok, Facebook
- **Time Period:** 2025-04-19 onwards
- **Languages:** 10 languages including English, Spanish, Portuguese, French, German, Japanese, Korean, Hindi, Arabic, and Chinese

### Key Features

The dataset includes 31 comprehensive columns covering:

- **Post Identification:** post_id, platform, timestamp, date
- **Temporal Features:** hour_of_day, day_of_week, is_weekend
- **User Metrics:** user_id, followers, account_age_days, verified
- **Content Characteristics:** topic, language, content_length, media_type, num_hashtags
- **Sentiment Scores:** sentiment_category, sentiment_positive, sentiment_negative, sentiment_neutral
- **Engagement Metrics:** likes, shares, comments, views, total_engagement, engagement_rate_per_1k_followers
- **Virality Indicators:** hours_since_post, viral_coefficient, cross_platform_spread
- **Additional Metrics:** toxicity_score, location

For detailed column descriptions, see [column_descriptions_social_sentiment.md](column_descriptions_social_sentiment.md).

## 📁 Project Structure

```
Data-Science-Project/
├── README.md                                          # This file
├── main.ipynb                                         # Main analysis notebook
├── multi_platform_social_sentiment_evolution.csv     # Dataset
└── column_descriptions_social_sentiment.md           # Detailed column documentation
```

## 🔬 Analysis Sections

The Jupyter notebook (`main.ipynb`) contains six comprehensive analysis sections:

### 1️⃣ Data Cleaning & Preparation
- Data type verification and conversion
- Missing value analysis
- Data quality assessment

### 2️⃣ Platform Comparison
- Unique characteristics of each social media platform
- Engagement pattern analysis by platform
- Platform-specific metrics comparison

### 3️⃣ Content Strategy Analysis
- Optimal content types and formats
- Topic performance analysis
- Media type effectiveness
- Hashtag usage patterns

### 4️⃣ Sentiment & Toxicity Impact
- Sentiment distribution across platforms
- Relationship between sentiment and engagement
- Toxicity analysis and audience psychology
- Impact of emotional content on virality

### 5️⃣ Temporal Analysis
- Best times to post for maximum engagement
- Day-of-week patterns
- Weekend vs weekday performance
- Hour-by-hour engagement trends

### 6️⃣ Viral Factor Analysis
- Factors contributing to content virality
- Viral coefficient analysis
- Cross-platform spread patterns
- Engagement velocity metrics

### 🎁 Bonus Analysis
- Verified account impact
- Language-specific patterns
- Geographic location analysis

## 🛠️ Technologies & Libraries

This project uses the following Python libraries:

- **Data Processing:** pandas, numpy
- **Data Visualization:** matplotlib, seaborn
- **Analysis:** Standard Python data science stack

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Running the Analysis

1. Clone the repository:
```bash
git clone https://github.com/sebuahdelusi/Data-Science-Project.git
cd Data-Science-Project
```

2. Open the Jupyter notebook:
```bash
jupyter notebook main.ipynb
```

3. Run all cells to reproduce the analysis

## 📈 Key Insights

The analysis reveals:

- **Platform-specific engagement patterns:** Different platforms have unique engagement characteristics
- **Sentiment matters:** Positive content generally receives higher engagement
- **Timing is crucial:** Specific hours and days show significantly better performance
- **Virality factors:** Combination of content quality, timing, and platform choice affects viral potential
- **Verified accounts advantage:** Verified accounts typically achieve ~30% higher engagement

## 📊 Dataset Statistics

- **Total Posts:** 150,000+
- **Unique Users:** 129,556
- **Date Range:** Starting from 2025-04-19
- **Topics Covered:** 15 categories (Technology, Politics, Entertainment, Sports, Health, Climate, Business, Education, Science, Gaming, Food, Travel, Fashion, Finance, AI/ML)
- **Sentiment Distribution:**
  - Positive: 45.1%
  - Neutral: 30.1%
  - Negative: 24.9%
- **Cross-Platform Viral Posts:** 1,946 (1.3%)

## 📝 Notes

- The notebook is in Indonesian language (Bahasa Indonesia) with comprehensive comments
- All columns have 0% missing values (100% complete dataset)
- Engagement metrics follow platform-specific distributions
- The analysis uses seaborn v0.8 darkgrid style for visualizations

## 📄 License

This project is available for educational and research purposes.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements or additional analysis.

## 📧 Contact

For questions or suggestions, please open an issue in this repository.

---

**Note:** This is a comprehensive data science project demonstrating end-to-end analysis of social media sentiment and engagement patterns across multiple platforms.
