import os
import voyageai
from dotenv import load_dotenv
load_dotenv()


# Instantiate Voyager Client
vo = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-2", input_type="document")
print(result.embeddings[0])
print(len(result.embeddings[0]))

