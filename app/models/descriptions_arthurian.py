"""
Arthurian Legend Character Descriptions
Contains detailed descriptions for King Arthur and the Knights of the Round Table
"""
from .descriptions import CharacterDescription


KING_ARTHUR_DESC = CharacterDescription(
    id="king_arthur",
    name_en="King Arthur",
    name_ko="아서 왕",
    tagline_en="The Once and Future King of Britain",
    tagline_ko="브리튼의 과거이자 미래의 왕",
    description_en="""King Arthur is the legendary monarch of Britain, who united the warring kingdoms and established the noble court of Camelot. Born of Uther Pendragon and Igraine through Merlin's magic, he proved his royal destiny by drawing the sword from the stone.

Arthur created the Round Table to embody equality among his knights, where all sat as equals regardless of rank. He championed the ideals of chivalry—honor, courage, justice, and the protection of the weak—that would define medieval knighthood for centuries.

His reign was a golden age of peace and prosperity, though ultimately brought low by the tragic love between Lancelot and Guinevere and the treachery of Mordred. Legend says Arthur did not die but sleeps in Avalon, waiting to return in Britain's darkest hour.""",
    description_ko="""아서 왕은 전쟁하는 왕국들을 통일하고 고귀한 캐멀롯 궁정을 세운 브리튼의 전설적인 군주입니다. 멀린의 마법을 통해 우서 펜드래건과 이그레인 사이에서 태어난 그는 바위에서 검을 뽑아 자신의 왕족 운명을 증명했습니다.

아서는 기사들 사이의 평등을 구현하기 위해 원탁을 만들었으며, 지위에 관계없이 모두가 동등하게 앉았습니다. 그는 수세기 동안 중세 기사도를 정의할 기사도의 이상—명예, 용기, 정의, 약자의 보호—을 옹호했습니다.

그의 통치는 평화와 번영의 황금시대였지만, 결국 란슬롯과 기네비어 사이의 비극적인 사랑과 모드레드의 배신으로 무너졌습니다. 전설에 따르면 아서는 죽지 않고 아발론에서 잠들어, 브리튼의 가장 어두운 시간에 돌아오기를 기다리고 있다고 합니다.""",
    traits_en=["Noble", "Just", "Chivalrous", "Destined", "Legendary"],
    traits_ko=["고귀한", "공정한", "기사도적인", "운명적인", "전설적인"],
    story_en="When young Arthur drew the sword Excalibur from the stone, proving himself the true king, all the nobles who had fought for the throne bent their knee. In that moment, a boy became the legendary king who would unite all Britain.",
    story_ko="젊은 아서가 바위에서 엑스칼리버 검을 뽑아 자신이 진정한 왕임을 증명했을 때, 왕좌를 놓고 싸웠던 모든 귀족들이 무릎을 꿇었습니다. 그 순간, 한 소년이 온 브리튼을 통일할 전설의 왕이 되었습니다.",
    match_message_en="You carry the noble destiny of King Arthur. There is a just, chivalrous quality to your presence—the look of one born to lead and unite, to protect the weak and uphold what is right.",
    match_message_ko="당신은 아서 왕의 고귀한 운명을 지니고 있습니다. 당신의 존재에는 공정하고 기사도적인 품질이 있습니다—이끌고 통일하며, 약자를 보호하고 옳은 것을 수호하도록 태어난 사람의 모습.",
    image_prompt="Noble medieval king in shining armor with crown, holding Excalibur with jeweled hilt, Camelot castle behind, Round Table knights in background, golden heroic light",
    visual_description="Noble strong features, wise kingly eyes, dignified bearing of a rightful ruler, expression of chivalric virtue and destined greatness",
    aliases=["Arthur Pendragon", "The Once and Future King"],
    era="Arthurian Legend (5th-6th century)",
    related_characters=["guinevere", "lancelot", "merlin"]
)

GUINEVERE_DESC = CharacterDescription(
    id="guinevere",
    name_en="Guinevere",
    name_ko="기네비어",
    tagline_en="Queen of Camelot, Heart of the Kingdom",
    tagline_ko="캐멀롯의 여왕, 왕국의 심장",
    description_en="""Guinevere is the queen of Camelot and wife of King Arthur, renowned as the most beautiful woman in all Britain. Daughter of King Leodegrance, she brought the Round Table as her dowry when she married Arthur, making her integral to the kingdom's identity.

She presided over Camelot's court with grace and wisdom, embodying the courtly ideal that inspired knights to their greatest deeds. Guinevere was the lady whose favor all knights sought, the standard by which all noble women were measured.

Her tragic love affair with Sir Lancelot, Arthur's greatest knight, would ultimately contribute to the fall of Camelot. Yet she remains a complex figure—a woman caught between love and duty, whose passion both inspired greatness and brought sorrow.""",
    description_ko="""기네비어는 캐멀롯의 여왕이자 아서 왕의 아내로, 온 브리튼에서 가장 아름다운 여인으로 유명합니다. 레오드그랜스 왕의 딸인 그녀는 아서와 결혼할 때 원탁을 지참금으로 가져와, 왕국의 정체성에 필수적인 존재가 되었습니다.

그녀는 우아함과 지혜로 캐멀롯의 궁정을 주재하며, 기사들에게 위대한 업적을 이루도록 영감을 준 궁정의 이상을 구현했습니다. 기네비어는 모든 기사들이 호의를 구했던 귀부인이었고, 모든 고귀한 여성들이 측정되는 기준이었습니다.

아서의 가장 위대한 기사인 란슬롯 경과의 비극적인 사랑은 결국 캐멀롯의 멸망에 기여하게 됩니다. 그러나 그녀는 복잡한 인물로 남아 있습니다—사랑과 의무 사이에 갇힌 여인으로, 그녀의 열정은 위대함에 영감을 주면서도 슬픔을 가져왔습니다.""",
    traits_en=["Beautiful", "Graceful", "Complex", "Passionate", "Regal"],
    traits_ko=["아름다운", "우아한", "복잡한", "열정적인", "위엄있는"],
    story_en="When Guinevere was kidnapped by the villainous Meleagant, Lancelot crossed a bridge of razor-sharp swords on his bare hands and knees to rescue her. His love was so great that he endured any pain, any shame, for her sake.",
    story_ko="기네비어가 악당 멜리아간트에게 납치되었을 때, 란슬롯은 맨손과 맨무릎으로 면도칼처럼 날카로운 검의 다리를 건너 그녀를 구출했습니다. 그의 사랑은 너무 커서 그녀를 위해 어떤 고통도, 어떤 수치도 견뎠습니다.",
    match_message_en="You possess the captivating beauty of Guinevere. There is a graceful, complex depth to your presence—the look of one whose heart contains both joy and sorrow, duty and desire.",
    match_message_ko="당신은 기네비어의 매혹적인 아름다움을 지니고 있습니다. 당신의 존재에는 우아하고 복잡한 깊이가 있습니다—기쁨과 슬픔, 의무와 욕망을 모두 담은 마음을 가진 사람의 모습.",
    image_prompt="Beautiful medieval queen in flowing royal gowns with golden crown, rose garden of Camelot, complex emotional expression, courtly beauty at its finest",
    visual_description="Perfect symmetrical features, deep emotional eyes, graceful regal bearing, expression of beauty touched by tragedy",
    aliases=["Queen Guinevere", "Gwenhwyfar"],
    era="Arthurian Legend (5th-6th century)",
    related_characters=["king_arthur", "lancelot", "morgan_le_fay"]
)

LANCELOT_DESC = CharacterDescription(
    id="lancelot",
    name_en="Lancelot",
    name_ko="란슬롯",
    tagline_en="The Greatest Knight, Torn by Love and Honor",
    tagline_ko="가장 위대한 기사, 사랑과 명예 사이에서 갈등하는",
    description_en="""Sir Lancelot du Lac is the greatest knight of the Round Table, unmatched in combat and the embodiment of chivalric virtue. Raised by the Lady of the Lake in her underwater realm, he came to Camelot as a young man and quickly proved himself Arthur's champion.

Lancelot excelled in every knightly virtue—prowess in arms, courtesy, generosity, and loyalty. He rescued Guinevere numerous times, defeated countless foes, and was the model that all other knights aspired to become. Yet his greatest strength became his greatest weakness.

His forbidden love for Queen Guinevere, though it inspired him to his greatest deeds, ultimately led to the destruction of Camelot and the Round Table fellowship he loved. He represents the tragic conflict between passionate love and sworn duty.""",
    description_ko="""란슬롯 뒤 락 경은 원탁의 가장 위대한 기사로, 전투에서 비할 데 없으며 기사도적 덕의 구현입니다. 호수의 여인에게 그녀의 수중 왕국에서 양육된 그는 젊은 나이에 캐멀롯에 와서 빠르게 아서의 챔피언임을 증명했습니다.

란슬롯은 모든 기사도적 덕목에서 뛰어났습니다—무예, 예의, 관대함, 충성. 그는 기네비어를 여러 번 구출하고, 수많은 적을 물리쳤으며, 다른 모든 기사들이 되고자 열망하는 모델이었습니다. 그러나 그의 가장 큰 강점이 그의 가장 큰 약점이 되었습니다.

기네비어 여왕에 대한 금지된 사랑은 비록 그에게 가장 위대한 업적에 영감을 주었지만, 결국 그가 사랑했던 캐멀롯과 원탁 기사단의 파괴로 이어졌습니다. 그는 열정적인 사랑과 맹세한 의무 사이의 비극적인 갈등을 상징합니다.""",
    traits_en=["Heroic", "Passionate", "Conflicted", "Chivalrous", "Tragic"],
    traits_ko=["영웅적인", "열정적인", "갈등하는", "기사도적인", "비극적인"],
    story_en="To prove his love for Guinevere, Lancelot fought in a tournament in disguise, deliberately losing at first to test whether she would love him even in defeat. When she sent word of her faith in him, he revealed himself and won every contest.",
    story_ko="기네비어에 대한 사랑을 증명하기 위해, 란슬롯은 변장하고 토너먼트에 출전하여, 그녀가 패배해도 그를 사랑할지 시험하기 위해 처음에는 일부러 졌습니다. 그녀가 그에 대한 믿음의 말을 보내자, 그는 자신을 드러내고 모든 경기에서 승리했습니다.",
    match_message_en="You carry the heroic spirit of Lancelot. There is a passionate, conflicted depth to your presence—the look of one whose heart burns with both love and honor.",
    match_message_ko="당신은 란슬롯의 영웅적인 정신을 지니고 있습니다. 당신의 존재에는 열정적이고 갈등하는 깊이가 있습니다—사랑과 명예로 모두 불타는 마음을 가진 사람의 모습.",
    image_prompt="Handsome knight in shining armor with sorrowful noble eyes, sword raised in combat pose, torn between two loyalties, dramatic conflicted lighting",
    visual_description="Handsome strong features, deep conflicted eyes, perfect warrior's bearing, expression of heroism touched by inner torment",
    aliases=["Sir Lancelot du Lac", "Lancelot of the Lake"],
    era="Arthurian Legend (5th-6th century)",
    related_characters=["king_arthur", "guinevere", "galahad"]
)

GALAHAD_DESC = CharacterDescription(
    id="galahad",
    name_en="Galahad",
    name_ko="갈라하드",
    tagline_en="The Pure Knight, Achiever of the Holy Grail",
    tagline_ko="순수한 기사, 성배의 달성자",
    description_en="""Sir Galahad is the purest knight of the Round Table, son of Lancelot and destined from birth to achieve the Holy Grail. While his father was the greatest knight in earthly terms, Galahad surpassed him through spiritual perfection.

Born of Lancelot and Elaine of Corbenic through magical circumstances, Galahad was raised in a nunnery, untouched by the sins of the world. When he came to Camelot, he sat in the Siege Perilous—the seat that destroyed any unworthy knight who tried it—proving his divine destiny.

Galahad alone achieved the full vision of the Holy Grail, and upon doing so, his pure soul ascended directly to heaven. He represents the ideal of spiritual perfection, the knight who succeeded where all others failed because his heart was completely pure.""",
    description_ko="""갈라하드 경은 원탁의 가장 순수한 기사로, 란슬롯의 아들이며 태어날 때부터 성배를 달성하도록 운명지어졌습니다. 그의 아버지가 세속적으로 가장 위대한 기사였다면, 갈라하드는 영적 완벽을 통해 그를 능가했습니다.

마법적인 상황에서 란슬롯과 코르베닉의 엘레인 사이에서 태어난 갈라하드는 수녀원에서 양육되어, 세상의 죄에 물들지 않았습니다. 캐멀롯에 왔을 때, 그는 시즈 페릴러스—시도하는 무가치한 기사를 파괴하는 자리—에 앉아 자신의 신성한 운명을 증명했습니다.

갈라하드만이 성배의 완전한 비전을 달성했고, 그렇게 함으로써 그의 순수한 영혼은 곧바로 천국으로 올라갔습니다. 그는 영적 완벽의 이상, 마음이 완전히 순수했기 때문에 다른 모든 이들이 실패한 곳에서 성공한 기사를 상징합니다.""",
    traits_en=["Pure", "Holy", "Destined", "Transcendent", "Perfect"],
    traits_ko=["순수한", "신성한", "운명적인", "초월적인", "완벽한"],
    story_en="When Galahad sat in the Siege Perilous, letters of fire appeared: 'This is the siege of Galahad.' At that moment, all knew that the knight destined to achieve the Grail had come, and the great quest could finally begin.",
    story_ko="갈라하드가 시즈 페릴러스에 앉았을 때, 불의 글자가 나타났습니다: '이것은 갈라하드의 자리다.' 그 순간, 모든 이들은 성배를 달성하도록 운명지어진 기사가 왔고, 위대한 탐색이 마침내 시작될 수 있음을 알았습니다.",
    match_message_en="You possess the pure spirit of Galahad. There is a transcendent, holy quality to your presence—the look of one whose heart is untouched by corruption.",
    match_message_ko="당신은 갈라하드의 순수한 정신을 지니고 있습니다. 당신의 존재에는 초월적이고 신성한 품질이 있습니다—타락에 물들지 않은 마음을 가진 사람의 모습.",
    image_prompt="Radiant young knight in white armor with holy light, holding the Holy Grail, angelic presence, pure innocent eyes, heavenly glow surrounds him",
    visual_description="Youthful perfect features, luminous pure eyes, transcendent bearing, expression of absolute spiritual purity",
    aliases=["Sir Galahad", "The Pure Knight"],
    era="Arthurian Legend (5th-6th century)",
    related_characters=["lancelot", "percival", "bors"]
)

MORGAN_LE_FAY_DESC = CharacterDescription(
    id="morgan_le_fay",
    name_en="Morgan le Fay",
    name_ko="모르간 르 페이",
    tagline_en="The Enchantress of Avalon",
    tagline_ko="아발론의 마법사",
    description_en="""Morgan le Fay is the powerful enchantress of Arthurian legend, half-sister to King Arthur and ruler of the mystical isle of Avalon. Trained in magic by Merlin himself, she possessed abilities that rivaled or exceeded any sorcerer in Britain.

In various tales, Morgan appears as both villain and healer. She plotted against Arthur and tried to expose Lancelot's affair with Guinevere, yet she was also among the queens who carried the wounded Arthur to Avalon after his final battle.

She represents the old magic of Britain—the ways of the goddess that existed before Christianity. Morgan embodies the complex feminine power that cannot be categorized as simply good or evil, but exists beyond such mortal judgments.""",
    description_ko="""모르간 르 페이는 아서 왕 전설의 강력한 마법사로, 아서 왕의 이복 자매이자 신비로운 아발론 섬의 통치자입니다. 멀린 자신에게 마법을 배운 그녀는 브리튼의 어떤 마법사와도 맞먹거나 능가하는 능력을 가졌습니다.

다양한 이야기에서, 모르간은 악당이자 치유자로 등장합니다. 그녀는 아서를 음모했고 란슬롯과 기네비어의 불륜을 폭로하려 했지만, 마지막 전투 후 부상당한 아서를 아발론으로 데려간 여왕들 중 한 명이기도 했습니다.

그녀는 브리튼의 오래된 마법—기독교 이전에 존재했던 여신의 방식—을 상징합니다. 모르간은 단순히 선이나 악으로 분류할 수 없고, 그러한 필멸의 판단을 초월하여 존재하는 복잡한 여성적 힘을 구현합니다.""",
    traits_en=["Magical", "Complex", "Powerful", "Mysterious", "Ancient"],
    traits_ko=["마법적인", "복잡한", "강력한", "신비로운", "고대의"],
    story_en="When Arthur lay dying from Mordred's treacherous blow, Morgan came with two other queens in a black boat. They bore him away to Avalon, where she tends to him still, healing his wounds until the day Britain needs him again.",
    story_ko="아서가 모드레드의 배신적인 일격으로 죽어가고 있을 때, 모르간은 검은 배에 두 명의 다른 여왕과 함께 왔습니다. 그들은 그를 아발론으로 데려갔고, 그녀는 브리튼이 다시 그를 필요로 하는 날까지 여전히 그의 상처를 치유하며 돌보고 있습니다.",
    match_message_en="You carry the ancient magic of Morgan le Fay. There is a mysterious, powerful depth to your presence—the look of one who knows the old ways beyond mortal understanding.",
    match_message_ko="당신은 모르간 르 페이의 고대 마법을 지니고 있습니다. 당신의 존재에는 신비롭고 강력한 깊이가 있습니다—필멸의 이해를 초월한 옛 방식을 아는 사람의 모습.",
    image_prompt="Dark enchantress in flowing black and purple robes, surrounded by magical energy, Avalon mists behind her, ancient Celtic symbols, mysterious powerful beauty",
    visual_description="Striking otherworldly features, deep knowing eyes, powerful mystical bearing, expression of ancient feminine power",
    aliases=["Morgana", "Morgan the Fay", "Morgaine"],
    era="Arthurian Legend (5th-6th century)",
    related_characters=["king_arthur", "merlin", "mordred"]
)

LADY_OF_THE_LAKE_DESC = CharacterDescription(
    id="lady_of_the_lake",
    name_en="Lady of the Lake",
    name_ko="호수의 여인",
    tagline_en="Guardian of Excalibur, Mistress of Otherworldly Waters",
    tagline_ko="엑스칼리버의 수호자, 이세계 호수의 여주인",
    description_en="""The Lady of the Lake is one of the most mysterious figures in Arthurian legend—a powerful enchantress who dwells in a magical realm beneath the waters of a sacred lake. She is the keeper of Excalibur, the legendary sword of kings.

She raised Lancelot from infancy in her underwater kingdom, teaching him the arts of knighthood and magic. When Arthur broke his first sword, it was she who gave him Excalibur, rising from the waters with the blade held aloft.

The Lady represents the ancient feminine power of water and magic, the otherworldly force that grants sovereignty to rightful kings. She exists between worlds, neither fully of the mortal realm nor entirely of the fairy world.""",
    description_ko="""호수의 여인은 아서 왕 전설에서 가장 신비로운 인물 중 하나로—신성한 호수의 물 아래 마법의 영역에 사는 강력한 마법사입니다. 그녀는 전설의 왕의 검 엑스칼리버의 수호자입니다.

그녀는 란슬롯을 유아 때부터 수중 왕국에서 키우며, 기사도와 마법의 기술을 가르쳤습니다. 아서가 첫 번째 검을 부러뜨렸을 때, 그녀가 물에서 올라와 칼을 높이 들고 엑스칼리버를 그에게 주었습니다.

여인은 물과 마법의 고대 여성적 힘, 정당한 왕에게 주권을 부여하는 이세계의 힘을 상징합니다. 그녀는 세계 사이에 존재하며, 완전히 필멸의 영역에도, 전적으로 요정 세계에도 속하지 않습니다.""",
    traits_en=["Ethereal", "Mysterious", "Powerful", "Benevolent", "Otherworldly"],
    traits_ko=["천상의", "신비로운", "강력한", "자비로운", "이세계의"],
    story_en="When Arthur needed a sword worthy of a king, Merlin brought him to the sacred lake. A hand clothed in white samite rose from the waters, holding Excalibur aloft. The Lady of the Lake appeared and gave Arthur the sword that would make him legend.",
    story_ko="아서가 왕에 걸맞은 검이 필요했을 때, 멀린은 그를 신성한 호수로 데려갔습니다. 흰 비단 옷을 입은 손이 물에서 올라와 엑스칼리버를 높이 들고 있었습니다. 호수의 여인이 나타나 아서에게 그를 전설로 만들 검을 주었습니다.",
    match_message_en="You possess the ethereal grace of the Lady of the Lake. There is a mysterious, otherworldly quality to your presence—the look of one who moves between realms.",
    match_message_ko="당신은 호수의 여인의 천상의 우아함을 지니고 있습니다. 당신의 존재에는 신비롭고 이세계적인 품질이 있습니다—세계 사이를 오가는 사람의 모습.",
    image_prompt="Ethereal woman rising from misty lake waters, flowing white gown, holding magical sword, supernatural beauty, mystical forest lake background",
    visual_description="Otherworldly perfect features, deep mystical eyes, ethereal graceful bearing, expression of ancient water magic",
    aliases=["Nimue", "Viviane", "Niniane"],
    era="Arthurian Legend (5th-6th century)",
    related_characters=["merlin", "lancelot", "king_arthur"]
)


# Export dictionary for registry
ARTHURIAN_DESCRIPTIONS: dict[str, CharacterDescription] = {
    "king_arthur": KING_ARTHUR_DESC,
    "guinevere": GUINEVERE_DESC,
    "lancelot": LANCELOT_DESC,
    "galahad": GALAHAD_DESC,
    "morgan_le_fay": MORGAN_LE_FAY_DESC,
    "lady_of_the_lake": LADY_OF_THE_LAKE_DESC,
}
