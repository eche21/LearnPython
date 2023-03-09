# we need to tell python to use the boto3 package
import boto3


def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)
    
text = input("Provide the text you want to translate:") #        "Text":"I am learning to code in AWS",
source_language_code = input("Provide the two letter source language code:")# "SourceLanguageCode":"en",
target_language_code = input("Provide the two letter source language code:")#  "TargetLanguageCode":"fr"

    
def main():    
   translate_text(
        Text = text, #'I am learning to code in AWS',
        SourceLanguageCode= source_language_code, # 'en',
        TargetLanguageCode= target_language_code #'fr'
        )

if __name__== "__main__":
   main()