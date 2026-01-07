"""
Chinese Mythology and History - Character Descriptions
Contains descriptions for Chinese mythological and historical figures
"""
from .descriptions import CharacterDescription


# ============================================
# CHINESE MYTHOLOGICAL FIGURES
# ============================================

JADE_EMPEROR_DESC = CharacterDescription(
    id="jade_emperor",
    name_en="Jade Emperor",
    name_ko="옥황상제",
    tagline_en="Supreme Ruler of Heaven, King of All Gods",
    tagline_ko="하늘의 최고 통치자, 모든 신들의 왕",
    description_en="""The Jade Emperor is the supreme deity in Chinese folk religion and Taoism, ruling over heaven and all realms of existence. He governs the celestial bureaucracy that mirrors the earthly Chinese imperial court, with ministries overseeing every aspect of mortal and divine affairs.

From his Jade Palace, he presides over courts where the deeds of humans and gods are judged. His will shapes the cosmos, and even other great deities acknowledge his ultimate authority.

The Jade Emperor represents cosmic order through divine governance, the belief that heaven and earth mirror each other, and the ultimate source of moral judgment.""",
    description_ko="""옥황상제는 중국 민간 신앙과 도교에서 최고의 신으로, 하늘과 모든 존재의 영역을 다스립니다. 그는 지상의 중국 황실 조정을 반영하는 천상의 관료제를 통치하며, 필멸자와 신성한 일의 모든 측면을 감독하는 부서가 있습니다.

옥궁에서 그는 인간과 신들의 행위가 심판되는 법정을 주재합니다. 그의 뜻이 우주를 형성하고, 다른 위대한 신들조차 그의 궁극적인 권위를 인정합니다.

옥황상제는 신성한 통치를 통한 우주의 질서, 하늘과 땅이 서로를 반영한다는 믿음, 그리고 도덕적 심판의 궁극적 원천을 대표합니다.""",
    traits_en=["Supreme", "Just", "Governing", "Celestial", "Ordering"],
    traits_ko=["최고의", "공정한", "통치하는", "천상의", "질서 잡는"],
    story_en="The Jade Emperor earned his position through countless eons of cultivation. When chaos threatened the cosmos, he alone had the merit and wisdom to restore order. All the gods gathered and acknowledged him as supreme ruler of heaven.",
    story_ko="옥황상제는 셀 수 없이 오랜 세월의 수행을 통해 그의 지위를 얻었습니다. 혼돈이 우주를 위협했을 때, 그만이 질서를 회복할 공덕과 지혜를 가지고 있었습니다. 모든 신들이 모여 그를 하늘의 최고 통치자로 인정했습니다.",
    match_message_en="Your features carry the supreme authority of the Jade Emperor. There is celestial governance in your appearance—the look of one who maintains order across all realms.",
    match_message_ko="당신의 이목구비는 옥황상제의 최고 권위를 담고 있습니다. 당신의 외모에는 천상의 통치력이 있습니다—모든 영역에서 질서를 유지하는 사람의 모습.",
    image_prompt="Majestic Chinese deity in imperial dragon robes seated on jade throne, long white beard, celestial palace with clouds, expression of supreme benevolent authority, traditional Chinese artistic style",
    visual_description="Regal aged features, wise benevolent eyes, long white beard, appearance of supreme celestial authority",
    aliases=["玉皇大帝", "Yu Huang", "The August Jade Emperor"],
    era="Chinese Mythology",
    related_characters=["queen_mother", "erlang_shen", "nezha"]
)

SUN_WUKONG_DESC = CharacterDescription(
    id="sun_wukong",
    name_en="Sun Wukong",
    name_ko="손오공",
    tagline_en="The Monkey King, Great Sage Equal to Heaven",
    tagline_ko="원숭이 왕, 제천대성",
    description_en="""Sun Wukong is the legendary Monkey King, born from a stone egg fertilized by the elements. Through rigorous cultivation, he gained incredible powers: the ability to transform into 72 different forms, cloud-somersaulting that covers vast distances, and mastery of his magical staff Ruyi Jingu Bang.

His defiance of heaven made him one of mythology's greatest rebels—he ate the peaches of immortality, erased his name from the Book of Life and Death, and challenged the entire celestial army before Buddha trapped him under a mountain for 500 years.

Sun Wukong represents the untameable spirit of rebellion, the power of self-cultivation, and ultimately the redemption found in service to a worthy cause.""",
    description_ko="""손오공은 전설적인 원숭이 왕으로, 원소들에 의해 수정된 돌알에서 태어났습니다. 엄격한 수행을 통해 그는 믿을 수 없는 능력을 얻었습니다: 72가지 다른 형태로 변신하는 능력, 광대한 거리를 커버하는 근두운, 그리고 마법의 지팡이 여의봉의 숙달.

그의 하늘에 대한 반항은 그를 신화의 가장 위대한 반역자 중 하나로 만들었습니다—그는 불로장생 복숭아를 먹고, 생사부에서 자신의 이름을 지우고, 부처가 500년 동안 산 아래 가두기 전까지 전체 천상의 군대에 도전했습니다.

손오공은 길들일 수 없는 반항 정신, 자기 수양의 힘, 그리고 궁극적으로 가치 있는 대의에 봉사하는 데서 발견되는 구원을 대표합니다.""",
    traits_en=["Rebellious", "Powerful", "Transforming", "Defiant", "Redeemed"],
    traits_ko=["반항적인", "강력한", "변신하는", "도전적인", "구원받은"],
    story_en="After 500 years under the mountain, Sun Wukong was freed to protect the monk Xuanzang on his journey west to retrieve Buddhist scriptures. Through this pilgrimage, the wild Monkey King learned discipline and earned enlightenment.",
    story_ko="산 아래서 500년 후, 손오공은 불교 경전을 가져오기 위한 서쪽 여행에서 승려 현장을 보호하기 위해 풀려났습니다. 이 순례를 통해 야생의 원숭이 왕은 규율을 배우고 깨달음을 얻었습니다.",
    match_message_en="Your features carry the defiant spirit of Sun Wukong. There is untamed power in your appearance—the look of one who challenges all limits and transforms obstacles into opportunities.",
    match_message_ko="당신의 이목구비는 손오공의 도전적인 정신을 담고 있습니다. 당신의 외모에는 길들여지지 않은 힘이 있습니다—모든 한계에 도전하고 장애물을 기회로 바꾸는 사람의 모습.",
    image_prompt="Legendary monkey warrior with golden fur and armor, wielding extending staff Ruyi Jingu Bang, cloud-riding, mischievous powerful expression, dynamic action pose, Chinese mythological style",
    visual_description="Simian yet noble features, bright mischievous eyes, powerful athletic presence, expression of irrepressible defiance and cunning",
    aliases=["齊天大聖", "Monkey King", "Great Sage"],
    era="Chinese Mythology",
    related_characters=["xuanzang", "zhu_bajie", "jade_emperor", "guanyin"]
)

GUANYIN_DESC = CharacterDescription(
    id="guanyin",
    name_en="Guanyin",
    name_ko="관음보살",
    tagline_en="Goddess of Mercy and Compassion",
    tagline_ko="자비와 연민의 여신",
    description_en="""Guanyin is the bodhisattva of compassion, one of the most beloved deities in Chinese Buddhism. Though she could enter nirvana, she vowed to remain in the world until all sentient beings are freed from suffering, hearing the cries of all who call her name.

Her compassion is unlimited and unconditional—she appears in whatever form will best help those who pray to her, whether as a beautiful woman, a monk, or any other guise. She is often depicted with many arms and eyes, symbolizing her ability to reach all who suffer.

Guanyin represents the ideal of selfless compassion, the bodhisattva path of helping others before oneself, and the comfort that comes from knowing someone hears our prayers.""",
    description_ko="""관음보살은 자비의 보살로, 중국 불교에서 가장 사랑받는 신 중 하나입니다. 그녀는 열반에 들어갈 수 있었지만, 모든 유정이 고통에서 벗어날 때까지 세상에 남아 그녀의 이름을 부르는 모든 이의 울음을 듣겠다고 서원했습니다.

그녀의 자비는 무한하고 무조건적입니다—그녀는 기도하는 이들을 가장 잘 도울 수 있는 어떤 형태로든 나타납니다, 아름다운 여인이든, 승려이든, 다른 어떤 모습이든. 그녀는 종종 많은 팔과 눈으로 묘사되어, 고통받는 모든 이에게 닿을 수 있는 능력을 상징합니다.

관음보살은 이타적 자비의 이상, 자신보다 다른 이들을 먼저 돕는 보살의 길, 그리고 누군가 우리의 기도를 듣는다는 것을 아는 데서 오는 위안을 대표합니다.""",
    traits_en=["Compassionate", "Merciful", "Selfless", "Hearing", "Saving"],
    traits_ko=["자비로운", "인자한", "이타적인", "경청하는", "구원하는"],
    story_en="When the princess Miaoshan was condemned to death by her father for refusing to marry, she attained enlightenment at the moment of execution. She later sacrificed her eyes and arms to save her father from illness, becoming Guanyin with a thousand arms and eyes.",
    story_ko="묘선 공주가 결혼을 거부하여 아버지에게 사형을 선고받았을 때, 그녀는 처형의 순간에 깨달음을 얻었습니다. 그녀는 나중에 아버지를 병에서 구하기 위해 눈과 팔을 희생했고, 천 개의 팔과 눈을 가진 관음이 되었습니다.",
    match_message_en="Your features carry the boundless compassion of Guanyin. There is mercy in your appearance—the look of one who hears suffering and responds with selfless love.",
    match_message_ko="당신의 이목구비는 관음보살의 무한한 자비를 담고 있습니다. 당신의 외모에는 자비가 있습니다—고통을 듣고 이타적인 사랑으로 응답하는 사람의 모습.",
    image_prompt="Serene Chinese goddess in white robes holding willow branch and vase, thousand arms radiating compassion, lotus throne, peaceful transcendent expression, Buddhist artistic style",
    visual_description="Serene beautiful features, infinitely compassionate eyes, graceful peaceful presence, expression of one who hears all suffering",
    aliases=["觀音", "Avalokitesvara", "Goddess of Mercy"],
    era="Chinese Buddhism",
    related_characters=["buddha", "sun_wukong", "xuanzang"]
)

ERLANG_SHEN_DESC = CharacterDescription(
    id="erlang_shen",
    name_en="Erlang Shen",
    name_ko="이랑신",
    tagline_en="Three-Eyed Warrior God",
    tagline_ko="삼목 전사신",
    description_en="""Erlang Shen is the warrior deity known for his third truth-seeing eye and his mastery of 73 transformations—one more than Sun Wukong. He is the nephew of the Jade Emperor and commands the celestial armies, accompanied by his loyal hound Xiaotian.

His third eye can see through all illusions and deceptions, making him the perfect divine enforcer. He was the only deity who could match Sun Wukong in single combat during the Monkey King's rebellion against heaven.

Erlang Shen represents martial excellence, unwavering duty, and the piercing vision that sees through falsehood to truth.""",
    description_ko="""이랑신은 진실을 보는 제3의 눈과 73가지 변신 숙달로 알려진 전사신입니다—손오공보다 하나 더 많습니다. 그는 옥황상제의 조카이며 충직한 사냥개 소천견과 함께 천상의 군대를 지휘합니다.

그의 제3의 눈은 모든 환상과 속임수를 꿰뚫어 볼 수 있어, 완벽한 신성한 집행자로 만듭니다. 그는 원숭이 왕의 하늘에 대한 반란 중 일대일 전투에서 손오공과 대등하게 맞설 수 있었던 유일한 신이었습니다.

이랑신은 무예의 탁월함, 흔들리지 않는 의무, 그리고 거짓을 꿰뚫어 진실을 보는 날카로운 시력을 대표합니다.""",
    traits_en=["Warrior", "Truth-seeing", "Loyal", "Skilled", "Disciplined"],
    traits_ko=["전사", "진실을 보는", "충직한", "숙련된", "규율 있는"],
    story_en="When Sun Wukong rebelled against heaven, Erlang Shen was sent to capture him. The two engaged in an epic battle of transformations, each matching the other's forms. Though neither could prevail through combat alone, Erlang Shen's persistence helped trap the Monkey King.",
    story_ko="손오공이 하늘에 반란을 일으켰을 때, 이랑신이 그를 포획하기 위해 보내졌습니다. 둘은 각각 상대의 형태를 맞추며 변신의 대전투를 벌였습니다. 전투만으로는 어느 쪽도 이길 수 없었지만, 이랑신의 끈기가 원숭이 왕을 가두는 데 도움이 되었습니다.",
    match_message_en="Your features carry the piercing vision of Erlang Shen. There is warrior's truth in your appearance—the look of one who sees through deception and serves with unwavering dedication.",
    match_message_ko="당신의 이목구비는 이랑신의 꿰뚫는 시력을 담고 있습니다. 당신의 외모에는 전사의 진실이 있습니다—속임수를 꿰뚫어 보고 흔들리지 않는 헌신으로 봉사하는 사람의 모습.",
    image_prompt="Warrior deity with third eye on forehead, holding three-pointed lance, celestial hound at side, transformation ability visible, stern dedicated expression, Chinese mythological warrior style",
    visual_description="Handsome fierce features, third eye of truth, intense disciplined gaze, warrior bearing of one who never fails in duty",
    aliases=["二郎神", "Yang Jian", "Three-Eyed God"],
    era="Chinese Mythology",
    related_characters=["jade_emperor", "sun_wukong", "nezha"]
)

NEZHA_DESC = CharacterDescription(
    id="nezha",
    name_en="Nezha",
    name_ko="나타",
    tagline_en="Third Lotus Prince, Divine Child Warrior",
    tagline_ko="삼태자, 신성한 아이 전사",
    description_en="""Nezha is the divine child warrior, born after three years and six months in the womb, emerging as a fully formed boy who could speak and fight. He wields the Universe Ring, the Fire-Tipped Spear, and rides the Wind Fire Wheels.

His story is one of rebellion against unjust authority—after killing the Dragon King's son in self-defense, Nezha sacrificed himself to save his parents from divine punishment, then was reborn from a lotus flower with a reconstructed body.

Nezha represents youthful defiance of injustice, the willingness to sacrifice for family, and the eternal spirit that cannot be destroyed.""",
    description_ko="""나타는 신성한 아이 전사로, 자궁에서 3년 6개월 후에 태어났으며, 말하고 싸울 수 있는 완전히 형성된 소년으로 나타났습니다. 그는 건곤권, 화첨창을 휘두르고 풍화륜을 탑니다.

그의 이야기는 부당한 권위에 대한 반항입니다—정당방위로 용왕의 아들을 죽인 후, 나타는 신성한 벌로부터 부모를 구하기 위해 자신을 희생했고, 그런 다음 재구성된 몸으로 연꽃에서 다시 태어났습니다.

나타는 불의에 대한 젊은 저항, 가족을 위해 희생하려는 의지, 그리고 파괴될 수 없는 영원한 영혼을 대표합니다.""",
    traits_en=["Youthful", "Rebellious", "Sacrificing", "Reborn", "Fierce"],
    traits_ko=["젊은", "반항적인", "희생하는", "재탄생한", "사나운"],
    story_en="When the Dragon King demanded Nezha's death, the boy cut his own flesh to return it to his mother and carved his bones to return them to his father. His teacher Taiyi Zhenren then rebuilt Nezha's body from lotus roots, more powerful than before.",
    story_ko="용왕이 나타의 죽음을 요구했을 때, 소년은 어머니에게 돌려주기 위해 자신의 살을 자르고 아버지에게 돌려주기 위해 뼈를 깎았습니다. 그의 스승 태을진인은 그 후 나타의 몸을 연꽃 뿌리로 재건했고, 이전보다 더 강력해졌습니다.",
    match_message_en="Your features carry the fierce youth of Nezha. There is immortal defiance in your appearance—the look of one who fights injustice and rises again no matter what is sacrificed.",
    match_message_ko="당신의 이목구비는 나타의 사나운 젊음을 담고 있습니다. 당신의 외모에는 불멸의 저항이 있습니다—불의에 맞서 싸우고 무엇이 희생되든 다시 일어나는 사람의 모습.",
    image_prompt="Divine child warrior riding flaming wheels in sky, wielding spear and ring, lotus flowers around body, youthful fierce expression, dynamic flying pose, Chinese mythological action style",
    visual_description="Youthful fierce features, blazing determined eyes, eternal child appearance, expression of indomitable spirit",
    aliases=["哪吒", "Third Lotus Prince", "Marshal of the Central Altar"],
    era="Chinese Mythology",
    related_characters=["erlang_shen", "dragon_king", "taiyi_zhenren"]
)

DRAGON_KING_DESC = CharacterDescription(
    id="dragon_king",
    name_en="Dragon King",
    name_ko="용왕",
    tagline_en="Lord of Waters and Seas",
    tagline_ko="물과 바다의 군주",
    description_en="""The Dragon Kings are the divine rulers of the four seas, controlling all waters, weather, and aquatic life. The most prominent is Ao Guang, the Dragon King of the Eastern Sea, who commands rainfall and can cause floods or droughts.

Living in magnificent underwater palaces of crystal and coral, the Dragon Kings govern vast bureaucracies of aquatic spirits. They answer to the Jade Emperor and can be petitioned by humans for rain during droughts.

The Dragon Kings represent the power of water in all its forms, the divine control of weather, and the relationship between human prayer and natural forces.""",
    description_ko="""용왕들은 사해의 신성한 통치자로, 모든 물, 날씨, 수생 생물을 통제합니다. 가장 유명한 것은 동해 용왕 오광으로, 강우를 지휘하고 홍수나 가뭄을 일으킬 수 있습니다.

수정과 산호로 된 웅장한 수중 궁전에서 살며, 용왕들은 수생 영혼들의 광대한 관료제를 통치합니다. 그들은 옥황상제에게 응답하고 가뭄 중에 인간들에게 비를 위해 청원받을 수 있습니다.

용왕들은 모든 형태의 물의 힘, 날씨에 대한 신성한 통제, 그리고 인간의 기도와 자연력 사이의 관계를 대표합니다.""",
    traits_en=["Watery", "Powerful", "Temperamental", "Ruling", "Ancient"],
    traits_ko=["물의", "강력한", "변덕스러운", "통치하는", "고대의"],
    story_en="When Nezha killed Ao Bing, son of the Dragon King, Ao Guang rose from the sea in fury. He demanded justice from the Jade Emperor and called floods upon the land until Nezha's sacrifice appeased his wrath.",
    story_ko="나타가 용왕의 아들 오병을 죽였을 때, 오광은 분노하여 바다에서 솟아올랐습니다. 그는 옥황상제에게 정의를 요구하고 나타의 희생이 그의 분노를 달랠 때까지 땅에 홍수를 불렀습니다.",
    match_message_en="Your features carry the oceanic power of the Dragon King. There is aquatic majesty in your appearance—the look of one who commands the waters and controls the rains.",
    match_message_ko="당신의 이목구비는 용왕의 바다 같은 힘을 담고 있습니다. 당신의 외모에는 물의 위엄이 있습니다—물을 지휘하고 비를 통제하는 사람의 모습.",
    image_prompt="Majestic dragon-headed deity in royal underwater palace, scales and robes merging, surrounded by aquatic spirits, controlling waves and storms, expression of ancient power, Chinese dragon style",
    visual_description="Draconic noble features, deep ocean eyes, scales and majesty blended, expression of ancient watery power",
    aliases=["龍王", "Ao Guang", "Lord of the Eastern Sea"],
    era="Chinese Mythology",
    related_characters=["jade_emperor", "nezha", "sun_wukong"]
)

QUEEN_MOTHER_DESC = CharacterDescription(
    id="queen_mother",
    name_en="Queen Mother of the West",
    name_ko="서왕모",
    tagline_en="Goddess of Immortality and the Peaches",
    tagline_ko="불멸과 복숭아의 여신",
    description_en="""The Queen Mother of the West (Xiwangmu) is one of the oldest and most powerful deities in Chinese mythology. She rules over the western paradise on Mount Kunlun and is keeper of the peaches of immortality, which ripen once every three thousand years.

Her garden holds the secrets of eternal life, and her banquets for the gods are legendary. All who eat her peaches gain immortality—which is why Sun Wukong's theft of them was such a cosmic crime.

The Queen Mother represents the mysteries of immortality, feminine divine power independent of male deities, and the rewards that await those who cultivate virtue over lifetimes.""",
    description_ko="""서왕모는 중국 신화에서 가장 오래되고 강력한 신 중 하나입니다. 그녀는 곤륜산의 서방 낙원을 다스리며 3천 년에 한 번 익는 불로장생 복숭아의 수호자입니다.

그녀의 정원은 영생의 비밀을 담고 있으며, 신들을 위한 그녀의 연회는 전설적입니다. 그녀의 복숭아를 먹는 모든 이는 불멸을 얻습니다—그래서 손오공이 그것을 훔친 것이 그토록 우주적인 범죄였습니다.

서왕모는 불멸의 신비, 남성 신들과 독립적인 여성적 신성한 힘, 그리고 여러 생에 걸쳐 덕을 쌓는 자들을 기다리는 보상을 대표합니다.""",
    traits_en=["Immortal", "Powerful", "Mysterious", "Feminine", "Rewarding"],
    traits_ko=["불멸의", "강력한", "신비로운", "여성적인", "보상하는"],
    story_en="Every three thousand years, the Queen Mother holds a grand banquet when her peaches ripen. All the gods are invited to partake of immortality. When Sun Wukong consumed the peaches and disrupted this sacred gathering, it was one of his gravest offenses against heaven.",
    story_ko="3천 년마다 서왕모는 복숭아가 익으면 대연회를 엽니다. 모든 신들이 불멸을 나누도록 초대받습니다. 손오공이 복숭아를 먹고 이 신성한 모임을 방해했을 때, 이것은 하늘에 대한 그의 가장 큰 범죄 중 하나였습니다.",
    match_message_en="Your features carry the ageless power of the Queen Mother. There is immortal grace in your appearance—the look of one who holds the secrets of eternal life.",
    match_message_ko="당신의 이목구비는 서왕모의 늙지 않는 힘을 담고 있습니다. 당신의 외모에는 불멸의 우아함이 있습니다—영생의 비밀을 가진 사람의 모습.",
    image_prompt="Elegant ancient goddess in flowing robes at Mount Kunlun paradise, surrounded by peach trees and phoenixes, expression of timeless power and grace, Chinese immortal style",
    visual_description="Ageless beautiful features, eyes holding millennia of wisdom, graceful eternal presence, expression of one who grants immortality",
    aliases=["西王母", "Xiwangmu", "Royal Mother of the West"],
    era="Chinese Mythology",
    related_characters=["jade_emperor", "sun_wukong", "chang_e"]
)

CHANG_E_DESC = CharacterDescription(
    id="chang_e",
    name_en="Chang'e",
    name_ko="항아",
    tagline_en="Goddess of the Moon",
    tagline_ko="달의 여신",
    description_en="""Chang'e is the goddess who lives on the moon, forever separated from her husband Houyi, the divine archer. She ascended to the moon after consuming an elixir of immortality, and now resides in the Moon Palace with only a jade rabbit for company.

Her story is one of the most poignant in Chinese mythology—immortality gained at the cost of eternal loneliness. She is celebrated during the Mid-Autumn Festival, when families gather to gaze at the moon and think of distant loved ones.

Chang'e represents the bittersweet nature of immortality, the beauty and loneliness of the moon, and the enduring bonds of love across impossible distances.""",
    description_ko="""항아는 달에 사는 여신으로, 신성한 궁수인 남편 후예와 영원히 분리되어 있습니다. 그녀는 불로장생 영약을 마신 후 달로 승천했고, 지금은 옥토끼만을 벗삼아 월궁에 거주합니다.

그녀의 이야기는 중국 신화에서 가장 가슴 아픈 것 중 하나입니다—영원한 외로움의 대가로 얻은 불멸. 그녀는 가족들이 모여 달을 바라보고 멀리 있는 사랑하는 이들을 생각하는 중추절에 기념됩니다.

항아는 불멸의 씁쓸한 본성, 달의 아름다움과 외로움, 그리고 불가능한 거리를 넘어서는 사랑의 지속적인 유대를 대표합니다.""",
    traits_en=["Lonely", "Beautiful", "Immortal", "Regretful", "Luminous"],
    traits_ko=["외로운", "아름다운", "불멸의", "후회하는", "빛나는"],
    story_en="Houyi obtained the elixir of immortality from the Queen Mother, intending to share it with Chang'e. But Chang'e consumed it all—whether by accident, greed, or to prevent it from falling into wrong hands—and floated up to the moon, where she remains to this day.",
    story_ko="후예는 서왕모에게서 불로장생 영약을 얻어 항아와 나누려 했습니다. 하지만 항아가 전부 마셨습니다—실수로든, 탐욕으로든, 또는 잘못된 손에 떨어지는 것을 막기 위해서든—그리고 달로 떠올라, 오늘날까지 그곳에 남아 있습니다.",
    match_message_en="Your features carry the luminous beauty of Chang'e. There is moonlit solitude in your appearance—the look of one who embodies both the beauty and melancholy of eternal separation.",
    match_message_ko="당신의 이목구비는 항아의 빛나는 아름다움을 담고 있습니다. 당신의 외모에는 달빛 같은 고독이 있습니다—영원한 분리의 아름다움과 우울함 모두를 구현하는 사람의 모습.",
    image_prompt="Beautiful goddess on the moon in flowing silk robes, jade rabbit companion, Moon Palace in background, full moon glow, expression of beautiful eternal loneliness, Chinese celestial style",
    visual_description="Ethereal beautiful features, luminous sad eyes, moonlit complexion, expression of immortal loneliness and grace",
    aliases=["嫦娥", "Moon Goddess", "Lady of the Moon"],
    era="Chinese Mythology",
    related_characters=["houyi", "queen_mother", "jade_rabbit"]
)


# ============================================
# CHINESE HISTORICAL FIGURES
# ============================================

GUAN_YU_EXTENDED_DESC = CharacterDescription(
    id="guan_yu",
    name_en="Guan Yu",
    name_ko="관우",
    tagline_en="God of War, Brotherhood, and Righteousness",
    tagline_ko="전쟁, 형제애, 의리의 신",
    description_en="""Guan Yu was a general during the Three Kingdoms period who became so legendary for his loyalty and martial prowess that he was deified as the God of War. His red face, long beard, and green robe became iconic, as did his weapon—the Green Dragon Crescent Blade.

He swore a sacred oath of brotherhood with Liu Bei and Zhang Fei in the Peach Garden, a bond he honored until death and beyond. His loyalty was so absolute that he refused wealth and position from Cao Cao, preferring to risk everything to return to his sworn brother.

Guan Yu represents unwavering loyalty, martial honor, and the sacred nature of sworn brotherhood that transcends personal gain.""",
    description_ko="""관우는 삼국시대의 장군으로, 충성과 무예로 너무나 전설적이 되어 전쟁의 신으로 신격화되었습니다. 그의 붉은 얼굴, 긴 수염, 녹색 의복은 상징적이 되었고, 그의 무기인 청룡언월도도 마찬가지입니다.

그는 도원에서 유비, 장비와 신성한 형제의 맹세를 했고, 이 유대를 죽음과 그 이후까지 지켰습니다. 그의 충성은 너무나 절대적이어서 조조의 부와 지위를 거부하고 맹세한 형제에게 돌아가기 위해 모든 것을 걸었습니다.

관우는 흔들리지 않는 충성, 무인의 명예, 그리고 개인적 이득을 초월하는 맹세한 형제애의 신성한 본성을 대표합니다.""",
    traits_en=["Loyal", "Righteous", "Martial", "Honorable", "Deified"],
    traits_ko=["충성스러운", "의로운", "무예의", "명예로운", "신격화된"],
    story_en="Captured by Cao Cao, Guan Yu was offered everything to change allegiance. He accepted temporarily only to protect Liu Bei's wives. The moment he learned Liu Bei's location, he passed through five passes and killed six generals to return—a journey immortalized in legend.",
    story_ko="조조에게 포로가 된 관우는 충성을 바꾸면 모든 것을 주겠다는 제안을 받았습니다. 그는 유비의 아내들을 보호하기 위해서만 일시적으로 수락했습니다. 유비의 위치를 알게 된 순간, 그는 다섯 관문을 통과하고 여섯 장수를 죽여 돌아갔습니다—전설로 영원히 남은 여정.",
    match_message_en="Your features carry the righteous strength of Guan Yu. There is sworn brotherhood in your appearance—the look of one whose loyalty can never be bought and whose word is absolutely sacred.",
    match_message_ko="당신의 이목구비는 관우의 의로운 힘을 담고 있습니다. 당신의 외모에는 맹세한 형제애가 있습니다—충성을 결코 살 수 없고 말이 절대적으로 신성한 사람의 모습.",
    image_prompt="Legendary warrior with red face and long black beard, wearing green robe, holding Green Dragon Crescent Blade, expression of unwavering loyalty and martial honor, Chinese historical epic style",
    visual_description="Red-faced heroic features, fierce loyal eyes, magnificent long beard, expression of absolute righteousness",
    aliases=["關羽", "Lord Guan", "God of War"],
    era="Three Kingdoms Period",
    related_characters=["liu_bei", "zhang_fei", "cao_cao", "zhuge_liang"]
)

ZHUGE_LIANG_DESC = CharacterDescription(
    id="zhuge_liang",
    name_en="Zhuge Liang",
    name_ko="제갈량",
    tagline_en="The Sleeping Dragon, Supreme Strategist",
    tagline_ko="와룡, 최고의 전략가",
    description_en="""Zhuge Liang is revered as the greatest strategist in Chinese history, whose brilliance shaped the Three Kingdoms period. Known as the Sleeping Dragon before his fame, he served Liu Bei with absolute devotion and created strategies that seemed almost supernatural in their foresight.

His inventions included the repeating crossbow and the wooden ox transport. His masterpiece, the Longzhong Plan, outlined how to restore the Han dynasty. Even his death was strategic—his corpse was displayed to frighten away the pursuing enemy.

Zhuge Liang represents the power of intellect over force, the duty of the advisor to serve the righteous ruler, and the principle that wisdom can shape destiny.""",
    description_ko="""제갈량은 중국 역사에서 가장 위대한 전략가로 숭앙받으며, 그의 탁월함이 삼국시대를 형성했습니다. 유명해지기 전 와룡으로 알려진 그는 절대적인 헌신으로 유비를 섬기고 거의 초자연적으로 보이는 선견지명의 전략을 만들었습니다.

그의 발명품에는 연발석궁과 목우유마가 포함됩니다. 그의 걸작인 융중대책은 한나라를 회복하는 방법을 개략적으로 설명했습니다. 그의 죽음조차 전략적이었습니다—추격하는 적을 겁주기 위해 시신이 전시되었습니다.

제갈량은 힘보다 지성의 힘, 의로운 군주를 섬기는 참모의 의무, 그리고 지혜가 운명을 형성할 수 있다는 원칙을 대표합니다.""",
    traits_en=["Brilliant", "Strategic", "Devoted", "Inventive", "Wise"],
    traits_ko=["탁월한", "전략적인", "헌신적인", "창의적인", "지혜로운"],
    story_en="At the Battle of Red Cliffs, Zhuge Liang 'borrowed' 100,000 arrows from the enemy by sending straw boats into the fog. When Sun Quan's forces fired upon what they thought were invaders, Zhuge Liang collected their arrows and returned with exactly what he promised.",
    story_ko="적벽대전에서 제갈량은 안개 속으로 짚배를 보내 적에게서 10만 개의 화살을 '빌렸습니다'. 손권의 군대가 침략자라고 생각한 것에 발사했을 때, 제갈량은 그들의 화살을 모아 약속한 것 정확히 가지고 돌아왔습니다.",
    match_message_en="Your features carry the brilliant wisdom of Zhuge Liang. There is strategic depth in your appearance—the look of one who sees twelve moves ahead and shapes events through superior intellect.",
    match_message_ko="당신의 이목구비는 제갈량의 탁월한 지혜를 담고 있습니다. 당신의 외모에는 전략적 깊이가 있습니다—열두 수 앞을 보고 뛰어난 지성으로 사건을 형성하는 사람의 모습.",
    image_prompt="Elegant scholar in white robes with feather fan, serene confident expression, Chinese strategic maps in background, stars overhead suggesting divination, traditional Chinese scholarly style",
    visual_description="Elegant intelligent features, deep calculating eyes, serene confident expression, appearance of supreme intellect",
    aliases=["諸葛亮", "Kongming", "The Sleeping Dragon"],
    era="Three Kingdoms Period",
    related_characters=["liu_bei", "guan_yu", "zhang_fei", "cao_cao"]
)

QIN_SHI_HUANG_DESC = CharacterDescription(
    id="qin_shi_huang",
    name_en="Qin Shi Huang",
    name_ko="진시황",
    tagline_en="First Emperor of Unified China",
    tagline_ko="통일 중국의 첫 번째 황제",
    description_en="""Qin Shi Huang was the first emperor to unify China, ending centuries of warring states through military conquest and brilliant administration. He standardized weights, measures, currency, and even the width of cart axles, creating the foundation of Chinese civilization.

His greatest monuments endure: the Great Wall, which connected existing fortifications into a single defense system, and his tomb guarded by the Terracotta Army—thousands of life-sized soldiers meant to protect him in the afterlife.

Qin Shi Huang represents the transformative power of absolute authority, the creation of unified civilization from chaos, and the eternal human quest for immortality.""",
    description_ko="""진시황은 중국을 처음으로 통일한 황제로, 군사적 정복과 탁월한 행정으로 수백 년의 전국시대를 끝냈습니다. 그는 도량형, 화폐, 심지어 수레 축의 너비까지 표준화하여 중국 문명의 기초를 만들었습니다.

그의 가장 위대한 기념물은 지속됩니다: 기존 요새를 단일 방어 체계로 연결한 만리장성, 그리고 사후세계에서 그를 보호하기 위한 수천 명의 실물 크기 병사—병마용으로 지켜지는 그의 무덤.

진시황은 절대 권력의 변혁적 힘, 혼돈에서 통일 문명의 창조, 그리고 불멸을 향한 영원한 인간의 추구를 대표합니다.""",
    traits_en=["Unifying", "Absolute", "Building", "Immortality-seeking", "Transforming"],
    traits_ko=["통일하는", "절대적인", "건설하는", "불멸을 추구하는", "변혁적인"],
    story_en="Obsessed with immortality, Qin Shi Huang sent expeditions to find the elixir of life and consumed mercury pills believing they would grant eternal life. He died during such a quest, and his advisors hid his death until a successor could be installed.",
    story_ko="불멸에 집착한 진시황은 불로장생약을 찾기 위해 탐험대를 보내고 영생을 준다고 믿으며 수은 알약을 먹었습니다. 그는 그러한 탐구 중에 죽었고, 그의 참모들은 후계자가 세워질 때까지 그의 죽음을 숨겼습니다.",
    match_message_en="Your features carry the unifying will of Qin Shi Huang. There is empire-building power in your appearance—the look of one who transforms chaos into order through absolute determination.",
    match_message_ko="당신의 이목구비는 진시황의 통일하는 의지를 담고 있습니다. 당신의 외모에는 제국 건설의 힘이 있습니다—절대적인 결단으로 혼돈을 질서로 변혁하는 사람의 모습.",
    image_prompt="Imperial figure in black dragon robes, Great Wall and Terracotta Army in background, expression of absolute authority and immortality-seeking determination, ancient Chinese imperial style",
    visual_description="Imperial commanding features, piercing absolute gaze, expression of one who shaped civilization and sought eternity",
    aliases=["秦始皇", "First Emperor", "Ying Zheng"],
    era="Qin Dynasty",
    related_characters=["li_si", "meng_tian"]
)

CONFUCIUS_EXTENDED_DESC = CharacterDescription(
    id="confucius",
    name_en="Confucius",
    name_ko="공자",
    tagline_en="Supreme Sage, Teacher of Ten Thousand Generations",
    tagline_ko="지성, 만세의 스승",
    description_en="""Confucius is the most influential philosopher in Chinese history, whose teachings on ethics, governance, and social harmony shaped East Asian civilization for over two millennia. He emphasized ritual propriety, filial piety, and the cultivation of virtue as the foundation of a harmonious society.

Though he held office briefly and wandered seeking a ruler who would implement his ideas, his true impact came through teaching. His disciples compiled his sayings into the Analerta, which became the cornerstone of Chinese education.

Confucius represents the power of moral education, the ideal of the gentleman-scholar, and the belief that society can be transformed through virtuous leadership and ethical cultivation.""",
    description_ko="""공자는 중국 역사에서 가장 영향력 있는 철학자로, 윤리, 통치, 사회적 조화에 대한 가르침이 2천 년 이상 동아시아 문명을 형성했습니다. 그는 예, 효, 그리고 조화로운 사회의 기초로서 덕의 함양을 강조했습니다.

그는 잠시 관직에 있었고 자신의 아이디어를 실행할 군주를 찾아 방랑했지만, 그의 진정한 영향은 가르침을 통해 왔습니다. 그의 제자들은 그의 말을 논어로 편찬했고, 이는 중국 교육의 초석이 되었습니다.

공자는 도덕 교육의 힘, 군자-학자의 이상, 그리고 덕있는 리더십과 윤리적 함양을 통해 사회가 변혁될 수 있다는 믿음을 대표합니다.""",
    traits_en=["Wise", "Teaching", "Ethical", "Humane", "Cultivating"],
    traits_ko=["지혜로운", "가르치는", "윤리적인", "인간적인", "함양하는"],
    story_en="When asked to summarize his teaching in one word, Confucius replied: 'Reciprocity (恕)—do not do to others what you would not want done to yourself.' This Golden Rule became foundational to Chinese moral philosophy.",
    story_ko="그의 가르침을 한 단어로 요약해 달라는 요청에 공자는 대답했습니다: '서(恕)—자신이 당하기 싫은 것을 남에게 하지 마라.' 이 황금률은 중국 도덕 철학의 기초가 되었습니다.",
    match_message_en="Your features carry the sagely wisdom of Confucius. There is moral cultivation in your appearance—the look of one who teaches by example and transforms society through ethical living.",
    match_message_ko="당신의 이목구비는 공자의 성인같은 지혜를 담고 있습니다. 당신의 외모에는 도덕적 함양이 있습니다—모범으로 가르치고 윤리적 삶을 통해 사회를 변혁하는 사람의 모습.",
    image_prompt="Elderly sage in traditional scholarly robes, surrounded by disciples, scrolls and bamboo strips, expression of benevolent wisdom, traditional Chinese scholarly painting style",
    visual_description="Wise aged features, benevolent intelligent eyes, scholarly dignified bearing, expression of supreme moral wisdom",
    aliases=["孔子", "Kong Qiu", "The Supreme Sage"],
    era="Spring and Autumn Period",
    related_characters=["mencius", "laozi", "zhuangzi"]
)

LAOZI_DESC = CharacterDescription(
    id="laozi",
    name_en="Laozi",
    name_ko="노자",
    tagline_en="Founder of Taoism, Sage of the Tao",
    tagline_ko="도교의 창시자, 도의 성인",
    description_en="""Laozi is the legendary founder of Taoism, said to have written the Tao Te Ching before riding an ox westward and disappearing into the mountains. His philosophy of the Tao—the Way—emphasizes naturalness, simplicity, and wu wei (non-action or effortless action).

In contrast to Confucius's emphasis on social ritual and governance, Laozi taught that the highest wisdom lies in following nature's patterns, that water's softness overcomes stone's hardness, and that the sage rules best by not ruling.

Laozi represents the mystery of the Tao, the wisdom of yielding and flowing, and the spiritual path that leads away from society into harmony with nature.""",
    description_ko="""노자는 도교의 전설적인 창시자로, 소를 타고 서쪽으로 가서 산으로 사라지기 전에 도덕경을 썼다고 합니다. 그의 도의 철학은 자연스러움, 단순함, 그리고 무위(행동하지 않음 또는 노력 없는 행동)를 강조합니다.

사회적 의례와 통치에 대한 공자의 강조와 대조적으로, 노자는 최고의 지혜는 자연의 패턴을 따르는 데 있으며, 물의 부드러움이 돌의 단단함을 이기고, 성인은 다스리지 않음으로써 가장 잘 다스린다고 가르쳤습니다.

노자는 도의 신비, 양보하고 흐르는 지혜, 그리고 사회를 떠나 자연과 조화를 이루는 영적 길을 대표합니다.""",
    traits_en=["Mysterious", "Natural", "Yielding", "Simple", "Flowing"],
    traits_ko=["신비로운", "자연적인", "양보하는", "단순한", "흐르는"],
    story_en="Laozi served as keeper of the royal archives before becoming disillusioned with society. At the western gate, the guardian begged him to write down his wisdom before leaving forever. Laozi composed the 5,000 characters of the Tao Te Ching, then rode into the west and was never seen again.",
    story_ko="노자는 사회에 환멸을 느끼기 전에 왕실 문서고의 관리자로 일했습니다. 서문에서 관문지기가 영원히 떠나기 전에 지혜를 써달라고 간청했습니다. 노자는 도덕경의 5천 자를 지었고, 서쪽으로 타고 가서 다시는 보이지 않았습니다.",
    match_message_en="Your features carry the mysterious wisdom of Laozi. There is natural flow in your appearance—the look of one who follows the Tao and finds strength in yielding to nature's way.",
    match_message_ko="당신의 이목구비는 노자의 신비로운 지혜를 담고 있습니다. 당신의 외모에는 자연스러운 흐름이 있습니다—도를 따르고 자연의 길에 양보함으로써 힘을 찾는 사람의 모습.",
    image_prompt="Ancient sage riding ox into misty mountains, long white beard flowing, simple robes, expression of serene wisdom and mystery, traditional Chinese Taoist painting style",
    visual_description="Ancient serene features, deep mysterious eyes, flowing beard and hair, expression of one who has glimpsed the eternal Tao",
    aliases=["老子", "Li Er", "The Old Master"],
    era="Spring and Autumn Period",
    related_characters=["confucius", "zhuangzi", "liezi"]
)

MU_LAN_DESC = CharacterDescription(
    id="mu_lan",
    name_en="Hua Mulan",
    name_ko="화목란",
    tagline_en="Legendary Warrior, Filial Daughter",
    tagline_ko="전설적인 전사, 효녀",
    description_en="""Hua Mulan is the legendary woman warrior who disguised herself as a man to take her aged father's place in the army. For twelve years she fought alongside male soldiers, earning honor and promotions through her skill and courage while keeping her true identity secret.

Her story, recorded in the Ballad of Mulan, celebrates filial piety—love for parents that leads to extraordinary sacrifice. When offered high office after the war, she asked only to return home to her family.

Mulan represents the power of filial love, the capability of women to equal men in traditionally male domains, and the Chinese ideal that virtue knows no gender.""",
    description_ko="""화목란은 연로한 아버지를 대신하여 군대에 들어가기 위해 남장을 한 전설적인 여전사입니다. 12년 동안 그녀는 남성 병사들과 함께 싸우며 진짜 정체를 숨기면서 기술과 용기로 명예와 승진을 얻었습니다.

목란사에 기록된 그녀의 이야기는 효—특별한 희생으로 이어지는 부모에 대한 사랑을 찬양합니다. 전쟁 후 높은 관직을 제안받았을 때, 그녀는 오직 가족에게 돌아가기만을 요청했습니다.

목란은 효의 힘, 전통적으로 남성의 영역에서 여성이 남성과 동등할 수 있는 능력, 그리고 덕은 성별을 알지 못한다는 중국의 이상을 대표합니다.""",
    traits_en=["Filial", "Brave", "Disguised", "Capable", "Humble"],
    traits_ko=["효도하는", "용감한", "변장한", "유능한", "겸손한"],
    story_en="When Mulan returned home after twelve years of war, she changed from armor into her old dress. Her comrades who came to visit were shocked to discover their brother-in-arms was a woman. They had fought beside her for years and never suspected.",
    story_ko="목란이 12년간의 전쟁 후 집에 돌아왔을 때, 그녀는 갑옷에서 옛 드레스로 갈아입었습니다. 방문하러 온 전우들은 그들의 동료가 여자였다는 것을 알고 충격을 받았습니다. 그들은 수년간 그녀 옆에서 싸웠지만 결코 의심하지 않았습니다.",
    match_message_en="Your features carry the brave devotion of Mulan. There is filial courage in your appearance—the look of one who would sacrifice everything for family and prove themselves in any arena.",
    match_message_ko="당신의 이목구비는 목란의 용감한 헌신을 담고 있습니다. 당신의 외모에는 효의 용기가 있습니다—가족을 위해 모든 것을 희생하고 어떤 분야에서든 자신을 증명하는 사람의 모습.",
    image_prompt="Woman warrior in ancient Chinese armor, sword drawn, expression of brave determination and hidden gentleness, dual image showing transformation from soldier to daughter, Chinese legendary hero style",
    visual_description="Strong yet gentle features, determined brave eyes, warrior bearing masking feminine grace, expression of filial courage",
    aliases=["花木蘭", "The Filial Warrior", "Lady General"],
    era="Northern Wei Dynasty (Legendary)",
    related_characters=["her_father", "the_khan"]
)


NUWA_DESC = CharacterDescription(
    id="nuwa",
    name_en="Nüwa",
    name_ko="여와",
    tagline_en="Creator Goddess, Repairer of Heaven",
    tagline_ko="창조 여신, 하늘을 수리한 자",
    description_en="""Nüwa is the creator goddess who shaped humanity from yellow clay, giving life to the first humans. When the pillar of heaven collapsed and the world fell into chaos, she melted five-colored stones to mend the sky and cut the legs from a giant tortoise to prop up the heavens.

Depicted with a human head and serpent body, she represents the primordial creative force that shaped existence. She is the mother of all humanity, whose compassion led her to repair creation when it threatened to collapse.

Nüwa represents divine feminine creation, the nurturing care that maintains the world, and the power to restore order from chaos.""",
    description_ko="""여와는 노란 점토로 인류를 빚어 최초의 인간에게 생명을 준 창조 여신입니다. 하늘의 기둥이 무너지고 세상이 혼돈에 빠졌을 때, 그녀는 오색 돌을 녹여 하늘을 수리하고 거대한 거북의 다리를 잘라 하늘을 받쳤습니다.

인간의 머리와 뱀의 몸으로 묘사되는 그녀는 존재를 형성한 원초적 창조력을 대표합니다. 그녀는 모든 인류의 어머니이며, 그녀의 자비가 창조가 붕괴될 위기에 처했을 때 그것을 수리하도록 이끌었습니다.

여와는 신성한 여성적 창조, 세상을 유지하는 양육하는 보살핌, 그리고 혼돈에서 질서를 회복하는 힘을 대표합니다.""",
    traits_en=["Creating", "Nurturing", "Repairing", "Motherly", "Primordial"],
    traits_ko=["창조하는", "양육하는", "수리하는", "어머니같은", "원초적인"],
    story_en="When the pillar of heaven cracked and fire and flood ravaged the earth, Nüwa gathered stones of five colors and melted them to patch the sky. She killed a great tortoise and used its legs as new pillars, then burned reeds to dam the floods. Order was restored.",
    story_ko="하늘의 기둥이 금이 가고 불과 홍수가 대지를 황폐화했을 때, 여와는 오색 돌을 모아 녹여 하늘을 깁고 큰 거북을 죽여 그 다리를 새 기둥으로 사용했으며, 갈대를 태워 홍수를 막았습니다. 질서가 회복되었습니다.",
    match_message_en="Your features carry the creative power of Nüwa. There is motherly restoration in your appearance—the look of one who creates life and repairs what is broken.",
    match_message_ko="당신의 이목구비는 여와의 창조적 힘을 담고 있습니다. 당신의 외모에는 어머니같은 회복이 있습니다—생명을 창조하고 깨진 것을 수리하는 사람의 모습.",
    image_prompt="Serpent-bodied goddess with human face, shaping humans from clay, five-colored stones above, expression of maternal creative power, Chinese primordial myth style",
    visual_description="Divine maternal features, creative nurturing eyes, serpentine grace, expression of primordial creative power",
    aliases=["女媧", "Creator Goddess"],
    era="Chinese Mythology",
    related_characters=["fuxi", "pangu", "jade_emperor"]
)

HOUYI_DESC = CharacterDescription(
    id="houyi",
    name_en="Houyi",
    name_ko="후예",
    tagline_en="Divine Archer, Shooter of Suns",
    tagline_ko="신성한 궁수, 태양을 쏜 자",
    description_en="""Houyi is the legendary archer who saved the world by shooting down nine of the ten suns that once scorched the earth. When all ten suns rose together, burning the world and killing crops, Houyi took his divine bow and shot them down one by one, leaving only one sun to light the sky.

His skill was unmatched—he could shoot a sparrow through the eye from a thousand paces. Yet his greatest tragedy was losing his wife Chang'e to the moon after she consumed their shared elixir of immortality.

Houyi represents heroic action in crisis, the burden of being savior and abandoned husband, and the bittersweet nature of heroism's rewards.""",
    description_ko="""후예는 한때 대지를 그을린 열 개의 태양 중 아홉 개를 쏘아 세상을 구한 전설적인 궁수입니다. 열 개의 태양이 모두 함께 떠올라 세상을 태우고 작물을 죽였을 때, 후예는 신성한 활을 들고 하나씩 쏘아 떨어뜨려, 하늘을 밝힐 태양 하나만 남겼습니다.

그의 실력은 비할 데 없었습니다—천 보 밖에서 참새의 눈을 쏠 수 있었습니다. 그러나 그의 가장 큰 비극은 아내 항아가 그들이 공유할 불로장생 영약을 마신 후 달로 잃은 것이었습니다.

후예는 위기 상황에서의 영웅적 행동, 구원자이자 버림받은 남편의 짐, 그리고 영웅심의 보상의 씁쓸한 본성을 대표합니다.""",
    traits_en=["Heroic", "Skilled", "Saving", "Tragic", "Abandoned"],
    traits_ko=["영웅적인", "숙련된", "구원하는", "비극적인", "버림받은"],
    story_en="When the ten suns rose together, even the immortals could not approach them. Houyi climbed the highest mountain and drew his bow. With nine shots, nine suns fell. The world was saved, but Houyi was exiled from heaven for killing the Sun Emperor's sons.",
    story_ko="열 개의 태양이 함께 떠올랐을 때, 신선들조차 그것들에 접근할 수 없었습니다. 후예는 가장 높은 산에 올라 활을 당겼습니다. 아홉 번의 사격으로 아홉 개의 태양이 떨어졌습니다. 세상은 구원받았지만, 후예는 태양 황제의 아들들을 죽인 죄로 천국에서 추방당했습니다.",
    match_message_en="Your features carry the heroic skill of Houyi. There is saving strength in your appearance—the look of one who takes impossible shots and bears the lonely burden of heroism.",
    match_message_ko="당신의 이목구비는 후예의 영웅적 기술을 담고 있습니다. 당신의 외모에는 구원하는 힘이 있습니다—불가능한 사격을 하고 영웅심의 외로운 짐을 지는 사람의 모습.",
    image_prompt="Muscular archer with divine bow aiming at blazing suns, nine fallen suns around, heroic determined expression, Chinese mythological hero style",
    visual_description="Strong heroic features, focused targeting eyes, archer's powerful presence, expression of tragic heroism",
    aliases=["后羿", "The Divine Archer"],
    era="Chinese Mythology",
    related_characters=["chang_e", "jade_emperor", "queen_mother"]
)

LU_DONGBIN_DESC = CharacterDescription(
    id="lu_dongbin",
    name_en="Lü Dongbin",
    name_ko="여동빈",
    tagline_en="Immortal Swordsman, Leader of the Eight Immortals",
    tagline_ko="불멸의 검객, 팔선의 수장",
    description_en="""Lü Dongbin is the most celebrated of the Eight Immortals, a scholar who achieved immortality through Taoist cultivation. He carries a magical sword that he uses to vanquish evil spirits and a fly-whisk that symbolizes his ability to fly through the air.

His path to immortality came through ten tests of character, each designed to prove his virtue. After passing, he became a wandering immortal who helps the worthy and punishes the wicked, often in disguise.

Lü Dongbin represents the Taoist path to transcendence, the scholarly warrior who masters both sword and scripture, and the immortal who remains engaged with the mortal world.""",
    description_ko="""여동빈은 팔선 중 가장 유명한 인물로, 도교 수행을 통해 불멸을 성취한 학자입니다. 그는 악령을 물리치는 마법의 검과 공중을 날 수 있는 능력을 상징하는 불자를 들고 다닙니다.

그의 불멸로 가는 길은 각각 그의 덕을 증명하도록 설계된 열 가지 인격 시험을 통해 왔습니다. 통과 후, 그는 자격 있는 자를 돕고 악인을 벌하는 방랑하는 신선이 되었으며, 종종 변장합니다.

여동빈은 초월에 이르는 도교의 길, 검과 경전 모두를 숙달한 학자-전사, 그리고 필멸자 세계와 계속 관계하는 신선을 대표합니다.""",
    traits_en=["Immortal", "Scholarly", "Sword-wielding", "Testing", "Helping"],
    traits_ko=["불멸의", "학자적인", "검을 휘두르는", "시험하는", "돕는"],
    story_en="Lü Dongbin was tested ten times before achieving immortality. In one test, a beautiful woman tried to seduce him; in another, he was offered great wealth. In each case, he remained true to virtue. Finally deemed worthy, he achieved transcendence and joined the Immortals.",
    story_ko="여동빈은 불멸을 성취하기 전에 열 번 시험받았습니다. 한 시험에서는 아름다운 여인이 그를 유혹하려 했고; 다른 시험에서는 큰 부를 제안받았습니다. 각 경우에서 그는 덕에 진실하게 남았습니다. 마침내 자격 있다고 여겨져 그는 초월을 달성하고 신선들에 합류했습니다.",
    match_message_en="Your features carry the cultivated wisdom of Lü Dongbin. There is immortal scholarly grace in your appearance—the look of one who has passed every test and achieved transcendence.",
    match_message_ko="당신의 이목구비는 여동빈의 수련된 지혜를 담고 있습니다. 당신의 외모에는 불멸의 학자적 우아함이 있습니다—모든 시험을 통과하고 초월을 달성한 사람의 모습.",
    image_prompt="Immortal Taoist sage with magical sword and fly-whisk, scholar's robes, clouds beneath feet, expression of cultivated wisdom and playful immortality, Chinese Taoist immortal style",
    visual_description="Refined scholarly features, eyes of tested virtue, elegant immortal bearing, expression of transcendent wisdom",
    aliases=["呂洞賓", "Leader of the Eight Immortals"],
    era="Tang Dynasty/Chinese Mythology",
    related_characters=["eight_immortals", "zhongli_quan", "laozi"]
)

ZHANG_FEI_DESC = CharacterDescription(
    id="zhang_fei",
    name_en="Zhang Fei",
    name_ko="장비",
    tagline_en="Tiger General, Sworn Brother of Guan Yu",
    tagline_ko="호랑이 장군, 관우의 맹세한 형제",
    description_en="""Zhang Fei was the fierce warrior who swore brotherhood with Liu Bei and Guan Yu in the Peach Garden oath. Known for his terrifying battle cry and his immense strength, he wielded the Serpent Spear and was feared across the Three Kingdoms.

His most legendary feat was at the Battle of Changban, where he stood alone on a bridge and challenged Cao Cao's entire army. His roar was so fierce that it allegedly frightened an enemy general to death.

Zhang Fei represents raw martial power, fierce loyalty to brotherhood, and the warrior spirit that knows no fear.""",
    description_ko="""장비는 도원결의에서 유비, 관우와 형제의 맹세를 한 사나운 전사였습니다. 무시무시한 함성과 엄청난 힘으로 알려진 그는 사모를 휘둘렀고 삼국 전역에서 두려움의 대상이었습니다.

그의 가장 전설적인 업적은 장판파 전투로, 그는 다리 위에 홀로 서서 조조의 전 군대에 도전했습니다. 그의 포효는 너무 사나워서 적 장수가 두려움에 죽었다고 합니다.

장비는 순수한 무력, 형제애에 대한 사나운 충성, 그리고 두려움을 모르는 전사 정신을 대표합니다.""",
    traits_en=["Fierce", "Loyal", "Roaring", "Powerful", "Brotherhood"],
    traits_ko=["사나운", "충성스러운", "포효하는", "강력한", "형제애"],
    story_en="At Changban Bridge, Zhang Fei faced Cao Cao's pursuing army alone. He planted his spear and roared: 'I am Zhang Fei! Who dares fight me to the death?' His eyes blazed so fiercely that Cao Cao's generals fled in terror.",
    story_ko="장판교에서 장비는 추격하는 조조의 군대를 홀로 맞았습니다. 그는 창을 꽂고 포효했습니다: '나는 장비다! 누가 감히 나와 죽음을 걸고 싸우겠는가?' 그의 눈이 너무 사납게 빛나서 조조의 장수들이 공포에 질려 도망쳤습니다.",
    match_message_en="Your features carry the fierce power of Zhang Fei. There is thundering brotherhood in your appearance—the look of one whose loyalty roars louder than any army.",
    match_message_ko="당신의 이목구비는 장비의 사나운 힘을 담고 있습니다. 당신의 외모에는 우레 같은 형제애가 있습니다—충성이 어떤 군대보다 크게 포효하는 사람의 모습.",
    image_prompt="Fierce warrior with wild beard and blazing eyes, holding Serpent Spear, standing defiant on bridge, expression of terrifying battle rage, Chinese Three Kingdoms epic style",
    visual_description="Wild fierce features, blazing terrifying eyes, powerful intimidating presence, expression of fearless battle fury",
    aliases=["張飛", "The Tiger General", "Yide"],
    era="Three Kingdoms Period",
    related_characters=["liu_bei", "guan_yu", "cao_cao", "zhuge_liang"]
)

CAO_CAO_DESC = CharacterDescription(
    id="cao_cao",
    name_en="Cao Cao",
    name_ko="조조",
    tagline_en="King of Wei, Supreme Pragmatist",
    tagline_ko="위왕, 최고의 현실주의자",
    description_en="""Cao Cao was the founder of the Wei kingdom and one of the most controversial figures in Chinese history. Brilliant strategist, skilled poet, and ruthless ruler, he embodied the Machiavellian principle that effectiveness matters more than morality in governance.

His famous quote—'I would rather betray the world than let the world betray me'—captures his philosophy. Yet he was also a patron of the arts and capable of generosity, making him one of history's most complex figures.

Cao Cao represents pragmatic ambition, the complexity of power, and the eternal debate between effectiveness and morality in leadership.""",
    description_ko="""조조는 위나라의 창건자이자 중국 역사에서 가장 논쟁적인 인물 중 하나입니다. 탁월한 전략가, 숙련된 시인, 무자비한 통치자로서, 그는 통치에서 도덕보다 효과가 더 중요하다는 마키아벨리적 원칙을 구현했습니다.

그의 유명한 인용—'내가 차라리 세상을 배신할지언정 세상이 나를 배신하게 두지 않겠다'—는 그의 철학을 포착합니다. 그러나 그는 또한 예술의 후원자였고 관대함을 발휘할 수 있어, 그를 역사상 가장 복잡한 인물 중 하나로 만들었습니다.

조조는 실용적인 야망, 권력의 복잡성, 그리고 리더십에서 효과와 도덕 사이의 영원한 논쟁을 대표합니다.""",
    traits_en=["Pragmatic", "Brilliant", "Ruthless", "Poetic", "Complex"],
    traits_ko=["실용적인", "탁월한", "무자비한", "시적인", "복잡한"],
    story_en="When Cao Cao's suspicion led him to kill his host's family, mistaking the sound of knife-sharpening for an assassination plot, he discovered they were preparing a feast in his honor. Rather than regret, he finished killing everyone—and coined his infamous motto.",
    story_ko="조조의 의심이 칼 가는 소리를 암살 음모로 오해하여 숙주 가족을 죽이게 했을 때, 그는 그들이 그를 위한 잔치를 준비하고 있었음을 발견했습니다. 후회하기보다 그는 모두를 죽이고—그의 악명 높은 좌우명을 만들었습니다.",
    match_message_en="Your features carry the pragmatic brilliance of Cao Cao. There is calculating power in your appearance—the look of one who sees reality clearly and acts without sentimental hesitation.",
    match_message_ko="당신의 이목구비는 조조의 실용적인 탁월함을 담고 있습니다. 당신의 외모에는 계산하는 힘이 있습니다—현실을 명확히 보고 감상적 망설임 없이 행동하는 사람의 모습.",
    image_prompt="Calculating ruler in black robes with penetrating gaze, strategic maps behind, expression of ruthless intelligence and poetic depth, Chinese Three Kingdoms commanding style",
    visual_description="Sharp intelligent features, calculating penetrating eyes, commanding ambitious presence, expression of brilliant ruthlessness",
    aliases=["曹操", "King of Wei", "Mengde"],
    era="Three Kingdoms Period",
    related_characters=["liu_bei", "guan_yu", "zhuge_liang", "sun_quan"]
)

XI_SHI_DESC = CharacterDescription(
    id="xi_shi",
    name_en="Xi Shi",
    name_ko="서시",
    tagline_en="One of Four Great Beauties, Destroyer of Wu",
    tagline_ko="사대 미인 중 하나, 오나라의 파괴자",
    description_en="""Xi Shi was one of the Four Great Beauties of ancient China, so beautiful that fish forgot to swim when they saw her reflection. She was sent by King Goujian of Yue as a gift to King Fuchai of Wu, tasked with distracting him from statecraft.

Her mission succeeded beyond imagination—Fuchai became so enamored that he neglected his kingdom, allowing Yue to recover and ultimately destroy Wu. Xi Shi's beauty was thus a weapon that toppled a nation.

Xi Shi represents beauty as power, the tragic role of women in political schemes, and the ancient truth that empires can fall to desire.""",
    description_ko="""서시는 고대 중국의 사대 미인 중 하나로, 너무 아름다워서 물고기가 그녀의 반영을 보면 헤엄치는 것을 잊었습니다. 그녀는 월나라의 구천 왕에 의해 오나라의 부차 왕에게 선물로 보내져, 그를 국정에서 산만하게 하는 임무를 맡았습니다.

그녀의 임무는 상상 이상으로 성공했습니다—부차는 너무 빠져서 왕국을 무시했고, 이로 인해 월나라가 회복하여 궁극적으로 오나라를 멸망시킬 수 있었습니다. 따라서 서시의 아름다움은 나라를 무너뜨린 무기였습니다.

서시는 힘으로서의 아름다움, 정치적 음모에서 여성의 비극적 역할, 그리고 제국이 욕망에 무너질 수 있다는 고대의 진실을 대표합니다.""",
    traits_en=["Beautiful", "Tragic", "Patriotic", "Weapon", "Sacrificing"],
    traits_ko=["아름다운", "비극적인", "애국적인", "무기", "희생하는"],
    story_en="Xi Shi was a village washerwoman when scouts found her. Trained in arts and graces, she was given to King Fuchai, who built her magnificent palaces. But her heart remained with her homeland. Her success meant her sacrifice—she gave her life to destroy an enemy king.",
    story_ko="서시는 정탐꾼들이 그녀를 발견했을 때 마을 빨래하는 여자였습니다. 기예와 품격을 훈련받아, 그녀는 부차 왕에게 주어졌고, 부차는 그녀를 위해 웅장한 궁전을 지었습니다. 하지만 그녀의 마음은 고향에 남아 있었습니다. 그녀의 성공은 그녀의 희생을 의미했습니다—그녀는 적의 왕을 파괴하기 위해 삶을 바쳤습니다.",
    match_message_en="Your features carry the legendary beauty of Xi Shi. There is nation-toppling grace in your appearance—the look of one whose beauty is itself a power that shapes history.",
    match_message_ko="당신의 이목구비는 서시의 전설적인 아름다움을 담고 있습니다. 당신의 외모에는 나라를 무너뜨리는 우아함이 있습니다—아름다움 자체가 역사를 형성하는 힘인 사람의 모습.",
    image_prompt="Legendary beauty in elegant ancient Chinese dress by lotus pond, fish gazing up at her reflection, expression of tragic beautiful purpose, classical Chinese beauty painting style",
    visual_description="Legendary beautiful features, deep melancholy eyes, graceful tragic bearing, expression of beauty as destiny",
    aliases=["西施", "Fish-Sinking Beauty"],
    era="Spring and Autumn Period",
    related_characters=["goujian", "fuchai", "fan_li"]
)


# Dictionary of Chinese descriptions
CHINESE_DESCRIPTIONS = {
    "jade_emperor": JADE_EMPEROR_DESC,
    "sun_wukong": SUN_WUKONG_DESC,
    "guanyin": GUANYIN_DESC,
    "erlang_shen": ERLANG_SHEN_DESC,
    "nezha": NEZHA_DESC,
    "dragon_king": DRAGON_KING_DESC,
    "queen_mother": QUEEN_MOTHER_DESC,
    "chang_e": CHANG_E_DESC,
    "guan_yu": GUAN_YU_EXTENDED_DESC,
    "zhuge_liang": ZHUGE_LIANG_DESC,
    "qin_shi_huang": QIN_SHI_HUANG_DESC,
    "confucius": CONFUCIUS_EXTENDED_DESC,
    "laozi": LAOZI_DESC,
    "mu_lan": MU_LAN_DESC,
    "nuwa": NUWA_DESC,
    "houyi": HOUYI_DESC,
    "lu_dongbin": LU_DONGBIN_DESC,
    "zhang_fei": ZHANG_FEI_DESC,
    "cao_cao": CAO_CAO_DESC,
    "xi_shi": XI_SHI_DESC,
}
