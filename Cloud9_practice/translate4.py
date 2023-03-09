# we need to tell python to use the boto3 package
import boto3


def translate_text(text,source_language_code,target_language_code):
    client = boto3.client('translate')
    response = client.translate_text(
        Text = text, #'I am learning to code in AWS',
        SourceLanguageCode= source_language_code, # 'en',
        TargetLanguageCode= target_language_code, #'fr'
    )
    print(response)

def main():    
   translate_text('I am learning to code in AWS','en','fr')

if __name__== "__main__":
   main()