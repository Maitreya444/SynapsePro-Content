# Japanese N5 Grammar — Basic Sentence Patterns

**127 patterns** across **18 categories**, deduplicated from an original 157-entry draft (30 duplicates removed — see the changelog at the end of this file). Each pattern has a stable code (`G0xx`) used by `Japanese/N5/Grammar/cards.md` and by `Analysis/prompts/japanese_grammar_cards_prompt.md`.

This file has two parts: a **checklist** (quick-scan table, one row per pattern, for tracking coverage and for Copilot/NotebookLM prompting) followed by the **full catalogue** (pattern/function/example/English detail behind each `G0xx` code).

---

# Part 1 — Checklist

## Basic Sentence Structure

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 1 | G001 | Nです | Identify or describe something using a noun in a polite sentence | P | ☐ |
| 2 | G002 | Nではありません | Make a negative statement using a noun | P | ☐ |
| 3 | G003 | Nでした | Make a polite past statement using a noun | P | ☐ |
| 4 | G004 | Nではありませんでした | Make a polite negative past statement using a noun | P | ☐ |
| 5 | G005 | Nですか | Ask a polite question using a noun | P | ☐ |
| 6 | G006 | Nも | Express "also" or "too." | P | ☐ |
| 7 | G007 | NのN | Show possession, relationship, or connection between two nouns | P | ☐ |
| 8 | G008 | NはNです | Identify or describe one noun in relation to another noun | P | ☐ |
| 9 | G009 | NはPlaceです | State the location of a person, place, or thing using a noun | P | ☐ |

## Question Patterns

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 10 | G010 | これは何ですか | Ask what something is | R | ☐ |
| 11 | G011 | だれですか / どなたですか | Ask who someone is. 「どなた」is a more polite form of 「だれ」 | R | ☐ |
| 12 | G012 | どこですか | Ask where something or someone is | R | ☐ |
| 13 | G013 | いつですか | Ask when something occurs or when something is | R | ☐ |
| 14 | G014 | 何時ですか | Ask what time it is | R | ☐ |
| 15 | G015 | いくらですか | Ask the price of something | R | ☐ |
| 16 | G016 | どれですか | Ask which item it is when choosing from multiple items | R | ☐ |
| 17 | G017 | どのNですか | Ask which specific noun or item | R | ☐ |
| 18 | G018 | どんなNですか | Ask what kind or type of thing someone or something is | R | ☐ |
| 19 | G019 | どうですか | Ask about the condition, impression, or opinion about something | R | ☐ |
| 20 | G020 | どうしてですか | Ask the reason for something | R | ☐ |
| 21 | G021 | 何をしますか | Ask what someone does or will do | R | ☐ |

## Particles

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 22 | G022 | Nは | Mark the topic of a sentence | FB | ☐ |
| 23 | G023 | Nが | Mark the subject of a sentence and in certain expressions such as likes, abilities, and existence | FB | ☐ |
| 24 | G024 | Nを | Mark the direct object of an action | FB | ☐ |
| 25 | G025 | Timeに | Indicate a specific time when an action occurs | FB | ☐ |
| 26 | G026 | PersonにNをVます | Indicate the person who receives or is the target of an action | FB | ☐ |
| 27 | G027 | PlaceでVます | Indicate the place where an action takes place | FB | ☐ |
| 28 | G028 | Means / ToolでVます | Indicate the means or tool used to perform an action | FB | ☐ |
| 29 | G029 | PersonとVます | Indicate the person with whom an action is performed | FB | ☐ |
| 30 | G030 | 「Sentence」と言います | Quote what someone says | FB | ☐ |
| 31 | G031 | PlaceからV | Indicate the starting point of movement | FB | ☐ |
| 32 | G032 | PlaceまでV | Indicate the endpoint of movement | FB | ☐ |
| 33 | G033 | NやN | List examples of nouns without implying that the list is complete | FB | ☐ |
| 34 | G034 | NとN | Connect nouns in a complete list | FB | ☐ |

## Demonstratives

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 35 | G035 | これ / それ / あれ | Refer to things without directly naming them | R | ☐ |
| 36 | G036 | このN / そのN / あのN | Specify a noun in relation to the speaker and listener | R | ☐ |
| 37 | G037 | ここ / そこ / あそこ | Refer to locations | R | ☐ |
| 38 | G038 | こちら / そちら / あちら | Polite forms used to refer to directions, locations, or people | R | ☐ |
| 39 | G039 | どれ / どのN | Ask which item or which specific noun | R | ☐ |
| 40 | G040 | どこ / どちら | Ask about a location or direction. 「どちら」can also be used politely to ask which of two choices or where someone is from | R | ☐ |

## Existence

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 41 | G041 | Nがあります | State that a non-living thing exists | P | ☐ |
| 42 | G042 | Nがいます | State that a person or living thing exists | P | ☐ |
| 43 | G043 | Nはあります | State or ask whether a non-living thing exists, with the noun as the topic | P | ☐ |
| 44 | G044 | Nはいます | State or ask whether a person or living thing exists, with the noun as the topic | P | ☐ |
| 45 | G045 | PlaceにNがあります | State that a non-living thing exists at a particular location | P | ☐ |
| 46 | G046 | PlaceにNがいます | State that a person or living thing exists at a particular location | P | ☐ |
| 47 | G047 | NはPlaceにあります | State the location of a non-living thing | P | ☐ |
| 48 | G048 | NはPlaceにいます | State the location of a person or living thing | P | ☐ |

## Verb Politeness

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 49 | G049 | Vます | Express an action or event in polite Japanese, commonly referring to the present or future | P | ☐ |
| 50 | G050 | Vません | Express a negative action or event in polite Japanese | P | ☐ |
| 51 | G051 | Vました | Express an action that happened in the past in polite Japanese | P | ☐ |
| 52 | G052 | Vませんでした | Express an action that did not happen in the past | P | ☐ |
| 53 | G053 | Vますか | Form a polite question about an action | P | ☐ |
| 54 | G054 | NをVます | Indicate the direct object of an action | P | ☐ |

## Verb + Time / Frequency

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 55 | G055 | TimeからTimeまでV | Indicate the starting and ending times of an action | FB | ☐ |
| 56 | G056 | 毎日V | Express an action performed every day | FB | ☐ |
| 57 | G057 | いつもV | Express an action that happens always or regularly | FB | ☐ |
| 58 | G058 | よくV | Express that an action happens frequently | FB | ☐ |
| 59 | G059 | ときどきV | Express that an action happens sometimes | FB | ☐ |
| 60 | G060 | あまりVません | Express that an action does not happen very often | FB | ☐ |
| 61 | G061 | ぜんぜんVません | Strongly express that an action does not happen at all | FB | ☐ |

## Movement

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 62 | G062 | Placeへ行きます | Express movement toward a destination | P | ☐ |
| 63 | G063 | Placeへ来ます | Express movement toward a place from the speaker's perspective | P | ☐ |
| 64 | G064 | Placeへ帰ります | Express returning to a place | P | ☐ |
| 65 | G065 | Placeに行きます | Express movement to a destination | P | ☐ |
| 66 | G066 | Placeに来ます | Express movement to a destination | P | ☐ |
| 67 | G067 | Placeに帰ります | Express returning to a destination | P | ☐ |
| 68 | G068 | Vehicleで行きます | Indicate the means of transportation | P | ☐ |
| 69 | G069 | Personと行きます | Indicate the person who accompanies the speaker | P | ☐ |

## Te-Form, Requests, Permission & Prohibition

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 70 | G070 | Vて-form | The て-form is used to connect verbs and forms several important N5 grammar constructions | FB | ☐ |
| 71 | G071 | Vてください | Make a polite request | P | ☐ |
| 72 | G072 | Vています | Express an action that is currently happening or a continuing state | P | ☐ |
| 73 | G073 | Vてもいいです | Express permission | P | ☐ |
| 74 | G074 | Vてはいけません | Express prohibition | P | ☐ |
| 75 | G075 | Vて、V | Connect actions performed in sequence | P | ☐ |
| 76 | G076 | Vてもいいですか | Ask for permission to do something | P | ☐ |
| 77 | G077 | Vないでください | Politely ask someone not to do something | P | ☐ |

## Let's / Invitations

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 78 | G078 | Vましょう | Suggest doing something together | P | ☐ |
| 79 | G079 | Vませんか | Politely invite or suggest doing something | P | ☐ |
| 80 | G080 | Vましょうか | Offer to do something or ask whether the speaker should do something | P | ☐ |

## Want / Desire

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 81 | G081 | Vたいです | Express the speaker's desire to do something | P | ☐ |
| 82 | G082 | Vたくないです | Express that the speaker does not want to do something | P | ☐ |
| 83 | G083 | Nがほしいです | Express the speaker's desire to have or obtain something | P | ☐ |
| 84 | G084 | Vたいですか | Ask whether someone wants to do something | P | ☐ |

## Adjectives

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 85 | G085 | い-adjective + です | Describe something with an い-adjective in a polite sentence | P | ☐ |
| 86 | G086 | い-adjective + N | Directly modify a noun with an い-adjective | P | ☐ |
| 87 | G087 | い-adjective negative | Make an い-adjective negative | P | ☐ |
| 88 | G088 | い-adjective past | Describe something in the past using an い-adjective | P | ☐ |
| 89 | G089 | い-adjective past negative | Make the past negative form of an い-adjective | P | ☐ |
| 90 | G090 | な-adjective + です | Describe something with a な-adjective in a polite sentence | P | ☐ |
| 91 | G091 | な-adjective + N | Modify a noun with a な-adjective | P | ☐ |
| 92 | G092 | な-adjective negative | Make a な-adjective negative | P | ☐ |
| 93 | G093 | な-adjective past | Describe something in the past with a な-adjective | P | ☐ |
| 94 | G094 | な-adjective past negative | Make the past negative form of a な-adjective | P | ☐ |

## Likes / Dislikes / Ability

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 95 | G095 | Nが好きです | Express that someone likes something | P | ☐ |
| 96 | G096 | Nが嫌いです | Express that someone dislikes something | P | ☐ |
| 97 | G097 | Nが上手です | Say that someone is good or skilled at something | P | ☐ |
| 98 | G098 | Nが下手です | Say that someone is not good at something | P | ☐ |
| 99 | G099 | Nがわかります | Express understanding or comprehension | P | ☐ |
| 100 | G100 | Nがあります | Express possession or the existence of a non-living thing depending on context | P | ☐ |

## Comparison

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 101 | G101 | N1はN2よりAdjです | Compare two things and say that N1 is more or less adjective than N2 | P | ☐ |
| 102 | G102 | N1とN2とどちらがAdjですか | Ask which of two things has a greater degree of a quality | P | ☐ |
| 103 | G103 | N1のほうがAdjです | State that one of two things is more adjective than the other | P | ☐ |
| 104 | G104 | Nの中でNが一番Adjです | Say that something is the most adjective among a group | P | ☐ |

## Counting / Quantity

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 105 | G105 | Number + Counter | Count people, objects, or other things using an appropriate counter | R | ☐ |
| 106 | G106 | いくつ | Ask how many items there are when using the general counter つ | R | ☐ |
| 107 | G107 | 何 + Counter | Ask how many or what number of something | R | ☐ |
| 108 | G108 | Quantity + V | Indicate the quantity of something involved in an action | P | ☐ |
| 109 | G109 | Quantity + あります / います | Indicate how many non-living things or living things exist | P | ☐ |
| 110 | G110 | Duration + V | Express how long an action takes place | P | ☐ |

## Time / Duration

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 111 | G111 | ～時 | Express a specific hour or time | R | ☐ |
| 112 | G112 | ～分 | Express minutes | R | ☐ |
| 113 | G113 | ～曜日 | Express days of the week | R | ☐ |
| 114 | G114 | ～月 | Express months | R | ☐ |
| 115 | G115 | ～日 | Express dates or days of the month | R | ☐ |
| 116 | G116 | ～年 | Express years or periods of years | R | ☐ |
| 117 | G117 | ～から～まで | Express a starting point and ending point in time or space | R | ☐ |
| 118 | G118 | ～ぐらい / ～くらい | Express an approximate amount, number, or duration | R | ☐ |

## Degree Adverbs

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 119 | G119 | たくさん | Express a large quantity or that an action is performed a lot | R | ☐ |
| 120 | G120 | 少し | Express a small quantity or degree | R | ☐ |
| 121 | G121 | ちょっと | Express a small amount, degree, or short duration | R | ☐ |

## Basic Connections & Reason

| # | Ref | Grammar Point | Meaning | Suggested Format | Done |
|---|---|---|---|---|---|
| 122 | G122 | ～から — Reason | Give a reason or cause | FB | ☐ |
| 123 | G123 | Nで、N | Connect nouns in a sentence or list | FB | ☐ |
| 124 | G124 | それから | Connect actions or events in sequence | R | ☐ |
| 125 | G125 | そして | Connect related statements or actions | R | ☐ |
| 126 | G126 | でも | Connect contrasting statements | R | ☐ |
| 127 | G127 | ～ですから | Politely give a reason or explanation | FB | ☐ |

---

# Part 2 — Full Catalogue

## Basic Sentence Structure

### G001 — Nです

**Pattern**
Nです

**Function**
Used to identify or describe something using a noun in a polite sentence.

**Example**
わたしは学生です。

**English**
I am a student.

---

### G002 — Nではありません

**Pattern**
Nではありません

**Function**
Used to make a negative statement using a noun.

**Example**
わたしは先生ではありません。

**English**
I am not a teacher.

---

### G003 — Nでした

**Pattern**
Nでした

**Function**
Used to make a polite past statement using a noun.

**Example**
昨日は日曜日でした。

**English**
Yesterday was Sunday.

---

### G004 — Nではありませんでした

**Pattern**
Nではありませんでした

**Function**
Used to make a polite negative past statement using a noun.

**Example**
昨日は休みではありませんでした。

**English**
Yesterday was not a holiday.

---

### G005 — Nですか

**Pattern**
Nですか

**Function**
Used to ask a polite question using a noun.

**Example**
あなたは学生ですか。

**English**
Are you a student?

---

### G006 — Nも

**Pattern**
Nも

**Function**
Used to express "also" or "too."

**Example**
わたしも学生です。

**English**
I am also a student.

---

### G007 — NのN

**Pattern**
NのN

**Function**
Used to show possession, relationship, or connection between two nouns.

**Example**
これはわたしの本です。

**English**
This is my book.

---

### G008 — NはNです

**Pattern**
NはNです

**Function**
Used to identify or describe one noun in relation to another noun.

**Example**
田中さんは先生です。

**English**
Mr. Tanaka is a teacher.

---

### G009 — NはPlaceです

**Pattern**
NはPlaceです

**Function**
Used to state the location of a person, place, or thing using a noun.

**Example**
わたしの学校は東京です。

**English**
My school is in Tokyo.

---

## Question Patterns

### G010 — これは何ですか

**Pattern**
これは何ですか

**Function**
Used to ask what something is.

**Example**
これは何ですか。

**English**
What is this?

---

### G011 — だれですか / どなたですか

**Pattern**
だれですか / どなたですか

**Function**
Used to ask who someone is. 「どなた」is a more polite form of 「だれ」.

**Example**
あの人はだれですか。

**English**
Who is that person?

---

### G012 — どこですか

**Pattern**
どこですか

**Function**
Used to ask where something or someone is.

**Example**
トイレはどこですか。

**English**
Where is the toilet?

---

### G013 — いつですか

**Pattern**
いつですか

**Function**
Used to ask when something occurs or when something is.

**Example**
試験はいつですか。

**English**
When is the exam?

---

### G014 — 何時ですか

**Pattern**
何時ですか

**Function**
Used to ask what time it is.

**Example**
今、何時ですか。

**English**
What time is it now?

---

### G015 — いくらですか

**Pattern**
いくらですか

**Function**
Used to ask the price of something.

**Example**
これはいくらですか。

**English**
How much is this?

---

### G016 — どれですか

**Pattern**
どれですか

**Function**
Used to ask which item it is when choosing from multiple items.

**Example**
あなたのかばんはどれですか。

**English**
Which one is your bag?

---

### G017 — どのNですか

**Pattern**
どのNですか

**Function**
Used to ask which specific noun or item.

**Example**
どの本ですか。

**English**
Which book is it?

---

### G018 — どんなNですか

**Pattern**
どんなNですか

**Function**
Used to ask what kind or type of thing someone or something is.

**Example**
どんな映画ですか。

**English**
What kind of movie is it?

---

### G019 — どうですか

**Pattern**
どうですか

**Function**
Used to ask about the condition, impression, or opinion about something.

**Example**
日本の生活はどうですか。

**English**
How is life in Japan?

---

### G020 — どうしてですか

**Pattern**
どうしてですか

**Function**
Used to ask the reason for something.

**Example**
どうして学校へ行きませんか。

**English**
Why don't you go to school?

---

### G021 — 何をしますか

**Pattern**
何をしますか

**Function**
Used to ask what someone does or will do.

**Example**
日曜日に何をしますか。

**English**
What will you do on Sunday?

---

## Particles

### G022 — Nは

**Pattern**
Nは

**Function**
Used to mark the topic of a sentence.

**Example**
わたしは学生です。

**English**
I am a student.

---

### G023 — Nが

**Pattern**
Nが

**Function**
Used to mark the subject of a sentence and in certain expressions such as likes, abilities, and existence.

**Example**
先生が来ます。

**English**
The teacher is coming.

---

### G024 — Nを

**Pattern**
Nを

**Function**
Used to mark the direct object of an action.

**Example**
ごはんを食べます。

**English**
I eat rice.

---

### G025 — Timeに

**Pattern**
TimeにV

**Function**
Used to indicate a specific time when an action occurs.

**Example**
七時に起きます。

**English**
I wake up at seven o'clock.

---

### G026 — PersonにNをVます

**Pattern**
PersonにNをVます

**Function**
Used to indicate the person who receives or is the target of an action.

**Example**
先生に本を見せます。

**English**
I show the book to the teacher.

---

### G027 — PlaceでVます

**Pattern**
PlaceでVます

**Function**
Used to indicate the place where an action takes place.

**Example**
学校で勉強します。

**English**
I study at school.

---

### G028 — Means / ToolでVます

**Pattern**
MeansでVます

**Function**
Used to indicate the means or tool used to perform an action.

**Example**
バスで学校へ行きます。

**English**
I go to school by bus.

---

### G029 — PersonとVます

**Pattern**
PersonとVます

**Function**
Used to indicate the person with whom an action is performed.

**Example**
友だちと映画を見ます。

**English**
I watch a movie with my friend.

---

### G030 — 「Sentence」と言います

**Pattern**
「Sentence」と言います

**Function**
Used to quote what someone says.

**Example**
田中さんは「ありがとう」と言いました。

**English**
Mr. Tanaka said, "Thank you."

---

### G031 — PlaceからV

**Pattern**
PlaceからV

**Function**
Used to indicate the starting point of movement.

**Example**
学校から帰ります。

**English**
I return from school.

---

### G032 — PlaceまでV

**Pattern**
PlaceまでV

**Function**
Used to indicate the endpoint of movement.

**Example**
駅まで歩きます。

**English**
I walk as far as the station.

---

### G033 — NやN

**Pattern**
NやN

**Function**
Used to list examples of nouns without implying that the list is complete.

**Example**
りんごやバナナを買います。

**English**
I buy things such as apples and bananas.

---

### G034 — NとN

**Pattern**
NとN

**Function**
Used to connect nouns in a complete list.

**Example**
りんごとバナナを買います。

**English**
I buy apples and bananas.

---

## Demonstratives

### G035 — これ / それ / あれ

**Pattern**
これ / それ / あれ

**Function**
Used to refer to things without directly naming them.

**Example**
これは本です。

**English**
This is a book.

---

### G036 — このN / そのN / あのN

**Pattern**
このN / そのN / あのN

**Function**
Used to specify a noun in relation to the speaker and listener.

**Example**
この本はおもしろいです。

**English**
This book is interesting.

---

### G037 — ここ / そこ / あそこ

**Pattern**
ここ / そこ / あそこ

**Function**
Used to refer to locations.

**Example**
ここは学校です。

**English**
This place is a school.

---

### G038 — こちら / そちら / あちら

**Pattern**
こちら / そちら / あちら

**Function**
Polite forms used to refer to directions, locations, or people.

**Example**
こちらは田中さんです。

**English**
This is Mr. Tanaka.

---

### G039 — どれ / どのN

**Pattern**
どれ / どのN

**Function**
Used to ask which item or which specific noun.

**Example**
あなたの本はどれですか。

**English**
Which one is your book?

---

### G040 — どこ / どちら

**Pattern**
どこ / どちら

**Function**
Used to ask about a location or direction. 「どちら」can also be used politely to ask which of two choices or where someone is from.

**Example**
学校はどこですか。

**English**
Where is the school?

---

## Existence

### G041 — Nがあります

**Pattern**
Nがあります

**Function**
Used to state that a non-living thing exists.

**Example**
机があります。

**English**
There is a desk.

---

### G042 — Nがいます

**Pattern**
Nがいます

**Function**
Used to state that a person or living thing exists.

**Example**
先生がいます。

**English**
There is a teacher.

---

### G043 — Nはあります

**Pattern**
Nはあります

**Function**
Used to state or ask whether a non-living thing exists, with the noun as the topic.

**Example**
質問はあります。

**English**
There is a question.

---

### G044 — Nはいます

**Pattern**
Nはいます

**Function**
Used to state or ask whether a person or living thing exists, with the noun as the topic.

**Example**
先生はいます。

**English**
The teacher is here / The teacher is present.

---

### G045 — PlaceにNがあります

**Pattern**
PlaceにNがあります

**Function**
Used to state that a non-living thing exists at a particular location.

**Example**
机の上に本があります。

**English**
There is a book on the desk.

---

### G046 — PlaceにNがいます

**Pattern**
PlaceにNがいます

**Function**
Used to state that a person or living thing exists at a particular location.

**Example**
教室に学生がいます。

**English**
There are students in the classroom.

---

### G047 — NはPlaceにあります

**Pattern**
NはPlaceにあります

**Function**
Used to state the location of a non-living thing.

**Example**
本は机の上にあります。

**English**
The book is on the desk.

---

### G048 — NはPlaceにいます

**Pattern**
NはPlaceにいます

**Function**
Used to state the location of a person or living thing.

**Example**
田中さんは教室にいます。

**English**
Tanaka is in the classroom.

---

## Verb Politeness

### G049 — Vます

**Pattern**
Vます

**Function**
Used to express an action or event in polite Japanese, commonly referring to the present or future.

**Example**
毎日勉強します。

**English**
I study every day.

---

### G050 — Vません

**Pattern**
Vません

**Function**
Used to express a negative action or event in polite Japanese.

**Example**
今日は勉強しません。

**English**
I will not study today.

---

### G051 — Vました

**Pattern**
Vました

**Function**
Used to express an action that happened in the past in polite Japanese.

**Example**
昨日勉強しました。

**English**
I studied yesterday.

---

### G052 — Vませんでした

**Pattern**
Vませんでした

**Function**
Used to express an action that did not happen in the past.

**Example**
昨日勉強しませんでした。

**English**
I did not study yesterday.

---

### G053 — Vますか

**Pattern**
Vますか

**Function**
Used to form a polite question about an action.

**Example**
毎日日本語を勉強しますか。

**English**
Do you study Japanese every day?

---

### G054 — NをVます

**Pattern**
NをVます

**Function**
Used to indicate the direct object of an action.

**Example**
本を読みます。

**English**
I read a book.

---

## Verb + Time / Frequency

### G055 — TimeからTimeまでV

**Pattern**
TimeからTimeまでV

**Function**
Used to indicate the starting and ending times of an action.

**Example**
九時から五時まで働きます。

**English**
I work from nine to five.

---

### G056 — 毎日V

**Pattern**
毎日V

**Function**
Used to express an action performed every day.

**Example**
毎日学校へ行きます。

**English**
I go to school every day.

---

### G057 — いつもV

**Pattern**
いつもV

**Function**
Used to express an action that happens always or regularly.

**Example**
いつも朝ごはんを食べます。

**English**
I always eat breakfast.

---

### G058 — よくV

**Pattern**
よくV

**Function**
Used to express that an action happens frequently.

**Example**
よく映画を見ます。

**English**
I often watch movies.

---

### G059 — ときどきV

**Pattern**
ときどきV

**Function**
Used to express that an action happens sometimes.

**Example**
ときどき図書館へ行きます。

**English**
I sometimes go to the library.

---

### G060 — あまりVません

**Pattern**
あまりVません

**Function**
Used to express that an action does not happen very often.

**Example**
あまりテレビを見ません。

**English**
I don't watch TV very often.

---

### G061 — ぜんぜんVません

**Pattern**
ぜんぜんVません

**Function**
Used to strongly express that an action does not happen at all.

**Example**
ぜんぜんお酒を飲みません。

**English**
I don't drink alcohol at all.

---

## Movement

### G062 — Placeへ行きます

**Pattern**
Placeへ行きます

**Function**
Used to express movement toward a destination.

**Example**
学校へ行きます。

**English**
I go to school.

---

### G063 — Placeへ来ます

**Pattern**
Placeへ来ます

**Function**
Used to express movement toward a place from the speaker's perspective.

**Example**
日本へ来ます。

**English**
I come to Japan.

---

### G064 — Placeへ帰ります

**Pattern**
Placeへ帰ります

**Function**
Used to express returning to a place.

**Example**
家へ帰ります。

**English**
I return home.

---

### G065 — Placeに行きます

**Pattern**
Placeに行きます

**Function**
Used to express movement to a destination.

**Example**
会社に行きます。

**English**
I go to the company/workplace.

---

### G066 — Placeに来ます

**Pattern**
Placeに来ます

**Function**
Used to express movement to a destination.

**Example**
学校に来ます。

**English**
I come to school.

---

### G067 — Placeに帰ります

**Pattern**
Placeに帰ります

**Function**
Used to express returning to a destination.

**Example**
家に帰ります。

**English**
I return home.

---

### G068 — Vehicleで行きます

**Pattern**
Vehicleで行きます

**Function**
Used to indicate the means of transportation.

**Example**
電車で学校へ行きます。

**English**
I go to school by train.

---

### G069 — Personと行きます

**Pattern**
Personと行きます

**Function**
Used to indicate the person who accompanies the speaker.

**Example**
友だちと学校へ行きます。

**English**
I go to school with my friend.

---

## Te-Form, Requests, Permission & Prohibition

### G070 — Vて-form

**Pattern**
Vて-form

**Function**
The て-form is used to connect verbs and forms several important N5 grammar constructions.

**Example**
本を読んで、寝ます。

**English**
I read a book and go to sleep.

---

### G071 — Vてください

**Pattern**
Vてください

**Function**
Used to make a polite request.

**Example**
ここに名前を書いてください。

**English**
Please write your name here.

---

### G072 — Vています

**Pattern**
Vています

**Function**
Used to express an action that is currently happening or a continuing state.

**Example**
今、本を読んでいます。

**English**
I am reading a book now.

---

### G073 — Vてもいいです

**Pattern**
Vてもいいです

**Function**
Used to express permission.

**Example**
ここで写真を撮ってもいいです。

**English**
You may take pictures here.

---

### G074 — Vてはいけません

**Pattern**
Vてはいけません

**Function**
Used to express prohibition.

**Example**
ここで写真を撮ってはいけません。

**English**
You must not take pictures here.

---

### G075 — Vて、V

**Pattern**
Vて、V

**Function**
Used to connect actions performed in sequence.

**Example**
朝ごはんを食べて、学校へ行きます。

**English**
I eat breakfast and then go to school.

---

### G076 — Vてもいいですか

**Pattern**
Vてもいいですか

**Function**
Used to ask for permission to do something.

**Example**
窓を開けてもいいですか。

**English**
May I open the window?

---

### G077 — Vないでください

**Pattern**
Vないでください

**Function**
Used to politely ask someone not to do something.

**Example**
ここで写真を撮らないでください。

**English**
Please do not take pictures here.

---

## Let's / Invitations

### G078 — Vましょう

**Pattern**
Vましょう

**Function**
Used to suggest doing something together.

**Example**
一緒に行きましょう。

**English**
Let's go together.

---

### G079 — Vませんか

**Pattern**
Vませんか

**Function**
Used to politely invite or suggest doing something.

**Example**
一緒に映画を見ませんか。

**English**
Would you like to watch a movie together?

---

### G080 — Vましょうか

**Pattern**
Vましょうか

**Function**
Used to offer to do something or ask whether the speaker should do something.

**Example**
手伝いましょうか。

**English**
Shall I help?

---

## Want / Desire

### G081 — Vたいです

**Pattern**
Vたいです

**Function**
Used to express the speaker's desire to do something.

**Example**
日本へ行きたいです。

**English**
I want to go to Japan.

---

### G082 — Vたくないです

**Pattern**
Vたくないです

**Function**
Used to express that the speaker does not want to do something.

**Example**
今日は出かけたくないです。

**English**
I don't want to go out today.

---

### G083 — Nがほしいです

**Pattern**
Nがほしいです

**Function**
Used to express the speaker's desire to have or obtain something.

**Example**
新しいかばんがほしいです。

**English**
I want a new bag.

---

### G084 — Vたいですか

**Pattern**
Vたいですか

**Function**
Used to ask whether someone wants to do something.

**Example**
日本へ行きたいですか。

**English**
Do you want to go to Japan?

---

## Adjectives

### G085 — い-adjective + です

**Pattern**
い-adjective + です

**Function**
Used to describe something with an い-adjective in a polite sentence.

**Example**
この本はおもしろいです。

**English**
This book is interesting.

---

### G086 — い-adjective + N

**Pattern**
い-adjective + N

**Function**
Used to directly modify a noun with an い-adjective.

**Example**
大きい学校です。

**English**
It is a big school.

---

### G087 — い-adjective negative

**Pattern**
い-adjective → ～くないです

**Function**
Used to make an い-adjective negative.

**Example**
この本はおもしろくないです。

**English**
This book is not interesting.

---

### G088 — い-adjective past

**Pattern**
い-adjective → ～かったです

**Function**
Used to describe something in the past using an い-adjective.

**Example**
昨日は暑かったです。

**English**
Yesterday was hot.

---

### G089 — い-adjective past negative

**Pattern**
い-adjective → ～くなかったです

**Function**
Used to make the past negative form of an い-adjective.

**Example**
昨日は暑くなかったです。

**English**
Yesterday was not hot.

---

### G090 — な-adjective + です

**Pattern**
な-adjective + です

**Function**
Used to describe something with a な-adjective in a polite sentence.

**Example**
この町は静かです。

**English**
This town is quiet.

---

### G091 — な-adjective + N

**Pattern**
な-adjective + な + N

**Function**
Used to modify a noun with a な-adjective.

**Example**
静かな町です。

**English**
It is a quiet town.

---

### G092 — な-adjective negative

**Pattern**
な-adjective + ではありません

**Function**
Used to make a な-adjective negative.

**Example**
この町は静かではありません。

**English**
This town is not quiet.

---

### G093 — な-adjective past

**Pattern**
な-adjective + でした

**Function**
Used to describe something in the past with a な-adjective.

**Example**
昨日は静かでした。

**English**
Yesterday was quiet.

---

### G094 — な-adjective past negative

**Pattern**
な-adjective + ではありませんでした

**Function**
Used to make the past negative form of a な-adjective.

**Example**
昨日は静かではありませんでした。

**English**
Yesterday was not quiet.

---

## Likes / Dislikes / Ability

### G095 — Nが好きです

**Pattern**
Nが好きです

**Function**
Used to express that someone likes something.

**Example**
日本料理が好きです。

**English**
I like Japanese food.

---

### G096 — Nが嫌いです

**Pattern**
Nが嫌いです

**Function**
Used to express that someone dislikes something.

**Example**
野菜が嫌いです。

**English**
I dislike vegetables.

---

### G097 — Nが上手です

**Pattern**
Nが上手です

**Function**
Used to say that someone is good or skilled at something.

**Example**
田中さんは日本語が上手です。

**English**
Tanaka is good at Japanese.

---

### G098 — Nが下手です

**Pattern**
Nが下手です

**Function**
Used to say that someone is not good at something.

**Example**
わたしは歌が下手です。

**English**
I am not good at singing.

---

### G099 — Nがわかります

**Pattern**
Nがわかります

**Function**
Used to express understanding or comprehension.

**Example**
日本語がわかります。

**English**
I understand Japanese.

---

### G100 — Nがあります

**Pattern**
Nがあります

**Function**
Used to express possession or the existence of a non-living thing depending on context.

**Example**
時間があります。

**English**
I have time.

---

## Comparison

### G101 — N1はN2よりAdjです

**Pattern**
N1はN2よりAdjです

**Function**
Used to compare two things and say that N1 is more or less adjective than N2.

**Example**
日本はインドより小さいです。

**English**
Japan is smaller than India.

---

### G102 — N1とN2とどちらがAdjですか

**Pattern**
N1とN2とどちらがAdjですか

**Function**
Used to ask which of two things has a greater degree of a quality.

**Example**
犬と猫とどちらが好きですか。

**English**
Which do you like better, dogs or cats?

---

### G103 — N1のほうがAdjです

**Pattern**
N1のほうがAdjです

**Function**
Used to state that one of two things is more adjective than the other.

**Example**
犬のほうが好きです。

**English**
I like dogs better.

---

### G104 — Nの中でNが一番Adjです

**Pattern**
Nの中でNが一番Adjです

**Function**
Used to say that something is the most adjective among a group.

**Example**
果物の中でりんごが一番好きです。

**English**
Among fruits, I like apples the best.

---

## Counting / Quantity

### G105 — Number + Counter

**Pattern**
Number + Counter

**Function**
Used to count people, objects, or other things using an appropriate counter.

**Example**
りんごを三つ買いました。

**English**
I bought three apples.

---

### G106 — いくつ

**Pattern**
いくつ

**Function**
Used to ask how many items there are when using the general counter つ.

**Example**
りんごはいくつありますか。

**English**
How many apples are there?

---

### G107 — 何 + Counter

**Pattern**
何 + Counter

**Function**
Used to ask how many or what number of something.

**Example**
りんごを何個買いましたか。

**English**
How many apples did you buy?

---

### G108 — Quantity + V

**Pattern**
Quantity + V

**Function**
Used to indicate the quantity of something involved in an action.

**Example**
りんごを三つ食べました。

**English**
I ate three apples.

---

### G109 — Quantity + あります / います

**Pattern**
Quantity + あります / います

**Function**
Used to indicate how many non-living things or living things exist.

**Example**
学生が三人います。

**English**
There are three students.

---

### G110 — Duration + V

**Pattern**
Duration + V

**Function**
Used to express how long an action takes place.

**Example**
二時間勉強します。

**English**
I study for two hours.

---

## Time / Duration

### G111 — ～時

**Pattern**
～時

**Function**
Used to express a specific hour or time.

**Example**
七時に起きます。

**English**
I wake up at seven o'clock.

---

### G112 — ～分

**Pattern**
～分

**Function**
Used to express minutes.

**Example**
十分待ちます。

**English**
I wait for ten minutes.

---

### G113 — ～曜日

**Pattern**
～曜日

**Function**
Used to express days of the week.

**Example**
月曜日に学校へ行きます。

**English**
I go to school on Monday.

---

### G114 — ～月

**Pattern**
～月

**Function**
Used to express months.

**Example**
四月に日本へ行きます。

**English**
I go to Japan in April.

---

### G115 — ～日

**Pattern**
～日

**Function**
Used to express dates or days of the month.

**Example**
七月七日に行きます。

**English**
I will go on July 7th.

---

### G116 — ～年

**Pattern**
～年

**Function**
Used to express years or periods of years.

**Example**
2026年に日本へ行きます。

**English**
I will go to Japan in 2026.

---

### G117 — ～から～まで

**Pattern**
～から～まで

**Function**
Used to express a starting point and ending point in time or space.

**Example**
九時から五時まで働きます。

**English**
I work from nine to five.

---

### G118 — ～ぐらい / ～くらい

**Pattern**
Quantity / Duration + ぐらい / くらい

**Function**
Used to express an approximate amount, number, or duration.

**Example**
一時間ぐらい勉強します。

**English**
I study for about one hour.

---

## Degree Adverbs

### G119 — たくさん

**Pattern**
たくさん + N / V

**Function**
Used to express a large quantity or that an action is performed a lot.

**Example**
本をたくさん読みます。

**English**
I read many books.

---

### G120 — 少し

**Pattern**
少し + N / V

**Function**
Used to express a small quantity or degree.

**Example**
日本語が少しわかります。

**English**
I understand a little Japanese.

---

### G121 — ちょっと

**Pattern**
ちょっと + N / V

**Function**
Used to express a small amount, degree, or short duration.

**Example**
ちょっと待ってください。

**English**
Please wait a moment.

---

## Basic Connections & Reason

### G122 — ～から — Reason

**Pattern**
Sentenceから、Sentence

**Function**
Used to give a reason or cause.

**Example**
暑いですから、窓を開けます。

**English**
Because it is hot, I open the window.

---

### G123 — Nで、N

**Pattern**
Nで、N

**Function**
Used to connect nouns in a sentence or list.

**Example**
これは日本語で、あれは英語です。

**English**
This is in Japanese, and that is in English.

---

### G124 — それから

**Pattern**
Sentence。それから、Sentence。

**Function**
Used to connect actions or events in sequence.

**Example**
朝ごはんを食べます。それから、学校へ行きます。

**English**
I eat breakfast. Then, I go to school.

---

### G125 — そして

**Pattern**
Sentence。そして、Sentence。

**Function**
Used to connect related statements or actions.

**Example**
この町は静かです。そして、きれいです。

**English**
This town is quiet. And it is beautiful.

---

### G126 — でも

**Pattern**
Sentence。でも、Sentence。

**Function**
Used to connect contrasting statements.

**Example**
この本は高いです。でも、おもしろいです。

**English**
This book is expensive. But it is interesting.

---

### G127 — ～ですから

**Pattern**
N / な-adjective + ですから

**Function**
Used to politely give a reason or explanation.

**Example**
明日は休みですから、学校へ行きません。

**English**
Because tomorrow is a holiday, I won't go to school.

---

---

## Duplicate patterns removed

The original draft had 157 numbered entries; 30 were exact or near-exact duplicates of another entry (same underlying grammar point, sometimes with a different example sentence, sometimes just reworded). Each was folded into a single canonical entry. Below, the dropped codes are the *old* (pre-renumbering) codes; the code they were kept as is the *current* `G0xx` code used throughout this file:
- G032 (old codes) -> kept as G006 (`Nも`)
- G033, G034, G104 (old codes) -> kept as G007 (`NのN`)
- G060 (old codes) -> kept as G025 (`TimeにV`)
- G082 (old codes) -> kept as G071 (`Vてください`)
- G083 (old codes) -> kept as G073 (`Vてもいいです`)
- G085 (old codes) -> kept as G074 (`Vてはいけません`)
- G105 (old codes) -> kept as G086 (`い-adjectiveN`)
- G106 (old codes) -> kept as G091 (`な-adjectiveなN`)
- G120 (old codes) -> kept as G015 (`いくらですか`)
- G132 (old codes) -> kept as G057 (`いつもV`)
- G133 (old codes) -> kept as G058 (`よくV`)
- G134 (old codes) -> kept as G059 (`ときどきV`)
- G135 (old codes) -> kept as G060 (`あまりVません`)
- G136 (old codes) -> kept as G061 (`ぜんぜんVません`)
- G140 (old codes) -> kept as G075 (`Vて、V`)
- G145 (old codes) -> kept as G122 (`Sentenceから、Sentence`)
- G149 (old codes) -> kept as G047 (`NはPlaceにあります`)
- G150 (old codes) -> kept as G048 (`NはPlaceにいます`)
- G152 (old codes) -> kept as G027 (`PlaceでVます`)
- G153 (old codes) -> kept as G029 (`PersonとVます`)
- G154 (old codes) -> kept as G095 (`Nが好きです`)
- G155 (old codes) -> kept as G099 (`Nがわかります`)
- G156 (old codes) -> kept as G041 (`Nがあります`)
- G157 (old codes) -> kept as G042 (`Nがいます`)
- G025, G035, G026 (old codes) -> superseded by the specific per-verb entries in Movement/Existence (kept as G065-G067, G062-G064, G045-G046) rather than the vague combined form.
- G146 (old code) -> superseded by G122 — both are the から reason-conjunction pattern, restated with different placeholder names.
