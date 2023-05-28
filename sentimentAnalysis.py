import openai
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")


keyword = "gluten free"

def sentimentAnalysis():
	reviews2 = """0: Above average vegan food, super delicious but it could have been better with meat in the dishes and animal products. The salad was tasty. I got pasta and the sauce was watery. I really liked the desert with honey and pear toffee. It was super good given that it is vegan. Overall I am not a fan of vegan food, though I do see it’s economic value, but this was surprisingly super good.
1: I loved the range of food on this menu and the garlic knots were absolutely incredible. My milanese dish was quite nice but the dessert was lacking in zest for me. The flavour could have been a little bit stronger and it would have been nicer. I'm not sure how fresh the blueberries were either, I think one of them was gone bad (zoom in on the berries at the forefront/left of the pic). It's a very expensive restaurant. The staff were very friendly and attentive.
2: We went for dinner here on a Saturday. I will recommend to go with a reservation beforehand. Otherwise the wait time can be long. This restaurant is one of the very rare restaurants which serves an entirely vegan Italian menu. We ordered a couple of cocktails to start with along with the mozzarella sticks. The cocktails are really good. We ordered the Golden ticket and the New leaf cocktails. Both of them had a very good balance of the alcohol and the non alcohol components. The breading on the mozzarella sticks was crispy and good. But the vegan mozzarella was very bland. The marinara sauce was a good accompaniment but still could not overcome the blandness beyond a certain extent. For the mains we ordered the Ravioli and the mushroom risotto. The ravioli was decent but the risotto was again a bit bland. The mushrooms and the veggies had a nice crunch and nice taste, but the risotto itself was under seasoned. Overall I wanted to give a rating of 3.5 but since the Google review has only decimal options, I went for the above rating of 3. Overall I liked the ambience and the service.
3: My new favorite restaurant! So so glad we tried this place! Outstanding vegan food! The manager is the sweetest and kindest man! He accommodated all my requests! The staff is so great and sweet especially the man who served us! They made our visit absolutely wonderful and memorable. The food , the vibe, the people! Great , great stuff! Being a vegetarian I can’t say how underrated it is, but anyone who can cook mushrooms that well, just knows food inside out. The deserts, oh my! My all time favorite shall be the Rigatoni, fantastic! Definitely coming back here soon
4: This is my new favorite plant based restaurant in SF. My husband and I came in for the first time tonight and sat at the bar because we didn't have a reservation. I really love the vibe in the restaurant and the gentleman in the suit behind the bar was very friendly and attentive. I had the butternut ravioli and my hubby had some pizza. We shared the "mozzarella" sticks as an appetizer. The cocktails were great. I love that they use Boulders here for the old fashioned and not small ice cubes which are not worthy of whiskey in my opinion. It's a 2-story restaurant with a great center bar and it's in Hayes Valley, which is one of my favorite neighborhoods in SF.
5: PERFECT! Go here for a great experience and an upscale vegan restaurant. This was approved even by my non vegan husband. We loved the meatballs, not so much the mozzarella sticks. I ordered the tortellini and it was very good, small portion though (I had maybe like 7 tortellini in the plate- too small for an entrée) . Lasagna wasn't also our favorite, but it was a big portion. I ordered the lemon custard Frutta, and it was amazing. Also two pizzas for take away. Definitely the best vegan food we had so far in a very elegant place. Will come back here again.
6: Visited this place with a few friends one Wednesday night, had reservations in advance so we were seated right away. Staff was really friendly, service was fast. Atmosphere was really nice, fun and the place felt very upscale. A 100% vegetarian restaurant (which as a vegetarian I absolutely loved). We ordered garlic knots arancini as apps - both were really delicious. I ordered the spaghetti (kale pesto, squash) for my main which was nice and light. Price $$-$$$. Highly recommend checking this place out, especially if you’re looking for a vegetarian friendly spot!
7: Fabulous vegan dining experience. Servers were impressively attentive yet kept their distance and did not rush us through our meal. But the food stole the show. We ordered three courses with cocktails and loved every bite and sip. If you’re in the area and enjoy high-end vegan cuisine, you must give Baia a try.
8: If I could eat here every day I would. Highly recommend. I am not vegan and this food would pass an old school Italian grandma taste test! Came back 2 nights in a row. The food is DELICIOUS and I love the ambiance. Service is quick and excellent. Heads up you can eat upstairs and downstairs. The restrooms are gender neutral just in case that's a concern for you and of course parking is just as difficult as any other part of the city.
9: A really lovely place to get all plant based Italian food. The pasta was delicious and had a good bite, and the mushrooms were fragrant. The parking garage next door was convenient, though not free, and the wait staff was a little stiff and indifferent, but timely and not unfriendly. A solid place to go for good vegan pasta.
"""
	system_msg = "You are an assistant that only returns valid JSON, with no pretext or posttext. "

	# Define the user message
	user_json_msg = f"You are answering questions on the following reviews```{reviews2}``` How many reviews are there? Reply with a JSON array with no pretext or posttext"
	assistant_json_msg = f"[10]"
	user_msg = f"Given a list of keywords [gluten free, vegan, <insert 10 more> ] Reply with a JSON array of JSON arrays with no pretext or posttext. Each array should be all keywords that apply to the given result. Use lateral thinking, for example, if it's implied all they sell is steak, that's probably gluten free"
	response = openai.ChatCompletion.create(model="gpt-4",
											temperature=0,
	                                        messages=[{"role": "system", "content": system_msg},
	                                         {"role": "user", "content": user_json_msg},
	                                         {"role": "assistant", "content": assistant_json_msg},
	                                         {"role": "user", "content": user_msg},
	                                         ])



	print(response)

sentimentAnalysis()
