"""
Buddhist Figures Character Descriptions
Contains detailed descriptions for major Buddhist figures and enlightened masters
"""
from .descriptions import CharacterDescription


BUDDHA_DESC = CharacterDescription(
    id="buddha",
    name_en="Buddha",
    name_ko="부처",
    tagline_en="The Awakened One, Founder of Buddhism",
    tagline_ko="깨달은 자, 불교의 창시자",
    description_en="""Siddhartha Gautama, the Buddha, was the founder of Buddhism who lived in ancient India around the 5th century BCE. Born a prince in the Shakya clan, he renounced his privileged life after encountering suffering and embarked on a spiritual quest for liberation.

After years of ascetic practice, Siddhartha sat beneath the Bodhi tree and achieved enlightenment, becoming the Buddha—"the Awakened One." He realized the Four Noble Truths: that life involves suffering, that suffering arises from craving, that suffering can end, and that the path to its end is the Eightfold Path.

For forty-five years, Buddha traveled and taught throughout India, establishing the sangha (community) and sharing the dharma (teachings). His final words reminded disciples to work out their own salvation with diligence, as all conditioned things are impermanent.""",
    description_ko="""싯다르타 고타마, 부처는 기원전 5세기경 고대 인도에 살았던 불교의 창시자입니다. 석가족의 왕자로 태어난 그는 고통을 마주한 후 특권적인 삶을 포기하고 해탈을 위한 영적 탐구에 나섰습니다.

수년간의 금욕 수행 끝에, 싯다르타는 보리수 아래 앉아 깨달음을 얻어 부처—"깨달은 자"—가 되었습니다. 그는 사성제를 깨달았습니다: 삶에는 고통이 있고, 고통은 갈애에서 일어나며, 고통은 끝날 수 있고, 그 끝으로 가는 길은 팔정도라는 것.

45년 동안, 부처는 인도 전역을 여행하며 가르쳤고, 승가(공동체)를 세우고 법(가르침)을 나누었습니다. 그의 마지막 말씀은 모든 조건 지어진 것은 무상하니 부지런히 스스로의 구원을 이루라고 제자들에게 상기시켰습니다.""",
    traits_en=["Enlightened", "Compassionate", "Peaceful", "Wise", "Liberating"],
    traits_ko=["깨달은", "자비로운", "평화로운", "지혜로운", "해탈하는"],
    story_en="On the night of his enlightenment, Mara the tempter sent armies and temptations to distract Siddhartha. The future Buddha touched the earth, calling it to witness his countless lifetimes of preparation. The earth trembled in response, and Mara fled.",
    story_ko="깨달음의 밤, 유혹자 마라는 싯다르타를 방해하기 위해 군대와 유혹을 보냈습니다. 미래의 부처는 땅을 만지며 그의 수많은 전생의 준비를 증언해 달라고 불렀습니다. 땅은 응답하여 떨렸고, 마라는 도망쳤습니다.",
    match_message_en="You radiate the serene wisdom of Buddha. There is a peaceful, awakened quality to your presence—the look of one who has seen through illusion to the truth beneath.",
    match_message_ko="당신은 부처의 고요한 지혜를 발산합니다. 당신의 존재에는 평화롭고 깨어있는 품질이 있습니다—환상을 꿰뚫어 그 아래의 진리를 본 사람의 모습.",
    image_prompt="Serene figure seated in lotus position beneath Bodhi tree, simple monk's robes, peaceful half-smile, golden aura, enlightened expression",
    visual_description="Serene gentle features, half-closed peaceful eyes, perfect equanimity, expression of deep inner peace and awakened wisdom",
    aliases=["Siddhartha Gautama", "Shakyamuni", "Tathagata", "석가모니"],
    era="Ancient India (c. 563-483 BCE)",
    related_characters=["avalokiteshvara", "maitreya", "ananda"]
)

AVALOKITESHVARA_DESC = CharacterDescription(
    id="avalokiteshvara",
    name_en="Avalokiteshvara",
    name_ko="관세음보살",
    tagline_en="Bodhisattva of Infinite Compassion",
    tagline_ko="무한한 자비의 보살",
    description_en="""Avalokiteshvara is the bodhisattva of compassion, one of the most beloved figures in Mahayana Buddhism. The name means "Lord who looks down with compassion," and this being embodies the infinite mercy that seeks to liberate all beings from suffering.

In East Asian Buddhism, Avalokiteshvara is often portrayed as Guanyin (Chinese) or Kannon (Japanese), frequently in female form. The bodhisattva is said to hear all the cries of the suffering world and manifest in whatever form is needed to help.

Avalokiteshvara postponed final nirvana to help all sentient beings achieve enlightenment first. Some depictions show a thousand arms, each with an eye in the palm, symbolizing the ability to see and reach out to help countless beings simultaneously.""",
    description_ko="""관세음보살은 자비의 보살로, 대승불교에서 가장 사랑받는 인물 중 하나입니다. 이름은 "자비로 내려다보는 주님"을 의미하며, 이 존재는 모든 중생을 고통에서 해방시키고자 하는 무한한 자비를 구현합니다.

동아시아 불교에서, 관세음보살은 종종 관음(중국) 또는 간논(일본)으로 묘사되며, 자주 여성 형태로 나타납니다. 보살은 고통받는 세상의 모든 울음을 듣고 도움이 필요한 어떤 형태로든 나타난다고 합니다.

관세음보살은 모든 유정중생이 먼저 깨달음을 얻을 수 있도록 돕기 위해 최종 열반을 미루었습니다. 일부 묘사에서는 천 개의 팔을 보여주며, 각 손바닥에 눈이 있어 동시에 수많은 중생을 보고 도움의 손길을 뻗을 수 있는 능력을 상징합니다.""",
    traits_en=["Compassionate", "Infinite", "Responsive", "Merciful", "Saving"],
    traits_ko=["자비로운", "무한한", "응답하는", "자애로운", "구원하는"],
    story_en="When Avalokiteshvara looked upon the suffering of all beings and wept, the tears became lotus flowers and one tear transformed into the goddess Tara. Even in grief, the bodhisattva's compassion gives birth to further beings of mercy.",
    story_ko="관세음보살이 모든 중생의 고통을 바라보고 울었을 때, 눈물은 연꽃이 되었고 한 방울의 눈물은 여신 타라가 되었습니다. 슬픔 속에서도, 보살의 자비는 더 많은 자비의 존재들을 낳습니다.",
    match_message_en="You embody the compassionate presence of Avalokiteshvara. There is an infinite, merciful quality to your presence—the look of one who hears suffering and responds with love.",
    match_message_ko="당신은 관세음보살의 자비로운 현존을 구현합니다. 당신의 존재에는 무한하고 자애로운 품질이 있습니다—고통을 듣고 사랑으로 응답하는 사람의 모습.",
    image_prompt="Graceful bodhisattva with serene compassionate expression, white robes with lotus flower, thousand arms radiating, gentle saving presence",
    visual_description="Serene graceful features, compassionate tender eyes, gentle merciful bearing, expression of infinite caring and responsive love",
    aliases=["Guanyin", "Kannon", "Chenrezig", "觀世音菩薩"],
    era="Buddhist Tradition (Eternal)",
    related_characters=["buddha", "tara", "maitreya"]
)

MAITREYA_DESC = CharacterDescription(
    id="maitreya",
    name_en="Maitreya",
    name_ko="미륵보살",
    tagline_en="The Future Buddha, Bringer of Joy",
    tagline_ko="미래의 부처, 기쁨을 가져오는 자",
    description_en="""Maitreya is the future Buddha, currently a bodhisattva residing in Tushita heaven until the time comes for a new Buddha to appear in the world. The name means "loving-kindness," and Maitreya embodies the promise of future enlightenment for all beings.

According to Buddhist scripture, Maitreya will descend to earth when the dharma has been forgotten and humans live to be 80,000 years old. He will achieve enlightenment and teach the dharma anew, bringing a golden age of spiritual awakening.

In East Asian Buddhism, Maitreya is often depicted as the "Laughing Buddha"—a rotund, jovial figure with exposed belly, representing contentment and abundance. This form, based on a 10th-century Chinese monk named Budai, captures Maitreya's joyful, welcoming nature.""",
    description_ko="""미륵은 미래의 부처로, 현재 도솔천에 머무르며 새 부처가 세상에 나타날 때를 기다리는 보살입니다. 이름은 "자애"를 의미하며, 미륵은 모든 중생을 위한 미래 깨달음의 약속을 구현합니다.

불경에 따르면, 미륵은 법이 잊혀지고 인간이 8만 세를 살게 될 때 지상에 내려올 것입니다. 그는 깨달음을 얻고 법을 새롭게 가르쳐, 영적 깨달음의 황금시대를 가져올 것입니다.

동아시아 불교에서, 미륵은 종종 "웃는 부처"로 묘사됩니다—배를 드러낸 뚱뚱하고 쾌활한 모습으로, 만족과 풍요를 상징합니다. 포대라는 10세기 중국 스님에 기반한 이 형태는 미륵의 기쁘고 환영하는 성품을 담아냅니다.""",
    traits_en=["Joyful", "Future", "Hopeful", "Loving", "Abundant"],
    traits_ko=["기쁜", "미래의", "희망찬", "사랑하는", "풍요로운"],
    story_en="It is said that Maitreya waits in Tushita heaven, teaching the dharma to celestial beings while preparing for his final rebirth. Those who call upon Maitreya with sincere devotion may be reborn in Tushita to receive his teachings directly.",
    story_ko="미륵은 도솔천에서 기다리며, 천상의 존재들에게 법을 가르치면서 마지막 환생을 준비한다고 합니다. 진심으로 미륵을 부르는 자들은 도솔천에 다시 태어나 그의 가르침을 직접 받을 수 있습니다.",
    match_message_en="You radiate the joyful hope of Maitreya. There is a future-facing, abundant quality to your presence—the look of one who carries promise and brings joy wherever they go.",
    match_message_ko="당신은 미륵의 기쁜 희망을 발산합니다. 당신의 존재에는 미래를 향하고 풍요로운 품질이 있습니다—약속을 품고 가는 곳마다 기쁨을 가져다주는 사람의 모습.",
    image_prompt="Joyful bodhisattva with content smile, seated waiting posture, holding lotus or dharma wheel, golden light of future promise, hopeful welcoming presence",
    visual_description="Joyful rounded features, bright hopeful eyes, abundant welcoming bearing, expression of future promise and loving anticipation",
    aliases=["Budai", "Laughing Buddha", "Miroku", "彌勒菩薩"],
    era="Buddhist Tradition (Future)",
    related_characters=["buddha", "avalokiteshvara"]
)

BODHIDHARMA_DESC = CharacterDescription(
    id="bodhidharma",
    name_en="Bodhidharma",
    name_ko="달마대사",
    tagline_en="Founder of Zen, Blue-Eyed Sage",
    tagline_ko="선종의 창시자, 푸른 눈의 성인",
    description_en="""Bodhidharma was the legendary monk who brought Chan (Zen) Buddhism from India to China in the 5th or 6th century. Known as the "Blue-Eyed Barbarian," he emphasized direct transmission of enlightenment outside of scriptures—a pointing directly at the heart of humanity.

The most famous story tells of Bodhidharma sitting in meditation facing a wall at Shaolin Temple for nine years, his legs withering from disuse. A student named Huike cut off his own arm to demonstrate his sincerity, and Bodhidharma finally transmitted the dharma to him.

Bodhidharma is also legendary as the originator of Shaolin martial arts, teaching the monks physical exercises that evolved into kung fu. He represents the fierce, uncompromising pursuit of enlightenment and the principle that Buddha-nature can be realized directly.""",
    description_ko="""달마대사는 5세기 또는 6세기에 인도에서 중국으로 선(禪) 불교를 가져온 전설적인 스님입니다. "푸른 눈의 야만인"으로 알려진 그는 경전 밖에서 깨달음의 직접 전수를 강조했습니다—인간의 마음을 직접 가리키는 것.

가장 유명한 이야기는 달마대사가 소림사에서 9년 동안 벽을 향해 명상에 앉아, 다리가 사용하지 않아 시들었다고 전합니다. 혜가라는 제자가 자신의 진심을 보여주기 위해 자신의 팔을 잘랐고, 달마대사는 마침내 그에게 법을 전했습니다.

달마대사는 또한 소림 무술의 창시자로 전설에 남아 있으며, 스님들에게 쿵푸로 발전한 신체 운동을 가르쳤습니다. 그는 맹렬하고 타협하지 않는 깨달음의 추구와 불성이 직접 실현될 수 있다는 원리를 상징합니다.""",
    traits_en=["Intense", "Direct", "Uncompromising", "Transmitting", "Fierce"],
    traits_ko=["강렬한", "직접적인", "타협하지 않는", "전수하는", "맹렬한"],
    story_en="When Emperor Wu asked Bodhidharma what merit he had accumulated through building temples and supporting monks, Bodhidharma replied, 'No merit whatsoever.' The emperor, shocked, asked who this was before him. 'I don't know,' replied Bodhidharma, and left.",
    story_ko="양 무제가 달마대사에게 절을 짓고 스님들을 지원하여 어떤 공덕을 쌓았는지 물었을 때, 달마대사는 '아무 공덕도 없습니다'라고 답했습니다. 충격받은 황제가 그 앞에 있는 이가 누구냐고 물었습니다. '나도 모릅니다'라고 달마대사는 답하고 떠났습니다.",
    match_message_en="You possess the fierce intensity of Bodhidharma. There is a direct, penetrating quality to your presence—the look of one who sees through all pretense to essential truth.",
    match_message_ko="당신은 달마대사의 맹렬한 강렬함을 지니고 있습니다. 당신의 존재에는 직접적이고 관통하는 품질이 있습니다—모든 가식을 꿰뚫어 본질적 진리를 보는 사람의 모습.",
    image_prompt="Fierce bearded monk with intense piercing eyes, bushy eyebrows, red robes, meditation posture, direct uncompromising expression",
    visual_description="Fierce weathered features, intense penetrating eyes with heavy brows, uncompromising bearing, expression of direct transmission",
    aliases=["Damo", "Daruma", "First Patriarch of Zen", "菩提達摩"],
    era="Early Medieval (5th-6th century)",
    related_characters=["huike", "buddha"]
)

WONHYO_DESC = CharacterDescription(
    id="wonhyo",
    name_en="Wonhyo",
    name_ko="원효대사",
    tagline_en="Enlightened by a Skull, Unifier of Korean Buddhism",
    tagline_ko="해골로 깨달은 자, 한국 불교의 통일자",
    description_en="""Wonhyo (617-686) was one of the greatest Buddhist masters in Korean history, famous for his spontaneous enlightenment experience and his efforts to harmonize different Buddhist schools. He represents the distinctive character of Korean Buddhism.

The most famous story tells of Wonhyo on a journey to China for study. Sleeping in a cave during a storm, he drank water from what he thought was a gourd. In the morning, he discovered it was a skull filled with rainwater. He was nauseated—but then realized: the water hadn't changed, only his perception. In that moment, he was enlightened.

Wonhyo returned home, declaring there was nothing to learn abroad that wasn't already within. He became known for breaking monastic rules to bring Buddhism to common people, even having a child with a princess. His philosophy of "harmonizing disputes" sought to unify all Buddhist teachings.""",
    description_ko="""원효(617-686)는 한국 역사상 가장 위대한 불교 스승 중 한 명으로, 자발적인 깨달음 경험과 다른 불교 종파들을 조화시키려는 노력으로 유명합니다. 그는 한국 불교의 독특한 성격을 대표합니다.

가장 유명한 이야기는 원효가 공부를 위해 중국으로 여행하던 중의 일입니다. 폭풍우 중에 동굴에서 자다가, 그는 조롱박이라고 생각한 것에서 물을 마셨습니다. 아침에, 그것이 빗물로 채워진 해골임을 발견했습니다. 메스꺼워했지만—그러다 깨달았습니다: 물은 변하지 않았고, 오직 그의 인식만 변한 것이라고. 그 순간, 그는 깨달음을 얻었습니다.

원효는 집으로 돌아와, 외국에서 배울 것이 이미 안에 없는 것은 없다고 선언했습니다. 그는 불교를 일반인들에게 가져다주기 위해 승려의 계율을 어기는 것으로 알려졌고, 심지어 공주와 아이를 가졌습니다. 그의 "쟁론을 조화시키는" 철학은 모든 불교 가르침을 통일하고자 했습니다.""",
    traits_en=["Enlightened", "Unifying", "Unconventional", "Korean", "Harmonizing"],
    traits_ko=["깨달은", "통일하는", "비관습적인", "한국적인", "조화시키는"],
    story_en="After his skull enlightenment, Wonhyo became known as a 'mad monk' who danced through villages and sang dharma songs in marketplaces. He brought Buddhism out of the monasteries and into the streets, accessible to all.",
    story_ko="해골 깨달음 이후, 원효는 마을을 춤추며 다니고 저잣거리에서 불교 노래를 부르는 '미친 스님'으로 알려졌습니다. 그는 불교를 사찰 밖으로 거리로 가져와, 모든 이들이 접근할 수 있게 했습니다.",
    match_message_en="You carry the unconventional wisdom of Wonhyo. There is a unifying, enlightened quality to your presence—the look of one who found truth in unexpected places.",
    match_message_ko="당신은 원효의 비관습적인 지혜를 지니고 있습니다. 당신의 존재에는 통일하고 깨달은 품질이 있습니다—예상치 못한 곳에서 진리를 찾은 사람의 모습.",
    image_prompt="Korean Buddhist monk in simple robes, dancing freely, unconventional joyful expression, Korean temple and village background, enlightened spontaneous spirit",
    visual_description="Expressive Korean features, bright awakened eyes, unconventional free bearing, expression of spontaneous enlightenment",
    aliases=["원효대사", "Master Wonhyo"],
    era="Three Kingdoms Period (617-686)",
    related_characters=["uisang", "seol_chong"]
)

NICHIREN_DESC = CharacterDescription(
    id="nichiren",
    name_en="Nichiren",
    name_ko="니치렌",
    tagline_en="Prophet of the Lotus Sutra",
    tagline_ko="법화경의 예언자",
    description_en="""Nichiren (1222-1282) was a Japanese Buddhist monk who founded one of the most distinctive and influential schools of Japanese Buddhism. He taught that the Lotus Sutra contained the ultimate truth and that chanting "Nam-myoho-renge-kyo" could bring enlightenment.

Nichiren was famous for his fearless criticism of other Buddhist schools and his warnings that Japan would face disaster if it didn't embrace the true dharma. He was exiled twice and nearly executed, but claimed that his persecutions proved the truth of his teachings.

His approach was revolutionary—he insisted that Buddhism must engage with society and government, not withdraw from the world. The schools that descended from him remain influential today, and his emphasis on the Lotus Sutra shaped Japanese religious culture.""",
    description_ko="""니치렌(1222-1282)은 일본 불교에서 가장 독특하고 영향력 있는 종파 중 하나를 창립한 일본 불교 승려입니다. 그는 법화경이 궁극적인 진리를 담고 있으며 "나무묘법연화경"을 외우면 깨달음을 얻을 수 있다고 가르쳤습니다.

니치렌은 다른 불교 종파에 대한 두려움 없는 비판과 일본이 진정한 법을 받아들이지 않으면 재앙에 직면할 것이라는 경고로 유명했습니다. 그는 두 번 유배되고 거의 처형당할 뻔했지만, 자신의 박해가 그의 가르침의 진리를 증명한다고 주장했습니다.

그의 접근법은 혁명적이었습니다—그는 불교가 세상에서 물러나지 말고 사회와 정부에 관여해야 한다고 주장했습니다. 그에게서 비롯된 종파들은 오늘날까지 영향력을 유지하고 있으며, 법화경에 대한 그의 강조는 일본 종교 문화를 형성했습니다.""",
    traits_en=["Prophetic", "Fierce", "Devoted", "Persecuted", "Revolutionary"],
    traits_ko=["예언적인", "맹렬한", "헌신적인", "박해받은", "혁명적인"],
    story_en="When Nichiren was about to be executed at Tatsunokuchi, a brilliant light appeared in the sky, terrifying the executioners. They could not carry out the sentence, and Nichiren was exiled instead—he took this as proof of the Lotus Sutra's protection.",
    story_ko="니치렌이 다쓰노쿠치에서 처형당하려 할 때, 하늘에 찬란한 빛이 나타나 집행자들을 겁먹게 했습니다. 그들은 형을 집행할 수 없었고, 니치렌은 대신 유배되었습니다—그는 이것을 법화경의 보호의 증거로 받아들였습니다.",
    match_message_en="You possess the prophetic fire of Nichiren. There is a devoted, fierce quality to your presence—the look of one who speaks truth regardless of consequences.",
    match_message_ko="당신은 니치렌의 예언적인 불꽃을 지니고 있습니다. 당신의 존재에는 헌신적이고 맹렬한 품질이 있습니다—결과에 관계없이 진리를 말하는 사람의 모습.",
    image_prompt="Fierce Japanese monk in robes holding lotus sutra scroll, intense prophetic expression, storm clouds and divine light, uncompromising devotion",
    visual_description="Intense Japanese features, burning devoted eyes, prophetic fiery bearing, expression of uncompromising faith",
    aliases=["日蓮", "Nichiren Daishonin"],
    era="Kamakura Period (1222-1282)",
    related_characters=["buddha"]
)


# Export dictionary for registry
BUDDHIST_DESCRIPTIONS: dict[str, CharacterDescription] = {
    "buddha": BUDDHA_DESC,
    "avalokiteshvara": AVALOKITESHVARA_DESC,
    "maitreya": MAITREYA_DESC,
    "bodhidharma": BODHIDHARMA_DESC,
    "wonhyo": WONHYO_DESC,
    "nichiren": NICHIREN_DESC,
}
