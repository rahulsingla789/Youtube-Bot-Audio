# Read the next article title
next_article = read_next_article()

if next_article is not None:
    # Use the retrieved article title as input to OpenAI GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "From now on which ever topic i give you, you will generate a single photo prompt for stable diffusion(image generation basically)on that topic.ill give you a example if the topic is about a football player ,you will create a propmt that will be used in a video of facts about that Football player,try to create relevent images such as football field in that particular situation.If you understand, say OK."},
            {"role": "assistant", "content": "OK."},
            #{"role": "user", "content":"Narendra Modi"},
            #{"role": "assistant", "content": "'Title: Narendra Modi - India\'s Visionary Leader | Incredible Facts and Achievements\n\nIntro:\n[Upbeat music playing]\nNarrator: Welcome back to our channel,"},
            #{"role": "user", "content":"You Will not include any text that will not be actually spoken in the actuall youtube script for example title, [Upbeat music playing] etc,just write the text that will acually be spoken,if you understand say ok"},
            #{"role": "assistant", "content": "OK."},  
            {"role": "user", "content": next_article}

        ],
        max_tokens=1000  # Adjust the number of tokens as needed
    )

    # Print the response generated by GPT-3.5 Turbo

    print(response.choices[0].message.content)

    # For Printing Syntax
    #print(response)

else:
    print("No more articles to read.")