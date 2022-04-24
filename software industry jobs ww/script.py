from serpapi import GoogleSearch
import json

def get_data(query):
  results = []
  i = 0
  while i < 100:
    print('got', i)
    params = {
      "api_key": "553b23be2d4a9901fcd0f2cf16fc9b0f8f485545f0fccc74d69a708762114005",
      "engine": "google_jobs",
      "google_domain": "google.com",
      "q": query,
      "start": i,
      "hl": "en"
    }

    search = GoogleSearch(params)
    results.append(search.get_dict())
    i += 10
  return results

def get_file_with_query(q):
  res = get_data(q)
  newarr = []
  for x in res:
    if "jobs_results" in x:
      for i in x["jobs_results"]:
        newarr.append(i)
  with open(q + '.json', 'w') as f:
    f.write(json.dumps(newarr))

if __name__ == "__main__":
  print('main')
