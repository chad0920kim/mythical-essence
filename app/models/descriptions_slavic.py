"""
Slavic Mythology Character Descriptions
Contains detailed descriptions for major Slavic mythological figures
"""
from .descriptions import CharacterDescription


PERUN_DESC = CharacterDescription(
    id="perun",
    name_en="Perun",
    name_ko="페룬",
    tagline_en="God of Thunder, Lightning, and Justice",
    tagline_ko="천둥, 번개, 정의의 신",
    description_en="""Perun is the supreme god of the ancient Slavic pantheon, ruler of thunder, lightning, and the sky. Like Zeus or Thor, he wields thunderbolts against the forces of chaos and evil, maintaining cosmic order throughout the Slavic lands.

As the god of war and warriors, Perun was worshipped by princes and soldiers before battle. He was associated with the oak tree, and his temples often stood in sacred oak groves. Oaths sworn by Perun were considered the most sacred and binding.

Perun's eternal enemy was Veles, the god of the underworld and cattle. Their cosmic battle—Perun striking from the sky, Veles hiding in trees and water—represented the eternal struggle between order and chaos, sky and earth, the living and the dead.""",
    description_ko="""페룬은 고대 슬라브 판테온의 최고신으로, 천둥, 번개, 하늘의 지배자입니다. 제우스나 토르처럼, 그는 혼돈과 악의 세력에 맞서 번개를 휘두르며, 슬라브 땅 전역에 우주적 질서를 유지합니다.

전쟁과 전사들의 신으로서, 페룬은 전투 전에 왕자와 군인들에게 숭배받았습니다. 그는 참나무와 연관되었으며, 그의 신전은 종종 신성한 참나무 숲에 세워졌습니다. 페룬의 이름으로 한 맹세는 가장 신성하고 구속력 있는 것으로 여겨졌습니다.

페룬의 영원한 적은 지하세계와 가축의 신인 벨레스였습니다. 그들의 우주적 전투—하늘에서 치는 페룬, 나무와 물에 숨는 벨레스—는 질서와 혼돈, 하늘과 땅, 산 자와 죽은 자 사이의 영원한 투쟁을 상징했습니다.""",
    traits_en=["Thunderous", "Just", "Martial", "Supreme", "Cosmic"],
    traits_ko=["천둥 같은", "공정한", "전투적인", "최고의", "우주적인"],
    story_en="When Veles stole Perun's cattle (or wife, or son—the myth varies), Perun pursued him across the world, striking with lightning. Veles hid in the water, in trees, among cattle, but could not escape. The spring thunderstorms are their eternal battle renewed.",
    story_ko="벨레스가 페룬의 가축(또는 아내, 또는 아들—신화마다 다름)을 훔쳤을 때, 페룬은 번개를 치며 세상을 가로질러 그를 추격했습니다. 벨레스는 물속에, 나무에, 가축 사이에 숨었지만 탈출할 수 없었습니다. 봄의 뇌우는 그들의 영원한 전투가 새롭게 되는 것입니다.",
    match_message_en="You carry the thunderous authority of Perun. There is a just, martial quality to your presence—the look of one who strikes against chaos and defends cosmic order.",
    match_message_ko="당신은 페룬의 천둥 같은 권위를 지니고 있습니다. 당신의 존재에는 공정하고 전투적인 품질이 있습니다—혼돈에 맞서 치고 우주적 질서를 지키는 사람의 모습.",
    image_prompt="Powerful Slavic thunder god with axe or lightning bolts, great warrior's form, oak leaves in hair, storm clouds gathering, ancient eastern European aesthetic",
    visual_description="Powerful commanding features, fierce sky-blue eyes like lightning, warrior's martial bearing, expression of divine justice and thunderous power",
    aliases=["Perkūnas", "Piorun"],
    era="Slavic Antiquity",
    related_characters=["veles", "svarog"]
)

VELES_DESC = CharacterDescription(
    id="veles",
    name_en="Veles",
    name_ko="벨레스",
    tagline_en="God of the Underworld, Cattle, and Magic",
    tagline_ko="지하세계, 가축, 마법의 신",
    description_en="""Veles is the Slavic god of the underworld, earth, water, and cattle. Where Perun ruled the sky, Veles governed everything below—the souls of the dead, the riches of the earth, and the mysterious forces of magic and prophecy.

Despite being Perun's eternal adversary, Veles was not an evil god but represented the necessary opposite to heavenly order. He was the patron of musicians, merchants, and wizards. Oaths of trade and commerce were sworn by Veles, for he knew the secrets hidden in the earth.

Veles was depicted as a serpent or dragon, sometimes as a bear, dwelling in the roots of the World Tree that Perun's eagles guarded above. His domain included the ancestors, making him essential to Slavic ancestor worship and the connection between the living and dead.""",
    description_ko="""벨레스는 지하세계, 땅, 물, 가축의 슬라브 신입니다. 페룬이 하늘을 다스렸다면, 벨레스는 아래의 모든 것—죽은 자의 영혼, 땅의 부, 마법과 예언의 신비로운 힘—을 다스렸습니다.

페룬의 영원한 적수임에도 불구하고, 벨레스는 사악한 신이 아니라 천상의 질서에 필요한 반대를 상징했습니다. 그는 음악가, 상인, 마법사들의 수호자였습니다. 무역과 상업의 맹세는 벨레스의 이름으로 행해졌는데, 그가 땅에 숨겨진 비밀을 알았기 때문입니다.

벨레스는 뱀이나 용으로, 때로는 곰으로 묘사되었으며, 페룬의 독수리들이 위에서 지키는 세계수의 뿌리에 거주했습니다. 그의 영역에는 조상들이 포함되어, 슬라브 조상 숭배와 산 자와 죽은 자 사이의 연결에 필수적이었습니다.""",
    traits_en=["Chthonic", "Wealthy", "Magical", "Mysterious", "Ancestral"],
    traits_ko=["지하의", "부유한", "마법적인", "신비로운", "조상의"],
    story_en="Merchants would swear oaths by Veles before trading, for he knew all that was hidden in the earth—including the worth of goods and the truth of hearts. Breaking an oath to Veles brought misfortune in this life and the next.",
    story_ko="상인들은 거래 전에 벨레스의 이름으로 맹세했는데, 그가 땅에 숨겨진 모든 것—물품의 가치와 마음의 진실을 포함하여—을 알았기 때문입니다. 벨레스에 대한 맹세를 어기면 이생과 다음 생에 불행이 찾아왔습니다.",
    match_message_en="You possess the mysterious depth of Veles. There is a magical, earthly quality to your presence—the look of one who knows the secrets hidden below the surface.",
    match_message_ko="당신은 벨레스의 신비로운 깊이를 지니고 있습니다. 당신의 존재에는 마법적이고 세속적인 품질이 있습니다—표면 아래 숨겨진 비밀을 아는 사람의 모습.",
    image_prompt="Mysterious Slavic chthonic god with serpent features, surrounded by cattle and treasure, roots of world tree, ancient knowing eyes",
    visual_description="Deep mysterious features, knowing serpentine eyes, earthy mysterious bearing, expression of hidden wisdom and underworld power",
    aliases=["Volos", "Weles"],
    era="Slavic Antiquity",
    related_characters=["perun", "morana"]
)

MORANA_DESC = CharacterDescription(
    id="morana",
    name_en="Morana",
    name_ko="모라나",
    tagline_en="Goddess of Winter, Death, and Rebirth",
    tagline_ko="겨울, 죽음, 재탄생의 여신",
    description_en="""Morana is the Slavic goddess of winter and death, but also of the cycle of rebirth that follows. She embodies the harsh winter that kills but also clears the way for spring's renewal. Her domain is the necessary destruction that precedes all new growth.

Every year at the end of winter, Slavic people would create an effigy of Morana, carry it through the village, and then drown or burn it. This ritual death of winter welcomed spring and the return of life, showing that Morana's death was always temporary.

Morana is often depicted as a beautiful but cold woman dressed in white, or as a terrifying hag. These dual aspects represent winter's beauty and danger, and the way death appears different depending on our perspective.""",
    description_ko="""모라나는 겨울과 죽음의 슬라브 여신이지만, 뒤따르는 재탄생의 순환의 여신이기도 합니다. 그녀는 죽이지만 또한 봄의 갱신을 위한 길을 열어주는 혹독한 겨울을 구현합니다. 그녀의 영역은 모든 새로운 성장에 앞서는 필요한 파괴입니다.

매년 겨울이 끝날 때, 슬라브 사람들은 모라나의 허수아비를 만들어 마을을 행진한 다음, 물에 빠뜨리거나 태웠습니다. 이 겨울의 의식적 죽음은 봄과 생명의 귀환을 환영했으며, 모라나의 죽음이 항상 일시적임을 보여주었습니다.

모라나는 종종 흰옷을 입은 아름답지만 차가운 여인으로, 또는 무시무시한 노파로 묘사됩니다. 이러한 이중적 측면은 겨울의 아름다움과 위험, 그리고 우리의 관점에 따라 죽음이 다르게 보이는 방식을 나타냅니다.""",
    traits_en=["Cold", "Cyclical", "Beautiful", "Deadly", "Renewing"],
    traits_ko=["차가운", "순환적인", "아름다운", "치명적인", "갱신하는"],
    story_en="Each spring, villagers would make a straw figure of Morana and parade it through the streets before throwing it into a river. As it floated away, they sang songs welcoming spring, knowing that Morana would return with next winter's first snow.",
    story_ko="매년 봄, 마을 사람들은 모라나의 짚 인형을 만들어 거리를 행진한 후 강에 던졌습니다. 그것이 떠내려가는 동안, 그들은 봄을 환영하는 노래를 불렀고, 모라나가 다음 겨울의 첫 눈과 함께 돌아올 것을 알고 있었습니다.",
    match_message_en="You embody the cold beauty of Morana. There is a cyclical, transforming quality to your presence—the look of one who understands that death brings rebirth.",
    match_message_ko="당신은 모라나의 차가운 아름다움을 구현합니다. 당신의 존재에는 순환적이고 변화시키는 품질이 있습니다—죽음이 재탄생을 가져온다는 것을 이해하는 사람의 모습.",
    image_prompt="Beautiful pale goddess in white winter robes, frost and snowflakes around her, cold but beautiful features, winter landscape, dual nature visible",
    visual_description="Cold beautiful features, icy blue eyes, deathly pale yet beautiful bearing, expression of winter's necessary cruelty and hidden renewal",
    aliases=["Marzanna", "Morena", "Mara"],
    era="Slavic Antiquity",
    related_characters=["veles", "lada"]
)

SVAROG_DESC = CharacterDescription(
    id="svarog",
    name_en="Svarog",
    name_ko="스바로그",
    tagline_en="God of the Sky, Sun, and Fire",
    tagline_ko="하늘, 태양, 불의 신",
    description_en="""Svarog is the Slavic god of the celestial fire, the sky, and smithcraft. His name relates to words meaning "bright" and "heaven," and he was considered the father of the sun god Dazhbog (or Dažbog) and the fire god Svarozhich.

As the divine smith, Svarog forged the sun and placed it in the sky. He gave humanity the knowledge of metallurgy, teaching them to forge plows for agriculture and weapons for defense. Civilization itself was his gift to the Slavic peoples.

Some sources suggest Svarog was the supreme god before Perun rose to prominence. He represents the creative, civilizing aspect of divinity—the fire that doesn't just destroy but transforms, the heat that forges tools from raw ore.""",
    description_ko="""스바로그는 천상의 불, 하늘, 대장장이 기술의 슬라브 신입니다. 그의 이름은 "밝은"과 "하늘"을 의미하는 단어들과 관련되며, 태양신 다지보그와 불의 신 스바로지치의 아버지로 여겨졌습니다.

신성한 대장장이로서, 스바로그는 태양을 단조하여 하늘에 놓았습니다. 그는 인류에게 금속 가공 기술을 주어, 농업을 위한 쟁기와 방어를 위한 무기를 단조하도록 가르쳤습니다. 문명 그 자체가 슬라브 민족들에 대한 그의 선물이었습니다.

일부 자료는 페룬이 두각을 나타내기 전에 스바로그가 최고신이었다고 제시합니다. 그는 신성의 창조적이고 문명화하는 측면—파괴만 하는 것이 아니라 변형시키는 불, 날것의 광석에서 도구를 단조하는 열기—을 상징합니다.""",
    traits_en=["Creative", "Celestial", "Forging", "Civilizing", "Fiery"],
    traits_ko=["창조적인", "천상의", "단조하는", "문명화하는", "불같은"],
    story_en="Svarog forged the sun and threw it across the sky, giving light and warmth to the world. Then he descended to earth and taught humanity to use fire for forging—turning them from animals into people who could shape their own destiny.",
    story_ko="스바로그는 태양을 단조하여 하늘을 가로질러 던져, 세상에 빛과 온기를 주었습니다. 그런 다음 그는 땅으로 내려와 인류에게 단조를 위해 불을 사용하도록 가르쳤습니다—그들을 동물에서 자신의 운명을 형성할 수 있는 사람들로 바꾸어 놓았습니다.",
    match_message_en="You radiate the creative fire of Svarog. There is a forging, civilizing quality to your presence—the look of one who creates and transforms through skill and flame.",
    match_message_ko="당신은 스바로그의 창조적 불을 발산합니다. 당신의 존재에는 단조하고 문명화하는 품질이 있습니다—기술과 불꽃을 통해 창조하고 변형시키는 사람의 모습.",
    image_prompt="Powerful Slavic smith god at cosmic forge, creating the sun, fire and stars around him, ancient wisdom with creative power",
    visual_description="Strong creator features, bright fiery eyes, smith's powerful bearing, expression of cosmic creation and civilizing fire",
    aliases=["Swarożyc", "Zuarasici"],
    era="Slavic Antiquity",
    related_characters=["perun", "dazhbog"]
)

LADA_DESC = CharacterDescription(
    id="lada",
    name_en="Lada",
    name_ko="라다",
    tagline_en="Goddess of Love, Beauty, and Spring",
    tagline_ko="사랑, 아름다움, 봄의 여신",
    description_en="""Lada is the Slavic goddess of love, beauty, fertility, and spring. She represents the life-giving warmth that returns after Morana's winter, the renewal of love and passion that comes with the flowering season.

Young couples would pray to Lada for happy marriages and blessed unions. Songs invoking her name were sung at weddings and spring festivals, calling for her blessings of love, harmony, and fertility. She was the joy of spring personified.

Some scholars identify Lada with the wider Indo-European goddess of love and beauty. Whether historical or reconstructed, she embodies the Slavic celebration of love, youth, and the eternal return of spring's warmth and growth.""",
    description_ko="""라다는 사랑, 아름다움, 다산, 봄의 슬라브 여신입니다. 그녀는 모라나의 겨울 이후 돌아오는 생명을 주는 온기, 꽃피는 계절과 함께 오는 사랑과 열정의 갱신을 상징합니다.

젊은 커플들은 행복한 결혼과 축복받은 결합을 위해 라다에게 기도했습니다. 그녀의 이름을 부르는 노래는 결혼식과 봄 축제에서 불렸으며, 사랑, 조화, 다산의 축복을 불렀습니다. 그녀는 봄의 기쁨이 의인화된 것이었습니다.

일부 학자들은 라다를 더 넓은 인도유럽 사랑과 아름다움의 여신과 동일시합니다. 역사적이든 재구성된 것이든, 그녀는 사랑, 젊음, 그리고 봄의 온기와 성장의 영원한 귀환에 대한 슬라브인들의 축하를 구현합니다.""",
    traits_en=["Loving", "Beautiful", "Fertile", "Joyful", "Renewing"],
    traits_ko=["사랑스러운", "아름다운", "다산의", "기쁜", "갱신하는"],
    story_en="At spring festivals, young women would dance and sing songs to Lada, asking for love and happy marriages. The goddess was believed to bless those who honored her with the gift of finding their true love.",
    story_ko="봄 축제에서, 젊은 여성들은 춤을 추고 라다에게 노래를 불러 사랑과 행복한 결혼을 청했습니다. 여신은 그녀를 공경하는 사람들에게 진정한 사랑을 찾는 선물로 축복한다고 믿어졌습니다.",
    match_message_en="You radiate the spring beauty of Lada. There is a loving, joyful quality to your presence—the look of one who brings warmth and renewal wherever they go.",
    match_message_ko="당신은 라다의 봄의 아름다움을 발산합니다. 당신의 존재에는 사랑스럽고 기쁜 품질이 있습니다—가는 곳마다 온기와 갱신을 가져다주는 사람의 모습.",
    image_prompt="Beautiful Slavic spring goddess with flowers in hair, spring colors and warmth, joyful loving expression, flowering meadow background",
    visual_description="Beautiful youthful features, warm loving eyes, graceful fertile bearing, expression of spring's joy and love's renewal",
    aliases=["Lado", "Vesna"],
    era="Slavic Antiquity",
    related_characters=["morana", "svarog"]
)


# Export dictionary for registry
SLAVIC_DESCRIPTIONS: dict[str, CharacterDescription] = {
    "perun": PERUN_DESC,
    "veles": VELES_DESC,
    "morana": MORANA_DESC,
    "svarog": SVAROG_DESC,
    "lada": LADA_DESC,
}
