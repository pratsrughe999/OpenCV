import openai
openai.api_key = open("/Users/pratikrughe/Library/Application Support/JetBrains/PyCharmCE2022.3/scratches/API_KEY.txt","r").read()
response = openai.Image.create(
    prompt="A BLUE SUPRA CAR",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(response['data'])
print(image_url)