"""
World Mythology Character Descriptions
Contains detailed descriptions for mythological figures from various cultures:
African, Polynesian, Native American, Celtic, Mesopotamian, and other world mythologies
"""
from .descriptions import CharacterDescription


# AFRICAN MYTHOLOGY

ANANSI_DESC = CharacterDescription(
    id="anansi",
    name_en="Anansi",
    name_ko="아난시",
    tagline_en="The Spider Trickster, Keeper of Stories",
    tagline_ko="거미 트릭스터, 이야기의 수호자",
    description_en="""Anansi is the legendary spider trickster of Akan/Ashanti tradition from West Africa. Through his cunning and wit, he obtained all the world's stories from the Sky God Nyame, becoming the keeper of wisdom and folklore.

Despite being small and seemingly weak, Anansi consistently outwits larger, stronger creatures through intelligence, trickery, and persistence. His stories spread across the Atlantic during the slave trade, becoming foundational to Caribbean and African American folklore.

Anansi represents the power of the underdog, the triumph of wit over strength, and the vital importance of storytelling. He can be both hero and villain, teaching moral lessons through his successes and failures alike.""",
    description_ko="""아난시는 서아프리카 아칸/아샨티 전통의 전설적인 거미 트릭스터입니다. 그의 교활함과 재치로 하늘 신 냐메로부터 세상의 모든 이야기를 얻어, 지혜와 민간 전승의 수호자가 되었습니다.

작고 겉보기에 약해 보임에도 불구하고, 아난시는 지능, 속임수, 끈기를 통해 더 크고 강한 생물들을 지속적으로 이깁니다. 그의 이야기들은 노예 무역 동안 대서양을 건너 퍼져, 카리브해와 아프리카계 미국인 민간 전승의 기반이 되었습니다.

아난시는 약자의 힘, 힘에 대한 재치의 승리, 이야기하기의 중요성을 대표합니다. 그는 영웅이자 악당이 될 수 있으며, 성공과 실패 모두를 통해 도덕적 교훈을 가르칩니다.""",
    traits_en=["Cunning", "Storytelling", "Trickster", "Wise", "Persistent"],
    traits_ko=["교활한", "이야기하는", "트릭스터", "지혜로운", "끈기 있는"],
    story_en="To win all stories, Anansi had to capture Onini the python, Osebo the leopard, and Mmoboro the hornets. Using clever tricks—pretending to measure the python, digging a pit for the leopard, trapping hornets with water—he succeeded where none thought possible.",
    story_ko="모든 이야기를 얻기 위해, 아난시는 비단뱀 오니니, 표범 오세보, 말벌 음모보로를 잡아야 했습니다. 영리한 속임수—비단뱀을 재는 척하기, 표범을 위한 구덩이 파기, 물로 말벌 잡기—를 사용하여 누구도 가능하다고 생각하지 않던 곳에서 성공했습니다.",
    match_message_en="Your features carry the clever wisdom of Anansi. There is a trickster's wit and storyteller's charm to your presence—the look of one who triumphs through intelligence.",
    match_message_ko="당신의 이목구비는 아난시의 영리한 지혜를 담고 있습니다. 당신의 존재에는 트릭스터의 재치와 이야기꾼의 매력이 있습니다—지능으로 승리하는 사람의 모습.",
    image_prompt="Anthropomorphic spider figure with human and spider features, web of stories around, West African aesthetic, clever knowing expression, storyteller's presence",
    visual_description="Clever adaptable features, quick knowing eyes, trickster's agile bearing, expression of cunning wisdom and storyteller's charm",
    aliases=["Kwaku Ananse", "Aunt Nancy", "Br'er Spider"],
    era="West African Mythology",
    related_characters=["nyame", "tiger"]
)

SHANGO_DESC = CharacterDescription(
    id="shango",
    name_en="Shango",
    name_ko="샹고",
    tagline_en="Orisha of Thunder, King of Fire",
    tagline_ko="천둥의 오리샤, 불의 왕",
    description_en="""Shango is one of the most powerful Orishas in Yoruba religion, the god of thunder, lightning, fire, and justice. Once a mortal king of the Oyo Empire, he ascended to become a deity through his legendary deeds and fiery temperament.

With his double-headed axe (oshe) and ability to breathe fire, Shango represents masculine power, virility, and righteous anger. He punishes liars and wrongdoers with lightning strikes while rewarding the honest and brave. His followers dance to the rhythm of batá drums during his festivals.

Shango's worship spread across the Atlantic, becoming central to Afro-Caribbean religions like Santería (where he syncretized with Saint Barbara), Candomblé, and Vodou. His colors are red and white, and his sacred number is six.""",
    description_ko="""샹고는 요루바 종교에서 가장 강력한 오리샤 중 하나로, 천둥, 번개, 불, 정의의 신입니다. 한때 오요 제국의 필멸의 왕이었던 그는 전설적인 행적과 불같은 기질을 통해 신이 되었습니다.

쌍두도끼(오셰)와 불을 뿜는 능력으로, 샹고는 남성적 힘, 정력, 정의로운 분노를 대표합니다. 그는 번개로 거짓말쟁이와 악인을 벌하면서 정직하고 용감한 자들을 보상합니다. 그의 추종자들은 축제 동안 바타 북의 리듬에 맞춰 춤춥니다.

샹고 숭배는 대서양을 건너 퍼져, 산테리아(성 바바라와 혼합), 칸돔블레, 부두교 같은 아프로-카리브 종교의 중심이 되었습니다. 그의 색깔은 빨강과 흰색이며, 신성한 숫자는 6입니다.""",
    traits_en=["Powerful", "Just", "Fiery", "Kingly", "Virile"],
    traits_ko=["강력한", "공정한", "불같은", "왕다운", "정력적인"],
    story_en="As a mortal king, Shango gained power over lightning but accidentally destroyed his own palace and family. Consumed by grief, he wandered until he ascended into the sky, becoming the Orisha of thunder—his destructive power now channeled toward justice.",
    story_ko="필멸의 왕으로서, 샹고는 번개에 대한 힘을 얻었지만 실수로 자신의 궁전과 가족을 파괴했습니다. 슬픔에 휩싸여 떠돌다가 하늘로 승천하여 천둥의 오리샤가 되었습니다—그의 파괴적인 힘은 이제 정의를 향합니다.",
    match_message_en="Your features carry the thunderous power of Shango. There is a kingly, fiery quality to your presence—the look of one who commands storms and dispenses justice.",
    match_message_ko="당신의 이목구비는 샹고의 천둥 같은 힘을 담고 있습니다. 당신의 존재에는 왕다운 불같은 품질이 있습니다—폭풍을 명령하고 정의를 집행하는 사람의 모습.",
    image_prompt="Powerful African thunder god with double-headed axe, lightning and fire surrounding, kingly bearing, red and white colors, Yoruba aesthetic, commanding fierce expression",
    visual_description="Powerful kingly features, fierce blazing eyes, commanding warrior-king bearing, expression of righteous fire and thunderous power",
    aliases=["Changó", "Xangô", "Jakuta"],
    era="Yoruba Mythology",
    related_characters=["oya", "obatala", "ogun"]
)

MAMI_WATA_DESC = CharacterDescription(
    id="mami_wata",
    name_en="Mami Wata",
    name_ko="마미 와타",
    tagline_en="Mother of Waters, Spirit of the Deep",
    tagline_ko="물의 어머니, 깊은 곳의 영",
    description_en="""Mami Wata is a powerful water spirit venerated throughout Africa and the African diaspora. Often depicted as a beautiful mermaid or woman with a serpent, she embodies the duality of water—nurturing life while capable of drowning it.

She represents feminine beauty, sexuality, wealth, and healing, but also jealousy and dangerous allure. Those she "claims" by pulling underwater may return with prophetic powers, healing abilities, or great fortune—if they survive. Her worshippers must remain faithful to her, often abstaining from other romantic relationships.

Mami Wata's imagery blends African traditions with global influences, reflecting the ocean's role in connecting cultures. She appears in art holding mirrors, combs, and snakes, symbols of her vanity, power, and seductive danger.""",
    description_ko="""마미 와타는 아프리카 전역과 아프리카 디아스포라에서 숭배되는 강력한 물의 영입니다. 종종 아름다운 인어나 뱀과 함께 있는 여인으로 묘사되며, 물의 이중성—생명을 양육하면서 익사시킬 수 있는—을 구현합니다.

그녀는 여성적 아름다움, 성, 부, 치유를 대표하지만, 질투와 위험한 매력도 대표합니다. 그녀가 물 밑으로 끌어당겨 "선택한" 자들은 예언 능력, 치유 능력, 또는 큰 행운을 가지고 돌아올 수 있습니다—살아남는다면. 그녀의 숭배자들은 그녀에게 충실해야 하며, 종종 다른 로맨틱한 관계를 삼가야 합니다.

마미 와타의 이미지는 아프리카 전통과 글로벌 영향을 혼합하여, 문화를 연결하는 바다의 역할을 반영합니다. 그녀는 예술에서 거울, 빗, 뱀을 들고 나타나며, 허영, 힘, 유혹적 위험의 상징입니다.""",
    traits_en=["Seductive", "Powerful", "Jealous", "Healing", "Dangerous"],
    traits_ko=["유혹적인", "강력한", "질투하는", "치유하는", "위험한"],
    story_en="A fisherman was pulled beneath the waves by Mami Wata, spending years in her underwater kingdom. She offered him endless wealth if he would stay faithful. He agreed, but later broke his vow—and lost everything she had given him.",
    story_ko="한 어부가 마미 와타에게 파도 아래로 끌려가 그녀의 수중 왕국에서 수년을 보냈습니다. 그녀는 그가 충실히 머문다면 무한한 부를 제안했습니다. 그는 동의했지만, 나중에 맹세를 어겼고—그녀가 준 모든 것을 잃었습니다.",
    match_message_en="Your features carry the alluring mystery of Mami Wata. There is a deep, hypnotic quality to your presence—the look of one who holds both fortune and danger in their depths.",
    match_message_ko="당신의 이목구비는 마미 와타의 매혹적인 신비를 담고 있습니다. 당신의 존재에는 깊고 최면적인 품질이 있습니다—깊은 곳에 행운과 위험 모두를 품은 사람의 모습.",
    image_prompt="Beautiful African water spirit with mermaid features, long flowing hair, holding mirror and snake, underwater palace, seductive yet dangerous beauty",
    visual_description="Stunning hypnotic features, deep mysterious eyes like dark waters, alluring yet dangerous bearing, expression of seductive power and oceanic mystery",
    aliases=["Mother of Water", "Mammy Water", "La Sirène"],
    era="African Water Spirit Tradition",
    related_characters=["yemoja", "river_spirits"]
)


# POLYNESIAN MYTHOLOGY

MAUI_DESC = CharacterDescription(
    id="maui",
    name_en="Māui",
    name_ko="마우이",
    tagline_en="The Demigod Trickster, Shaper of the World",
    tagline_ko="반신 트릭스터, 세계의 형성자",
    description_en="""Māui is the legendary demigod hero of Polynesian mythology, famous throughout Hawaii, New Zealand, Tahiti, and across the Pacific. Born small and seemingly worthless, he became the greatest hero through cleverness, determination, and magical achievements.

His legendary feats include fishing up the islands from the sea using his magical hook, slowing the sun so humans would have longer days to work, discovering fire for humanity by tricking the fire goddess, and attempting to conquer death itself by crawling into the goddess of death.

Māui represents humanity's defiance of cosmic forces, the trickster who reshapes the world to benefit mortals. Though he ultimately died trying to win immortality for humanity, his achievements remain written across the Pacific islands themselves.""",
    description_ko="""마우이는 하와이, 뉴질랜드, 타히티, 태평양 전역에서 유명한 폴리네시아 신화의 전설적인 반신 영웅입니다. 작고 겉보기에 가치 없이 태어났지만, 영리함, 결단력, 마법적 업적을 통해 가장 위대한 영웅이 되었습니다.

그의 전설적인 업적에는 마법의 갈고리로 바다에서 섬들을 낚아 올리기, 인간이 일할 더 긴 낮을 갖도록 태양을 늦추기, 불의 여신을 속여 인류를 위해 불을 발견하기, 죽음의 여신 안으로 기어들어가 죽음 자체를 정복하려 시도하기가 포함됩니다.

마우이는 우주적 힘에 대한 인류의 도전, 필멸자에게 이익이 되도록 세상을 재형성하는 트릭스터를 대표합니다. 비록 인류를 위한 불멸을 얻으려다 결국 죽었지만, 그의 업적은 태평양 섬들 자체에 기록되어 있습니다.""",
    traits_en=["Heroic", "Trickster", "Defiant", "Creative", "Legendary"],
    traits_ko=["영웅적인", "트릭스터", "도전적인", "창조적인", "전설적인"],
    story_en="When the sun moved too fast across the sky, Māui braided a rope from his sister's hair, climbed to the sun's resting place, and beat it until it agreed to move more slowly. From then on, humanity had long days to fish, farm, and create.",
    story_ko="태양이 하늘을 너무 빨리 움직였을 때, 마우이는 누나의 머리카락으로 밧줄을 엮어 태양의 휴식처로 올라가서, 더 천천히 움직이기로 동의할 때까지 때렸습니다. 그때부터 인류는 낚시하고, 농사짓고, 창조할 긴 낮을 갖게 되었습니다.",
    match_message_en="Your features carry the defiant heroism of Māui. There is a trickster's cleverness and world-shaping power in your presence—the look of one who challenges the gods themselves.",
    match_message_ko="당신의 이목구비는 마우이의 도전적인 영웅주의를 담고 있습니다. 당신의 존재에는 트릭스터의 영리함과 세계를 형성하는 힘이 있습니다—신들 자체에 도전하는 사람의 모습.",
    image_prompt="Polynesian demigod with magical fish hook, muscular heroic build, tribal tattoos, island creation scene, sun in chains, legendary trickster hero presence",
    visual_description="Heroic youthful features, clever defiant eyes, demigod's powerful bearing, expression of trickster wit and world-shaping determination",
    aliases=["Māui-tikitiki", "Maui of the Thousand Tricks"],
    era="Polynesian Mythology",
    related_characters=["hina", "pele", "tangaroa"]
)

PELE_DESC = CharacterDescription(
    id="pele",
    name_en="Pele",
    name_ko="펠레",
    tagline_en="Goddess of Volcanoes, Creator and Destroyer",
    tagline_ko="화산의 여신, 창조자이자 파괴자",
    description_en="""Pele is the Hawaiian goddess of volcanoes, fire, lightning, and wind. She is believed to reside in Kīlauea volcano on the Big Island of Hawaii, one of the world's most active volcanoes. Her fiery temper and passionate nature make her both revered and feared.

She creates new land as lava flows into the sea, literally building the Hawaiian islands—but destroys whatever lies in her path. Her legendary rivalry with her sister Nāmaka, goddess of the sea, caused Pele to be chased across the islands until she found her current home.

Pele is said to appear as either a beautiful young woman in a flowing red dress or as an old woman with white hair. Those who meet her on the road and show kindness are blessed; those who disrespect her face her fiery wrath.""",
    description_ko="""펠레는 화산, 불, 번개, 바람의 하와이 여신입니다. 그녀는 세계에서 가장 활동적인 화산 중 하나인 하와이 빅 아일랜드의 킬라우에아 화산에 거주한다고 믿어집니다. 그녀의 불같은 기질과 열정적인 성격은 그녀를 숭배받으면서도 두려움 받게 합니다.

그녀는 용암이 바다로 흐르면서 새로운 땅을 창조하여 문자 그대로 하와이 제도를 건설합니다—하지만 그녀의 길에 놓인 것은 무엇이든 파괴합니다. 바다의 여신인 언니 나마카와의 전설적인 경쟁은 펠레가 현재의 집을 찾을 때까지 섬들을 가로질러 쫓기게 했습니다.

펠레는 흐르는 빨간 드레스를 입은 아름다운 젊은 여인이나 흰 머리카락을 가진 노파로 나타난다고 합니다. 길에서 그녀를 만나 친절을 보이는 자들은 축복받습니다; 그녀를 무례하게 대하는 자들은 그녀의 불같은 분노에 직면합니다.""",
    traits_en=["Fiery", "Creative", "Destructive", "Passionate", "Temperamental"],
    traits_ko=["불같은", "창조적인", "파괴적인", "열정적인", "기질이 변하기 쉬운"],
    story_en="Pele fell in love with the mortal chief Lohiau. When she could not stay with him, she sent her sister Hi'iaka to fetch him. But Hi'iaka and Lohiau fell in love. In her jealous rage, Pele killed Lohiau with lava—then, overcome with regret, she brought him back to life.",
    story_ko="펠레는 필멸의 추장 로히아우와 사랑에 빠졌습니다. 그와 함께 있을 수 없어서, 언니 히이아카를 보내 그를 데려오게 했습니다. 그러나 히이아카와 로히아우가 사랑에 빠졌습니다. 질투의 분노로 펠레는 용암으로 로히아우를 죽였습니다—그러나 후회에 휩싸여 그를 다시 살렸습니다.",
    match_message_en="Your features carry the volcanic passion of Pele. There is a creative, destructive power in your presence—the look of one who builds and destroys with equal intensity.",
    match_message_ko="당신의 이목구비는 펠레의 화산 같은 열정을 담고 있습니다. 당신의 존재에는 창조적이고 파괴적인 힘이 있습니다—동등한 강도로 건설하고 파괴하는 사람의 모습.",
    image_prompt="Hawaiian volcano goddess with flowing fire hair, red dress like lava, standing in volcanic crater, creating and destroying islands, fierce beautiful expression",
    visual_description="Fierce beautiful features, blazing passionate eyes, volcanic goddess bearing, expression of creative destruction and fiery temperament",
    aliases=["Pelehonuamea", "She Who Shapes the Sacred Land"],
    era="Hawaiian Mythology",
    related_characters=["maui", "namaka", "hiiaka"]
)


# NATIVE AMERICAN MYTHOLOGY

COYOTE_DESC = CharacterDescription(
    id="coyote",
    name_en="Coyote",
    name_ko="코요테",
    tagline_en="The Great Trickster, Creator and Fool",
    tagline_ko="위대한 트릭스터, 창조자이자 바보",
    description_en="""Coyote is the paramount trickster figure in Native American mythology, appearing in stories from dozens of tribes across North America. He is simultaneously creator and destroyer, wise and foolish, sacred and profane.

In some traditions, Coyote helped create the world, gave humans fire, and taught them important skills. In others, he causes chaos, plays pranks, and suffers the consequences of his own foolishness. Often, he gets killed in his misadventures—only to return in the next story.

Coyote embodies the unpredictable, amoral forces of nature and the contradictions within humanity itself. His stories are both entertainment and teaching tools, showing what happens when one ignores taboos, overreaches, or fails to respect the natural order.""",
    description_ko="""코요테는 북미 전역의 수십 개 부족 이야기에 등장하는 아메리카 원주민 신화에서 가장 중요한 트릭스터 인물입니다. 그는 동시에 창조자이자 파괴자, 현명하면서 어리석고, 신성하면서 속된 존재입니다.

일부 전통에서 코요테는 세상 창조를 도왔고, 인간에게 불을 주었으며, 중요한 기술을 가르쳤습니다. 다른 전통에서 그는 혼란을 일으키고, 장난을 치고, 자신의 어리석음의 결과를 겪습니다. 종종 그는 모험에서 죽지만—다음 이야기에서 돌아옵니다.

코요테는 자연의 예측 불가능하고 비도덕적인 힘과 인류 자체 내의 모순을 구현합니다. 그의 이야기는 오락이자 교육 도구로, 금기를 무시하거나, 과도하게 손을 뻗거나, 자연 질서를 존중하지 않을 때 무슨 일이 일어나는지 보여줍니다.""",
    traits_en=["Trickster", "Creative", "Foolish", "Unpredictable", "Resilient"],
    traits_ko=["트릭스터", "창조적인", "어리석은", "예측 불가능한", "회복력 있는"],
    story_en="Coyote stole fire from the Fire Beings by tricking them with a relay race. He passed the fire to other animals until it reached the wood of trees, where it remains hidden—waiting for humans to release it through friction.",
    story_ko="코요테는 릴레이 경주로 불의 존재들을 속여 불을 훔쳤습니다. 그는 다른 동물들에게 불을 전달했고 마침내 나무의 목재에 도달했고, 거기서 숨어 남아 있습니다—인간이 마찰로 풀어주기를 기다리며.",
    match_message_en="Your features carry the unpredictable spirit of Coyote. There is a trickster's adaptability and creative chaos in your presence—the look of one who defies expectations and transcends categories.",
    match_message_ko="당신의 이목구비는 코요테의 예측 불가능한 정신을 담고 있습니다. 당신의 존재에는 트릭스터의 적응력과 창조적 혼돈이 있습니다—기대를 저버리고 범주를 초월하는 사람의 모습.",
    image_prompt="Anthropomorphic coyote figure with clever expression, southwestern desert setting, fire and chaos elements, shape-shifting trickster presence, mythic Native American aesthetic",
    visual_description="Clever adaptable features, mischievous knowing eyes, trickster's agile bearing, expression of creative chaos and resilient foolish wisdom",
    aliases=["Old Man Coyote", "First Angry", "Mica"],
    era="Native American Mythology",
    related_characters=["raven", "spider_woman"]
)

WHITE_BUFFALO_WOMAN_DESC = CharacterDescription(
    id="white_buffalo_woman",
    name_en="White Buffalo Calf Woman",
    name_ko="흰 버팔로 송아지 여인",
    tagline_en="Sacred Messenger, Bringer of the Pipe",
    tagline_ko="신성한 사자, 파이프를 가져온 자",
    description_en="""White Buffalo Calf Woman (Ptesan-Wi) is the sacred prophet of the Lakota Sioux, who brought the chanunpa (sacred pipe) and taught the Seven Sacred Rites that form the spiritual foundation of Lakota life.

She appeared to two scouts as a beautiful woman dressed in white buckskin. One scout had lustful thoughts and was reduced to bones by a cloud; the other treated her with respect and was charged to prepare his people. She taught them how to pray, honor all living things, and maintain the balance between humans and nature.

Before departing, she transformed into a white buffalo calf, promising to return in times of great change. The rare birth of a white buffalo calf is considered a sacred sign of her spiritual presence and a call for humanity to come together in peace.""",
    description_ko="""흰 버팔로 송아지 여인(프테산 위)은 라코타 수족의 신성한 예언자로, 차눈파(신성한 파이프)를 가져오고 라코타 삶의 영적 기반을 형성하는 일곱 가지 신성한 의식을 가르쳤습니다.

그녀는 흰 사슴 가죽을 입은 아름다운 여인으로 두 정찰병에게 나타났습니다. 한 정찰병은 음란한 생각을 했고 구름에 의해 뼈로 환원되었습니다; 다른 이는 그녀를 존경으로 대했고 그의 부족을 준비시키라는 책임을 받았습니다. 그녀는 그들에게 기도하는 법, 모든 생명을 공경하는 법, 인간과 자연 사이의 균형을 유지하는 법을 가르쳤습니다.

떠나기 전, 그녀는 흰 버팔로 송아지로 변신하여, 큰 변화의 시기에 돌아오겠다고 약속했습니다. 드문 흰 버팔로 송아지의 탄생은 그녀의 영적 존재의 신성한 징표이자 인류가 평화롭게 하나되라는 부름으로 여겨집니다.""",
    traits_en=["Sacred", "Teaching", "Prophetic", "Transforming", "Peaceful"],
    traits_ko=["신성한", "가르치는", "예언적인", "변형하는", "평화로운"],
    story_en="When the two scouts approached her, she told the disrespectful one: 'You do not know who I am.' A cloud enveloped him and when it lifted, only his skeleton remained. The respectful scout received her message and led her to his people, where she taught them for four days before her transformation.",
    story_ko="두 정찰병이 그녀에게 다가갔을 때, 그녀는 무례한 자에게 말했습니다: '너는 내가 누구인지 모른다.' 구름이 그를 감쌌고 걷혔을 때, 그의 해골만 남았습니다. 존경을 보인 정찰병은 그녀의 메시지를 받아 그의 부족에게 그녀를 인도했고, 그곳에서 그녀는 변신하기 전 4일 동안 그들을 가르쳤습니다.",
    match_message_en="Your features carry the sacred presence of White Buffalo Calf Woman. There is a prophetic, peace-bringing quality to your presence—the look of one who bridges the spiritual and physical worlds.",
    match_message_ko="당신의 이목구비는 흰 버팔로 송아지 여인의 신성한 존재를 담고 있습니다. 당신의 존재에는 예언적이고 평화를 가져오는 품질이 있습니다—영적 세계와 물질 세계를 연결하는 사람의 모습.",
    image_prompt="Sacred Native American spirit woman in white buckskin dress, white buffalo nearby, holding sacred pipe, Great Plains setting, sacred prophetic presence, divine transformation",
    visual_description="Sacred ethereal features, knowing prophetic eyes, divine messenger's bearing, expression of sacred teaching and transformative peace",
    aliases=["Ptesan-Wi", "White Buffalo Woman"],
    era="Lakota Sioux Mythology",
    related_characters=["wakan_tanka"]
)


# CELTIC MYTHOLOGY

MORRIGAN_DESC = CharacterDescription(
    id="morrigan",
    name_en="The Morrígan",
    name_ko="모리간",
    tagline_en="Phantom Queen, Goddess of War and Fate",
    tagline_ko="유령 여왕, 전쟁과 운명의 여신",
    description_en="""The Morrígan is the Irish goddess of war, fate, death, and sovereignty. Often appearing as a trio of sisters (Badb, Macha, and Morrígan/Nemain), she embodies the terror and glory of battle and the inexorable nature of fate.

She appears on battlefields as a crow or raven, feasting on the slain, or as a washerwoman cleaning the bloodied clothes of those fated to die. She can grant victory or doom, inspire warriors with battle-fury or terrify them into defeat. Her favor was sought but her appearance was feared.

The Morrígan is particularly associated with the hero Cú Chulainn, appearing at his birth, offering him her love (which he unwisely refused), and ultimately foretelling his death. She represents the dark goddess who embodies the female aspects of war and fate.""",
    description_ko="""모리간은 전쟁, 운명, 죽음, 주권의 아일랜드 여신입니다. 종종 세 자매(바브, 마하, 모리간/네만)의 삼위일체로 나타나며, 전투의 공포와 영광, 운명의 피할 수 없는 성격을 구현합니다.

그녀는 전장에서 죽은 자들을 먹는 까마귀나 갈까마귀로, 또는 죽을 운명인 자들의 피 묻은 옷을 빨래하는 빨래 여인으로 나타납니다. 그녀는 승리나 파멸을 줄 수 있고, 전사들에게 전투의 광기를 불어넣거나 공포로 패배하게 할 수 있습니다. 그녀의 호의를 구했지만 그녀의 출현은 두려움 받았습니다.

모리간은 특히 영웅 쿠 훌린과 연관되어, 그의 탄생에 나타나, 그에게 사랑을 제안하고(그가 현명하지 못하게 거부한), 궁극적으로 그의 죽음을 예언합니다. 그녀는 전쟁과 운명의 여성적 측면을 구현하는 어두운 여신을 대표합니다.""",
    traits_en=["Fearsome", "Prophetic", "Sovereign", "Dark", "Triple-aspected"],
    traits_ko=["두려운", "예언적인", "주권적인", "어두운", "삼면의"],
    story_en="Before the second battle of Mag Tuired, the Morrígan mated with the Dagda to secure victory for the Tuatha Dé Danann. During the battle, she chanted incantations that confused the enemy. Victory belonged to those she blessed—and doom to those she cursed.",
    story_ko="마그 투이레드의 두 번째 전투 전에, 모리간은 다그다와 교합하여 투아사 데 다난의 승리를 확보했습니다. 전투 동안 그녀는 적을 혼란시키는 주문을 외웠습니다. 승리는 그녀가 축복한 자들에게—그리고 파멸은 그녀가 저주한 자들에게 속했습니다.",
    match_message_en="Your features carry the dark sovereignty of the Morrígan. There is a prophetic, fearsome quality to your presence—the look of one who embodies both doom and victory.",
    match_message_ko="당신의 이목구비는 모리간의 어두운 주권을 담고 있습니다. 당신의 존재에는 예언적이고 두려운 품질이 있습니다—파멸과 승리 모두를 구현하는 사람의 모습.",
    image_prompt="Dark Celtic goddess with raven features, triple-aspected, battlefield setting, blood and prophecy symbols, fearsome beautiful expression, war goddess presence",
    visual_description="Fierce dark beautiful features, prophetic knowing eyes, sovereign goddess bearing, expression of war's glory and fate's inevitability",
    aliases=["Phantom Queen", "Great Queen", "Badb Catha"],
    era="Irish Celtic Mythology",
    related_characters=["cu_chulainn", "dagda", "lugh"]
)

CU_CHULAINN_DESC = CharacterDescription(
    id="cu_chulainn",
    name_en="Cú Chulainn",
    name_ko="쿠 훌린",
    tagline_en="The Hound of Ulster, Greatest Warrior of Ireland",
    tagline_ko="얼스터의 사냥개, 아일랜드 최고의 전사",
    description_en="""Cú Chulainn is the legendary hero of the Ulster Cycle, Ireland's greatest warrior. Born Sétanta, he earned his famous name ("Culann's Hound") when as a child he killed the fierce hound of the smith Culann and offered to take its place as guardian.

His battle-rage (ríastrad) transformed him into a monstrous, nearly invincible form—one eye would sink into his skull while the other bulged out, his body contorted, and battle-light blazed from his forehead. In this state, he could not distinguish friend from foe.

Single-handedly, he defended Ulster against the armies of Queen Medb during the Táin Bó Cúailnge, fighting each day while the Ulster men lay under a curse. He died young, as prophesied, but achieved the immortality of legend.""",
    description_ko="""쿠 훌린은 아일랜드 최고의 전사인 얼스터 사이클의 전설적인 영웅입니다. 세탄타로 태어나, 어린 시절 대장장이 쿨란의 사나운 개를 죽이고 수호자로 그 자리를 대신하겠다고 제안하여 유명한 이름("쿨란의 사냥개")을 얻었습니다.

그의 전투 광기(리아스트라드)는 그를 괴물 같은 거의 무적의 형태로 변형시켰습니다—한쪽 눈은 두개골 속으로 가라앉고 다른 쪽은 튀어나오며, 몸이 비틀리고, 이마에서 전투의 빛이 타올랐습니다. 이 상태에서 그는 아군과 적을 구별할 수 없었습니다.

혼자서 그는 타인 보 쿠알니에 동안 메이브 여왕의 군대로부터 얼스터를 방어했고, 얼스터 남자들이 저주 아래 누워 있는 동안 매일 싸웠습니다. 예언대로 젊어서 죽었지만, 전설의 불멸을 달성했습니다.""",
    traits_en=["Heroic", "Fierce", "Loyal", "Tragic", "Legendary"],
    traits_ko=["영웅적인", "맹렬한", "충성스러운", "비극적인", "전설적인"],
    story_en="When mortally wounded, Cú Chulainn tied himself to a standing stone so he could die on his feet, facing his enemies. Only when a raven landed on his shoulder did they know he was truly dead—and the hero-light left his face.",
    story_ko="치명상을 입었을 때, 쿠 훌린은 적을 향해 서서 죽을 수 있도록 자신을 돌에 묶었습니다. 까마귀가 그의 어깨에 앉았을 때만 그들은 그가 정말로 죽었다는 것을 알았고—영웅의 빛이 그의 얼굴을 떠났습니다.",
    match_message_en="Your features carry the heroic intensity of Cú Chulainn. There is a fierce, tragic quality to your presence—the look of one destined for glory and early death.",
    match_message_ko="당신의 이목구비는 쿠 훌린의 영웅적 강렬함을 담고 있습니다. 당신의 존재에는 맹렬하고 비극적인 품질이 있습니다—영광과 이른 죽음을 운명 지은 사람의 모습.",
    image_prompt="Young Celtic warrior with spear Gáe Bulg, battle transformation beginning, hero-light on forehead, standing at ford defending alone, tragic heroic intensity",
    visual_description="Fierce youthful features transforming with battle-rage, blazing intense eyes, legendary warrior bearing, expression of heroic fury and tragic destiny",
    aliases=["Sétanta", "The Hound of Culann", "Ireland's Achilles"],
    era="Irish Celtic Mythology - Ulster Cycle",
    related_characters=["morrigan", "scathach", "emer", "medb"]
)


# MESOPOTAMIAN MYTHOLOGY

INANNA_DESC = CharacterDescription(
    id="inanna",
    name_en="Inanna",
    name_ko="이난나",
    tagline_en="Queen of Heaven, Goddess of Love and War",
    tagline_ko="하늘의 여왕, 사랑과 전쟁의 여신",
    description_en="""Inanna is the ancient Sumerian goddess of love, beauty, sex, desire, fertility, war, justice, and political power. She is the most important female deity of ancient Mesopotamia and inspired later goddesses including Ishtar, Astarte, and Aphrodite.

Her mythology is among the oldest recorded in human history. She descended to the underworld, was killed by her sister Ereshkigal, hung on a hook for three days, and was resurrected—one of the earliest death-and-resurrection myths. To leave, she had to send someone to take her place: her husband Dumuzi, who had not mourned her.

Inanna embodies the paradoxes of power: she is goddess of both love and war, of civilization and chaos. She represents female power that is not tamed or domesticated but wild, ambitious, and transformative.""",
    description_ko="""이난나는 사랑, 아름다움, 성, 욕망, 다산, 전쟁, 정의, 정치적 권력의 고대 수메르 여신입니다. 그녀는 고대 메소포타미아에서 가장 중요한 여성 신으로, 이슈타르, 아스타르테, 아프로디테를 포함한 이후 여신들에게 영감을 주었습니다.

그녀의 신화는 인류 역사에서 가장 오래 기록된 것 중 하나입니다. 그녀는 지하세계로 내려가, 언니 에레쉬키갈에게 죽임을 당하고, 3일 동안 갈고리에 매달렸다가 부활했습니다—가장 초기의 죽음과 부활 신화 중 하나. 떠나기 위해 그녀는 자신의 자리를 대신할 누군가를 보내야 했습니다: 그녀를 애도하지 않았던 남편 두무지.

이난나는 권력의 역설을 구현합니다: 그녀는 사랑과 전쟁, 문명과 혼돈 모두의 여신입니다. 그녀는 길들여지거나 가정화되지 않고 야생적이고, 야망적이며, 변형적인 여성 권력을 대표합니다.""",
    traits_en=["Powerful", "Paradoxical", "Ambitious", "Transformative", "Ancient"],
    traits_ko=["강력한", "역설적인", "야망적인", "변형적인", "고대의"],
    story_en="Inanna said: 'I will go to the underworld.' She put on her royal garments and descended through seven gates, forced to remove one item at each until she stood naked before her sister Death. But she arose again, for even death could not hold the Queen of Heaven.",
    story_ko="이난나가 말했습니다: '나는 지하세계로 갈 것이다.' 그녀는 왕족의 옷을 입고 일곱 문을 통해 내려갔고, 각 문에서 하나씩 벗도록 강요받아 언니 죽음 앞에 벌거벗고 섰습니다. 그러나 그녀는 다시 일어났습니다, 심지어 죽음도 하늘의 여왕을 붙들 수 없었기에.",
    match_message_en="Your features carry the paradoxical power of Inanna. There is an ancient, transformative quality to your presence—the look of one who embodies both creation and destruction.",
    match_message_ko="당신의 이목구비는 이난나의 역설적인 힘을 담고 있습니다. 당신의 존재에는 고대의 변형적인 품질이 있습니다—창조와 파괴 모두를 구현하는 사람의 모습.",
    image_prompt="Ancient Mesopotamian goddess with eight-pointed star, lions, owls, multiple divine attributes, descending through seven gates, powerful transformative presence",
    visual_description="Fierce ancient beautiful features, paradoxical knowing eyes, divine queen bearing, expression of wild ambitious power and transformative mystery",
    aliases=["Ishtar", "Queen of Heaven", "Lady of Myriad Offices"],
    era="Sumerian/Mesopotamian Mythology (3500-1500 BCE)",
    related_characters=["dumuzi", "ereshkigal", "gilgamesh"]
)

GILGAMESH_DESC = CharacterDescription(
    id="gilgamesh",
    name_en="Gilgamesh",
    name_ko="길가메시",
    tagline_en="King of Uruk, Seeker of Immortality",
    tagline_ko="우루크의 왕, 불멸을 찾는 자",
    description_en="""Gilgamesh is the legendary king of Uruk from the world's oldest written epic. Two-thirds god and one-third human, he was the mightiest of all kings—but also the most tyrannical, until the gods sent Enkidu to humble him and become his beloved companion.

Together, Gilgamesh and Enkidu slew the demon Humbaba and the Bull of Heaven. But when Enkidu died as punishment for their deeds, Gilgamesh was consumed with grief and terror of death. He journeyed to the ends of the earth seeking immortality, finding the secret—only to lose it to a serpent.

His story, written 4,000 years ago, explores themes that remain timeless: friendship, mortality, the search for meaning, and acceptance of human limits. He returned home to find his immortality not in eternal life but in the walls of Uruk and the civilization he built.""",
    description_ko="""길가메시는 세계에서 가장 오래된 서사시의 전설적인 우루크의 왕입니다. 3분의 2는 신이고 3분의 1은 인간으로, 그는 모든 왕 중 가장 강력했지만—또한 가장 폭군적이었으며, 신들이 엔키두를 보내 그를 겸손하게 하고 사랑하는 동반자가 되게 했습니다.

함께, 길가메시와 엔키두는 악마 훔바바와 하늘의 황소를 죽였습니다. 그러나 엔키두가 그들의 행위에 대한 벌로 죽었을 때, 길가메시는 슬픔과 죽음의 공포에 휩싸였습니다. 그는 불멸을 찾아 지구 끝까지 여행했고, 비밀을 찾았지만—뱀에게 잃었습니다.

4,000년 전에 쓰인 그의 이야기는 시대를 초월하는 주제를 탐구합니다: 우정, 필멸성, 의미 찾기, 인간 한계의 수용. 그는 영생이 아닌 우루크의 성벽과 그가 건설한 문명에서 불멸을 찾아 집으로 돌아왔습니다.""",
    traits_en=["Heroic", "Seeking", "Grieving", "Mighty", "Transformed"],
    traits_ko=["영웅적인", "찾는", "슬퍼하는", "강력한", "변형된"],
    story_en="After finding the plant of immortality at the bottom of the sea, Gilgamesh stopped to bathe. A serpent smelled the plant's fragrance and stole it, shedding its skin and gaining eternal youth. Gilgamesh wept—but finally understood that his true legacy was the great city he would leave behind.",
    story_ko="바다 밑에서 불멸의 식물을 찾은 후, 길가메시는 목욕하기 위해 멈췄습니다. 뱀이 식물의 향기를 맡고 훔쳐, 피부를 벗고 영원한 젊음을 얻었습니다. 길가메시는 울었지만—마침내 그의 진정한 유산이 그가 남길 위대한 도시임을 이해했습니다.",
    match_message_en="Your features carry the mighty seeking of Gilgamesh. There is a questing, transformed quality to your presence—the look of one who has sought immortality and found wisdom instead.",
    match_message_ko="당신의 이목구비는 길가메시의 강력한 추구를 담고 있습니다. 당신의 존재에는 탐구하고 변형된 품질이 있습니다—불멸을 찾았지만 대신 지혜를 발견한 사람의 모습.",
    image_prompt="Ancient Mesopotamian king-hero with wild hair and beard, wrestling lions, searching at world's end, mighty but grief-stricken, legendary hero presence",
    visual_description="Powerful mighty features, grief-tempered seeking eyes, heroic king bearing, expression of mighty grief transformed into acceptance and wisdom",
    aliases=["King of Uruk", "Bilgamesh", "He Who Saw the Deep"],
    era="Mesopotamian Mythology (c. 2100 BCE)",
    related_characters=["enkidu", "inanna", "utnapishtim"]
)


# AZTEC/MESOAMERICAN

QUETZALCOATL_DESC = CharacterDescription(
    id="quetzalcoatl",
    name_en="Quetzalcoatl",
    name_ko="케찰코아틀",
    tagline_en="The Feathered Serpent, Lord of Wind and Learning",
    tagline_ko="깃털 달린 뱀, 바람과 학문의 신",
    description_en="""Quetzalcoatl, the Feathered Serpent, is one of the most important deities of ancient Mesoamerica, worshipped by the Aztec, Maya, and earlier civilizations. He combines the quetzal bird (representing the heavens) with the serpent (representing earth), symbolizing the union of sky and land.

As god of wind, air, and learning, Quetzalcoatl is credited with creating humanity, discovering maize, and inventing the calendar and books. Unlike other Aztec gods, he opposed human sacrifice, preferring offerings of butterflies and jade. He represented wisdom, civilization, and priesthood.

Legend tells that he was tricked into disgrace by the god Tezcatlipoca and left Mexico on a raft of serpents, promising to return. This prophecy allegedly influenced the Aztec reception of Cortés, who arrived from the east in the year prophesied for Quetzalcoatl's return.""",
    description_ko="""깃털 달린 뱀 케찰코아틀은 아즈텍, 마야, 그 이전 문명들이 숭배한 고대 메소아메리카의 가장 중요한 신 중 하나입니다. 그는 케찰 새(하늘을 대표)와 뱀(대지를 대표)을 결합하여 하늘과 땅의 결합을 상징합니다.

바람, 공기, 학문의 신으로서 케찰코아틀은 인류 창조, 옥수수 발견, 달력과 책 발명에 기여했습니다. 다른 아즈텍 신들과 달리, 그는 인신 공양에 반대하며 나비와 옥의 제물을 선호했습니다. 그는 지혜, 문명, 성직을 대표했습니다.

전설에 따르면 그는 신 테스카틀리포카에게 속아 치욕을 당하고 뱀들의 뗏목을 타고 멕시코를 떠나며 돌아오겠다고 약속했습니다. 이 예언은 케찰코아틀의 귀환이 예언된 해에 동쪽에서 도착한 코르테스에 대한 아즈텍의 반응에 영향을 미쳤다고 합니다.""",
    traits_en=["Wise", "Creative", "Civilizing", "Peaceful", "Mysterious"],
    traits_ko=["지혜로운", "창조적인", "문명화하는", "평화로운", "신비로운"],
    story_en="Quetzalcoatl descended to the underworld to retrieve the bones of the previous humanity. Mictlantecuhtli, lord of death, set traps, but Quetzalcoatl succeeded. Though the bones shattered, he sprinkled his blood upon them, and from the fragments arose the current race of humans.",
    story_ko="케찰코아틀은 이전 인류의 뼈를 찾으러 지하세계로 내려갔습니다. 죽음의 신 믹틀란테쿠틀리가 함정을 설치했지만, 케찰코아틀은 성공했습니다. 뼈들이 부서졌지만, 그가 그 위에 피를 뿌리자, 조각들에서 현재의 인류가 일어났습니다.",
    match_message_en="Your features carry the civilizing wisdom of Quetzalcoatl. There is a creative, peaceful quality to your presence—the look of one who brings learning and culture to humanity.",
    match_message_ko="당신의 이목구비는 케찰코아틀의 문명화하는 지혜를 담고 있습니다. 당신의 존재에는 창조적이고 평화로운 품질이 있습니다—인류에게 학문과 문화를 가져다주는 사람의 모습.",
    image_prompt="Feathered serpent deity with quetzal plumage, wind and learning symbols, Aztec temple background, civilizing peaceful presence, majestic sacred beauty",
    visual_description="Majestic otherworldly features combining bird and serpent, wise knowing eyes, divine civilizer bearing, expression of peaceful wisdom and creative power",
    aliases=["Feathered Serpent", "Kukulkan (Maya)", "Ce Acatl Topiltzin"],
    era="Mesoamerican Mythology",
    related_characters=["tezcatlipoca", "huitzilopochtli"]
)


# SLAVIC MYTHOLOGY

BABA_YAGA_DESC = CharacterDescription(
    id="baba_yaga",
    name_en="Baba Yaga",
    name_ko="바바 야가",
    tagline_en="The Wild Crone, Guardian of the Threshold",
    tagline_ko="야생의 노파, 문지방의 수호자",
    description_en="""Baba Yaga is the legendary witch of Slavic folklore, an ancient crone who lives in a hut that stands on chicken legs in the heart of the dark forest. Neither fully good nor evil, she is a force of wild nature that tests those who seek her.

She flies through the air in a mortar, steering with a pestle and sweeping away her tracks with a broom. Her hut is surrounded by a fence of bones with skulls that glow with magical fire. She is served by three mysterious horsemen: White (Day), Red (Sun), and Black (Night).

To those who approach with courage and proper manners, she may grant wisdom, magical objects, or solutions to impossible problems. To those who fail her tests, she is death itself. Baba Yaga represents the wild, untamed feminine power that stands at the boundary between civilization and the unknown.""",
    description_ko="""바바 야가는 슬라브 민간 전승의 전설적인 마녀로, 어두운 숲의 중심에 닭 다리 위에 서 있는 오두막에 사는 고대의 노파입니다. 완전히 선하지도 악하지도 않은, 그녀를 찾는 자들을 시험하는 야생 자연의 힘입니다.

그녀는 절구에 타고 공중을 날며, 절굿공이로 조종하고 빗자루로 흔적을 쓸어냅니다. 그녀의 오두막은 마법의 불로 빛나는 해골들이 있는 뼈 울타리로 둘러싸여 있습니다. 그녀는 세 명의 신비한 기사—흰색(낮), 빨간색(태양), 검은색(밤)—에게 시중을 받습니다.

용기와 적절한 예절로 다가오는 자들에게, 그녀는 지혜, 마법 물건, 또는 불가능한 문제의 해결책을 줄 수 있습니다. 그녀의 시험에 실패한 자들에게, 그녀는 죽음 자체입니다. 바바 야가는 문명과 미지 사이의 경계에 서 있는 야생적이고 길들여지지 않은 여성적 힘을 대표합니다.""",
    traits_en=["Wild", "Testing", "Ancient", "Ambiguous", "Powerful"],
    traits_ko=["야생적인", "시험하는", "고대의", "모호한", "강력한"],
    story_en="Vasilisa the Beautiful was sent to Baba Yaga for fire. The witch set her impossible tasks—sorting poppy seeds from dirt, pressing oil from seeds—but Vasilisa's magic doll (her mother's blessing) helped her complete them. Impressed, Baba Yaga gave her the fire and let her go.",
    story_ko="미녀 바실리사가 불을 얻으러 바바 야가에게 보내졌습니다. 마녀는 그녀에게 불가능한 과제들—흙에서 양귀비 씨앗 분류하기, 씨앗에서 기름 짜기—을 주었지만, 바실리사의 마법 인형(어머니의 축복)이 그녀를 도와 완수했습니다. 감명받은 바바 야가는 그녀에게 불을 주고 보내주었습니다.",
    match_message_en="Your features carry the wild testing power of Baba Yaga. There is an ancient, threshold-guarding quality to your presence—the look of one who tests the worthy and destroys the foolish.",
    match_message_ko="당신의 이목구비는 바바 야가의 야생적이고 시험하는 힘을 담고 있습니다. 당신의 존재에는 고대의 문지방을 지키는 품질이 있습니다—가치 있는 자를 시험하고 어리석은 자를 파괴하는 사람의 모습.",
    image_prompt="Ancient Slavic witch crone in hut on chicken legs, flying mortar and pestle, bone fence with glowing skulls, wild forest setting, terrifying yet wise",
    visual_description="Ancient crone features both terrifying and wise, wild knowing eyes, threshold guardian bearing, expression of wild testing power and ancient forest mystery",
    aliases=["Baba Jaga", "Grandmother Witch", "Bone-Legged One"],
    era="Slavic Folklore",
    related_characters=["koschei", "vasilisa"]
)


# AUSTRALIAN ABORIGINAL

RAINBOW_SERPENT_DESC = CharacterDescription(
    id="rainbow_serpent",
    name_en="Rainbow Serpent",
    name_ko="무지개 뱀",
    tagline_en="Creator of the World, Keeper of Waters",
    tagline_ko="세계의 창조자, 물의 수호자",
    description_en="""The Rainbow Serpent is one of the most important creator beings in Australian Aboriginal mythology, appearing in the Dreamtime stories of peoples across the continent. This immense serpent shaped the land itself, carving out rivers, valleys, and mountains as it traveled.

When the Rainbow Serpent moves, it creates waterways and billabongs. When it arches across the sky after rain, it appears as the rainbow. It is associated with water, fertility, and the cycle of seasons. Disturbing the places sacred to the Rainbow Serpent can bring drought or flood.

The Rainbow Serpent represents the life-giving power of water in the Australian landscape and the interconnection of all things. Known by different names in different Aboriginal nations—Ungud, Wollunqua, Yurlungur—it is perhaps the most widespread deity in Aboriginal Australia.""",
    description_ko="""무지개 뱀은 호주 원주민 신화에서 가장 중요한 창조 존재 중 하나로, 대륙 전역 민족들의 드림타임 이야기에 등장합니다. 이 거대한 뱀은 여행하며 강, 계곡, 산을 깎아 땅 자체를 형성했습니다.

무지개 뱀이 움직일 때, 수로와 빌라봉(물웅덩이)을 만듭니다. 비 후 하늘을 가로질러 아치를 그릴 때, 무지개로 나타납니다. 물, 다산, 계절의 순환과 연관됩니다. 무지개 뱀에게 신성한 장소를 방해하면 가뭄이나 홍수를 가져올 수 있습니다.

무지개 뱀은 호주 풍경에서 물의 생명을 주는 힘과 모든 것의 상호 연결을 대표합니다. 다른 원주민 국가에서 다른 이름—웅구드, 월룽쿠아, 율룽구르—으로 알려져 있으며, 아마도 호주 원주민에서 가장 널리 퍼진 신일 것입니다.""",
    traits_en=["Creating", "Powerful", "Ancient", "Life-giving", "Transforming"],
    traits_ko=["창조하는", "강력한", "고대의", "생명을 주는", "변형하는"],
    story_en="In the Dreamtime, the Rainbow Serpent awoke from beneath the ground and traveled across the flat land, pushing up mountains and digging out rivers. Where it rested, it created waterholes. The landscape of Australia is the record of its journey.",
    story_ko="드림타임에, 무지개 뱀이 땅 아래에서 깨어나 평평한 땅을 가로질러 여행하며, 산을 밀어 올리고 강을 파냈습니다. 쉬는 곳마다 물웅덩이를 만들었습니다. 호주의 풍경은 그 여정의 기록입니다.",
    match_message_en="Your features carry the primal creative power of the Rainbow Serpent. There is an ancient, landscape-shaping quality to your presence—the look of one who creates the very contours of the world.",
    match_message_ko="당신의 이목구비는 무지개 뱀의 원초적 창조력을 담고 있습니다. 당신의 존재에는 고대의 풍경을 형성하는 품질이 있습니다—세상의 윤곽 자체를 창조하는 사람의 모습.",
    image_prompt="Immense iridescent serpent across Australian landscape, creating rivers and mountains, rainbow colors, Dreamtime aesthetic, primal creative presence",
    visual_description="Flowing serpentine features with rainbow iridescence, ancient primal eyes, land-creating presence, expression of primordial creative power",
    aliases=["Ungud", "Wollunqua", "Yurlungur", "Ngalyod"],
    era="Australian Aboriginal Dreamtime",
    related_characters=["baiame"]
)


# PERSIAN/ZOROASTRIAN

AHURA_MAZDA_DESC = CharacterDescription(
    id="ahura_mazda",
    name_en="Ahura Mazda",
    name_ko="아후라 마즈다",
    tagline_en="Lord of Wisdom, Creator of All Good",
    tagline_ko="지혜의 군주, 모든 선의 창조자",
    description_en="""Ahura Mazda is the supreme deity of Zoroastrianism, the ancient Persian religion that profoundly influenced Judaism, Christianity, and Islam. He is the uncreated creator of the universe, the source of all that is good, true, and orderly.

He represents light, truth (Asha), and wisdom in eternal opposition to Angra Mainyu (Ahriman), the destructive spirit of lies and chaos. This cosmic battle between good and evil, light and darkness, was one of the first dualistic religious concepts in history.

Ahura Mazda created the Amesha Spentas (Bounteous Immortals) to help govern creation. Zoroaster, the prophet of this religion, received his revelations directly from Ahura Mazda. The faith teaches that good thoughts, good words, and good deeds align one with Ahura Mazda's truth.""",
    description_ko="""아후라 마즈다는 유대교, 기독교, 이슬람에 깊은 영향을 미친 고대 페르시아 종교인 조로아스터교의 최고 신입니다. 그는 우주의 창조되지 않은 창조자, 선하고 참되며 질서 있는 모든 것의 근원입니다.

그는 거짓과 혼돈의 파괴적 영인 앙그라 마이뉴(아흐리만)와 영원한 대립 속에서 빛, 진리(아샤), 지혜를 대표합니다. 선과 악, 빛과 어둠 사이의 이 우주적 전투는 역사상 최초의 이원론적 종교 개념 중 하나였습니다.

아후라 마즈다는 창조를 다스리는 것을 돕기 위해 아메샤 스펜타(풍요로운 불멸자들)를 창조했습니다. 이 종교의 예언자 조로아스터는 아후라 마즈다로부터 직접 계시를 받았습니다. 이 신앙은 선한 생각, 선한 말, 선한 행동이 아후라 마즈다의 진리와 일치하게 한다고 가르칩니다.""",
    traits_en=["Wise", "Good", "Creating", "Light", "Truthful"],
    traits_ko=["지혜로운", "선한", "창조하는", "빛의", "진실한"],
    story_en="In the beginning, Ahura Mazda existed alone in infinite light. He created the universe in seven stages, culminating in humanity—beings with free will who could choose good over evil. The cosmic battle will end when humanity's good choices finally defeat darkness.",
    story_ko="태초에, 아후라 마즈다는 무한한 빛 속에 홀로 존재했습니다. 그는 일곱 단계로 우주를 창조했고, 인류—악보다 선을 선택할 수 있는 자유 의지를 가진 존재들—로 정점에 달했습니다. 우주적 전투는 인류의 선한 선택이 마침내 어둠을 물리칠 때 끝날 것입니다.",
    match_message_en="Your features carry the radiant wisdom of Ahura Mazda. There is a luminous, truthful quality to your presence—the look of one who embodies the cosmic principle of good.",
    match_message_ko="당신의 이목구비는 아후라 마즈다의 빛나는 지혜를 담고 있습니다. 당신의 존재에는 빛나고 진실한 품질이 있습니다—선의 우주적 원리를 구현하는 사람의 모습.",
    image_prompt="Radiant Persian deity of pure light and wisdom, winged sun disk symbol, cosmic light defeating darkness, Zoroastrian fire temple, supreme good presence",
    visual_description="Radiant luminous features of pure light, wise truthful eyes, supreme creator bearing, expression of cosmic goodness and eternal wisdom",
    aliases=["Ohrmazd", "Wise Lord", "Lord of Light"],
    era="Persian/Zoroastrian Mythology",
    related_characters=["angra_mainyu", "zoroaster"]
)


# FINNISH/NORDIC

VAINAMOINEN_DESC = CharacterDescription(
    id="vainamoinen",
    name_en="Väinämöinen",
    name_ko="배이내뫼이넨",
    tagline_en="The Eternal Sage, Singer of Creation",
    tagline_ko="영원한 현자, 창조의 가수",
    description_en="""Väinämöinen is the central hero of Finnish mythology and the Kalevala, the Finnish national epic. An ancient sage and powerful shaman, he was born old and already wise, having gestated in his mother's womb for 730 years before swimming to shore.

His greatest power is his singing—through magical songs, he can control nature, defeat enemies, and even create objects from thin air. He is credited with creating the kantele (Finnish harp) from the jawbone of a great pike and with numerous quests that shaped the world.

Väinämöinen represents the Finnish ideal of wisdom through age and experience. At the epic's end, he sails away in a copper boat, leaving but promising to return when Finland needs him again—an eternal archetype of the wise leader.""",
    description_ko="""배이내뫼이넨은 핀란드 신화와 핀란드 민족 서사시인 칼레발라의 중심 영웅입니다. 고대의 현자이자 강력한 샤먼으로, 어머니의 자궁에서 730년간 잉태된 후 해안으로 헤엄쳐 나와 이미 늙고 지혜롭게 태어났습니다.

그의 가장 큰 힘은 그의 노래입니다—마법의 노래를 통해 자연을 제어하고, 적을 물리치고, 심지어 무에서 물건을 창조할 수 있습니다. 그는 큰 파이크의 턱뼈로 칸텔레(핀란드 하프)를 만들고 세상을 형성한 수많은 탐구로 알려져 있습니다.

배이내뫼이넨은 나이와 경험을 통한 지혜의 핀란드적 이상을 대표합니다. 서사시의 끝에서 그는 구리 배를 타고 떠나며, 핀란드가 다시 필요로 할 때 돌아오겠다고 약속합니다—지혜로운 지도자의 영원한 원형.""",
    traits_en=["Ancient", "Wise", "Singing", "Magical", "Eternal"],
    traits_ko=["고대의", "지혜로운", "노래하는", "마법적인", "영원한"],
    story_en="When challenged to a singing contest by the young boastful Joukahainen, Väinämöinen sang him into a swamp up to his waist, then his chest, then his neck. Joukahainen offered everything—finally his sister Aino—to be freed. Such was the power of the old sage's song.",
    story_ko="젊고 허풍스러운 요우카하이넨에게 노래 대결을 도전받았을 때, 배이내뫼이넨은 그를 허리까지, 그 다음 가슴까지, 그 다음 목까지 늪에 빠지게 노래했습니다. 요우카하이넨은 모든 것—마침내 누이 아이노—을 풀려나기 위해 제안했습니다. 노현자의 노래의 힘은 그러했습니다.",
    match_message_en="Your features carry the ancient singing wisdom of Väinämöinen. There is an eternal, magical quality to your presence—the look of one whose words shape reality itself.",
    match_message_ko="당신의 이목구비는 배이내뫼이넨의 고대 노래하는 지혜를 담고 있습니다. 당신의 존재에는 영원하고 마법적인 품질이 있습니다—말로 현실 자체를 형성하는 사람의 모습.",
    image_prompt="Ancient Finnish sage with long white beard, playing kantele, singing magic into existence, northern forest setting, eternal wise presence",
    visual_description="Ancient wise features born old, deep knowing eyes, singing shaman bearing, expression of eternal wisdom and magical creative power",
    aliases=["Old Steadfast", "Suvetär's Son"],
    era="Finnish Mythology (Kalevala)",
    related_characters=["ilmarinen", "lemminkainen", "louhi"]
)


# JAPANESE (Additional)

ONI_DESC = CharacterDescription(
    id="oni",
    name_en="Oni",
    name_ko="오니",
    tagline_en="Demonic Ogres, Enforcers of Hell",
    tagline_ko="악마적 도깨비, 지옥의 집행자",
    description_en="""Oni are the demonic ogres of Japanese folklore, fearsome beings with horns, wild hair, and skin of red, blue, or other unnatural colors. They carry iron clubs (kanabō) and are associated with thunder, disaster, disease, and punishment.

In Buddhist tradition, oni serve as torturers in the various hells, punishing sinners according to their crimes. In folklore, they may be mountain-dwelling monsters who raid villages, kidnap people, or cause natural disasters. However, some oni can be converted to Buddhism and become protective guardians.

The festival of Setsubun involves driving out oni by throwing beans and shouting "Oni wa soto! Fuku wa uchi!" (Demons out! Fortune in!). Oni represent the forces of chaos and destruction that must be periodically expelled to maintain order and good fortune.""",
    description_ko="""오니는 일본 민간 전승의 악마적 도깨비로, 뿔, 거친 머리카락, 빨간색, 파란색 또는 다른 부자연스러운 색의 피부를 가진 두려운 존재입니다. 그들은 쇠몽둥이(카나보)를 들고 천둥, 재앙, 질병, 처벌과 연관됩니다.

불교 전통에서 오니는 다양한 지옥에서 고문자 역할을 하며, 죄인들을 그들의 죄에 따라 처벌합니다. 민간 전승에서 그들은 마을을 습격하고, 사람을 납치하거나, 자연 재해를 일으키는 산에 사는 괴물일 수 있습니다. 그러나 일부 오니는 불교로 개종하여 보호 수호자가 될 수 있습니다.

세츠분 축제는 콩을 던지고 "오니와 소토! 후쿠와 우치!"(도깨비는 밖으로! 복은 안으로!)라고 외치며 오니를 쫓아내는 것을 포함합니다. 오니는 질서와 행운을 유지하기 위해 주기적으로 추방되어야 하는 혼돈과 파괴의 힘을 대표합니다.""",
    traits_en=["Fearsome", "Powerful", "Chaotic", "Punishing", "Transformable"],
    traits_ko=["두려운", "강력한", "혼란스러운", "처벌하는", "변형 가능한"],
    story_en="The hero Momotarō traveled to Onigashima (Demon Island) with his animal companions to defeat the oni who had been terrorizing the land. After a fierce battle, the oni king surrendered, returned their stolen treasure, and promised never to do evil again.",
    story_ko="영웅 모모타로는 동물 동료들과 함께 땅을 공포에 떨게 하던 오니를 물리치기 위해 오니가시마(도깨비 섬)로 여행했습니다. 치열한 전투 끝에 오니 왕은 항복하고, 훔친 보물을 돌려주고, 다시는 악을 행하지 않겠다고 약속했습니다.",
    match_message_en="Your features carry the fierce power of the Oni. There is a fearsome, transformative quality to your presence—the look of one who embodies chaos but can be turned to protection.",
    match_message_ko="당신의 이목구비는 오니의 맹렬한 힘을 담고 있습니다. 당신의 존재에는 두렵고 변형적인 품질이 있습니다—혼돈을 구현하지만 보호로 전환될 수 있는 사람의 모습.",
    image_prompt="Fearsome Japanese demon ogre with horns and colored skin, iron club, traditional Oni aesthetic, powerful chaotic presence, both terrifying and potentially redeemable",
    visual_description="Fearsome demonic features with horns, fierce wild eyes, powerful chaotic bearing, expression of destructive force and potential transformation",
    aliases=["Japanese Demon", "Ogre", "Yokai"],
    era="Japanese Mythology/Folklore",
    related_characters=["momotaro", "raijin"]
)


# SOUTHEAST ASIAN

GARUDA_DESC = CharacterDescription(
    id="garuda",
    name_en="Garuda",
    name_ko="가루다",
    tagline_en="King of Birds, Mount of Vishnu",
    tagline_ko="새의 왕, 비슈누의 탈 것",
    description_en="""Garuda is the legendary king of birds in Hindu and Buddhist mythology, a divine eagle-like being who serves as the mount (vahana) of the god Vishnu. He is depicted with a golden body, red wings, a white face, and an eagle's beak.

Born from an egg, Garuda's mother was enslaved by her sister's naga (serpent) children. To free her, he was tasked with stealing amrita (the nectar of immortality) from the gods. He succeeded, defeating gods and breaking through supernatural barriers, earning Vishnu's respect and the boon of immortality.

Garuda is the eternal enemy of nagas, representing the cosmic conflict between sky and earth, eagle and serpent. He is the national symbol of Indonesia and Thailand, embodying speed, power, and martial prowess. His name means "the devourer" as he consumes the serpents of ignorance.""",
    description_ko="""가루다는 힌두교와 불교 신화에서 새의 전설적인 왕으로, 비슈누 신의 탈 것(바하나) 역할을 하는 신성한 독수리 같은 존재입니다. 금색 몸, 빨간 날개, 흰 얼굴, 독수리 부리를 가진 모습으로 묘사됩니다.

알에서 태어난 가루다의 어머니는 언니의 나가(뱀) 자식들에게 노예가 되었습니다. 그녀를 풀어주기 위해, 그는 신들로부터 암리타(불멸의 감로)를 훔치는 과제를 받았습니다. 그는 신들을 물리치고 초자연적 장벽을 뚫고 성공하여 비슈누의 존경과 불멸의 축복을 얻었습니다.

가루다는 나가의 영원한 적으로, 하늘과 땅, 독수리와 뱀 사이의 우주적 충돌을 대표합니다. 그는 인도네시아와 태국의 국가 상징으로, 속도, 힘, 무예를 구현합니다. 그의 이름은 무지의 뱀들을 삼키기 때문에 "삼키는 자"를 의미합니다.""",
    traits_en=["Powerful", "Loyal", "Swift", "Divine", "Serpent-enemy"],
    traits_ko=["강력한", "충성스러운", "빠른", "신성한", "뱀의 적"],
    story_en="To steal amrita, Garuda had to pass through spinning wheels of fire, fight the gods, and overcome the naga guardians. He succeeded in everything. Indra's thunderbolt could not penetrate him. He then offered the amrita to free his mother—and Vishnu, impressed by his power and devotion, made him immortal and his vehicle.",
    story_ko="암리타를 훔치기 위해, 가루다는 회전하는 불의 바퀴를 통과하고, 신들과 싸우고, 나가 수호자들을 이겨야 했습니다. 그는 모든 것에 성공했습니다. 인드라의 번개도 그를 관통할 수 없었습니다. 그런 다음 그는 어머니를 풀어주기 위해 암리타를 제공했고—비슈누는 그의 힘과 헌신에 감명받아 그를 불멸로 만들고 자신의 탈 것으로 삼았습니다.",
    match_message_en="Your features carry the divine might of Garuda. There is a swift, powerful quality to your presence—the look of one who serves the highest and defeats the lowest.",
    match_message_ko="당신의 이목구비는 가루다의 신성한 힘을 담고 있습니다. 당신의 존재에는 빠르고 강력한 품질이 있습니다—가장 높은 것을 섬기고 가장 낮은 것을 물리치는 사람의 모습.",
    image_prompt="Majestic eagle-like divine being with golden body and red wings, carrying Vishnu, defeating serpents, Southeast Asian aesthetic, royal bird of heaven",
    visual_description="Majestic eagle-like features, fierce loyal eyes, divine mount bearing, expression of swift power and unwavering devotion",
    aliases=["King of Birds", "Vahan of Vishnu", "Garuna"],
    era="Hindu-Buddhist Mythology",
    related_characters=["vishnu", "naga"]
)


# ARTHURIAN/BRITISH

MERLIN_DESC = CharacterDescription(
    id="merlin",
    name_en="Merlin",
    name_ko="멀린",
    tagline_en="The Arch-Mage, Architect of Camelot",
    tagline_ko="대마법사, 카멜롯의 설계자",
    description_en="""Merlin is the legendary wizard of Arthurian legend, perhaps the most famous sorcerer in Western literature. Said to be born of a mortal woman and an otherworldly spirit, he possessed prophetic abilities and powers over nature, time, and transformation.

He orchestrated the rise of King Arthur—from engineering Arthur's birth through Uther's deception, to placing the sword in the stone, to guiding the young king's early reign. Merlin built Stonehenge, created the Round Table, and foresaw both the glory and fall of Camelot.

His wisdom was legendary but could not protect him from love. The Lady of the Lake (or Nimue) learned his secrets and used them to trap him forever in a cave, a crystal prison, or beneath a stone—his power turned against him by the one he loved.""",
    description_ko="""멀린은 아서왕 전설의 전설적인 마법사로, 아마도 서양 문학에서 가장 유명한 마법사일 것입니다. 필멸의 여인과 이세계 영의 사이에서 태어났다고 하며, 자연, 시간, 변신에 대한 예언 능력과 힘을 가졌습니다.

그는 아서 왕의 부상을 조율했습니다—유터의 속임을 통한 아서의 탄생 설계부터, 돌에 검을 꽂는 것까지, 젊은 왕의 초기 통치를 인도하는 것까지. 멀린은 스톤헨지를 건설하고, 원탁을 만들고, 카멜롯의 영광과 몰락 모두를 예견했습니다.

그의 지혜는 전설적이었지만 사랑으로부터 그를 보호할 수 없었습니다. 호수의 여인(또는 니무에)이 그의 비밀을 배우고 그것을 사용하여 그를 동굴, 수정 감옥, 또는 돌 아래에 영원히 가뒀습니다—그가 사랑한 자에 의해 그의 힘이 그에게 돌려졌습니다.""",
    traits_en=["Wise", "Magical", "Prophetic", "Architecting", "Tragic"],
    traits_ko=["지혜로운", "마법적인", "예언적인", "설계하는", "비극적인"],
    story_en="Merlin foresaw his own imprisonment but could not prevent it. When Nimue asked him to teach her to create an unbreakable prison, he knew she would use it against him—yet loved her too much to refuse. He willingly walked into his eternal trap.",
    story_ko="멀린은 자신의 투옥을 예견했지만 막을 수 없었습니다. 니무에가 깨지지 않는 감옥을 만드는 법을 가르쳐달라고 했을 때, 그는 그녀가 그것을 자신에게 사용할 것을 알았지만—거부하기엔 그녀를 너무 사랑했습니다. 그는 기꺼이 영원한 함정으로 들어갔습니다.",
    match_message_en="Your features carry the profound magic of Merlin. There is a prophetic, architecting quality to your presence—the look of one who shapes destiny but cannot escape their own.",
    match_message_ko="당신의 이목구비는 멀린의 심오한 마법을 담고 있습니다. 당신의 존재에는 예언적이고 설계하는 품질이 있습니다—운명을 형성하지만 자신의 운명은 피할 수 없는 사람의 모습.",
    image_prompt="Ancient wizard with long white beard and staff, stars and prophecy in eyes, Stonehenge and Round Table imagery, trapped by love, legendary sage presence",
    visual_description="Ancient wise features, prophetic knowing eyes seeing past and future, wizard's bearing, expression of profound wisdom and tragic acceptance",
    aliases=["Myrddin", "Emrys", "The Prophet"],
    era="Arthurian Legend",
    related_characters=["arthur", "nimue", "morgan_le_fay"]
)


# Dictionary of World Mythology descriptions
WORLD_MYTHOLOGY_DESCRIPTIONS = {
    # African
    "anansi": ANANSI_DESC,
    "shango": SHANGO_DESC,
    "mami_wata": MAMI_WATA_DESC,
    # Polynesian
    "maui": MAUI_DESC,
    "pele": PELE_DESC,
    # Native American
    "coyote": COYOTE_DESC,
    "white_buffalo_woman": WHITE_BUFFALO_WOMAN_DESC,
    # Celtic
    "morrigan": MORRIGAN_DESC,
    "cu_chulainn": CU_CHULAINN_DESC,
    # Mesopotamian
    "inanna": INANNA_DESC,
    "gilgamesh": GILGAMESH_DESC,
    # Mesoamerican
    "quetzalcoatl": QUETZALCOATL_DESC,
    # Slavic
    "baba_yaga": BABA_YAGA_DESC,
    # Australian Aboriginal
    "rainbow_serpent": RAINBOW_SERPENT_DESC,
    # Persian/Zoroastrian
    "ahura_mazda": AHURA_MAZDA_DESC,
    # Finnish
    "vainamoinen": VAINAMOINEN_DESC,
    # Japanese (Additional)
    "oni": ONI_DESC,
    # Southeast Asian
    "garuda": GARUDA_DESC,
    # Arthurian
    "merlin": MERLIN_DESC,
}
