# Duolingo Scraper

Scrape public Duolingo data without login. Extract learner profiles with streaks, XP and achievements, weekly league standings, course catalogs with learner counts, and vocabulary words from lessons in clean structured data.

**[Open Duolingo Scraper on Apify](https://apify.com/abotapi/duolingo-learner-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~duolingo-learner-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchType": "profiles", "usernames": ["duolingo"], "courseSort": "learners", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchType` | string | Search type |
| `usernames` | array | Usernames |
| `urls` | array | URLs |
| `courseQuery` | string | Course keyword |
| `courseLearningLanguage` | string | Course language being learned |
| `courseFromLanguage` | string | Course source language |
| `courseMinLearners` | integer | Minimum learners |
| `courseSort` | string | Course sort |
| `vocabSkill` | string | Vocabulary skill filter |
| `learningLanguage` | string | Language being learned |
| `hasPlusOnly` | boolean | Super subscribers only |
| `minTotalXp` | integer | Minimum total XP |
| `minStreak` | integer | Minimum streak |
| `fetchAchievements` | boolean | Achievements detail |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/duolingo-learner-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `username` | string |
| `name` | string |
| `userId` | integer |
| `profileUrl` | string |
| `bio` | null |
| `picture` | string |
| `joinedAt` | integer |
| `streak` | integer |
| `streakData` | object |
| `totalXp` | integer |
| `learningLanguage` | string |
| `fromLanguage` | string |
| `currentCourseId` | string |
| `hasPlus` | boolean |
| `profileCountry` | null |
| `location` | null |
| `hasRecentActivity15` | boolean |
| `betaStatus` | string |
| `motivation` | string |
| `roles` | list |
| `globalAmbassadorStatus` | null |
| `emailVerified` | boolean |
| `courses` | list |
| `coursesCount` | integer |
| `achievements` | list |
| `achievementsCount` | integer |
| `achievementsDetail` | list |

---

[← All scrapers](../../README.md)
