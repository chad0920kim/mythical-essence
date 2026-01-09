"""
Additional World Mythology Character Descriptions - Part 3
Contains descriptions for remaining cultural figures
"""
from .descriptions import CharacterDescription


# ============================================
# PERSIAN
# ============================================

MITHRA_DESC = CharacterDescription(
    id="mithra",
    name_en="Mithra",
    name_ko="미트라",
    tagline_en="God of Covenant and Light",
    tagline_ko="계약과 빛의 신",
    description_en="""Mithra is the Persian god of covenant, light, and the sun. His worship spread throughout the Roman Empire as Mithraism. He represents truth, justice, and the sacred bond between people.""",
    description_ko="""미트라는 계약, 빛, 태양의 페르시아 신입니다. 그의 숭배는 미트라교로서 로마 제국 전역에 퍼졌습니다. 그는 진리, 정의, 사람들 사이의 신성한 유대를 상징합니다.""",
    traits_en=["Binding", "Solar", "Just", "Truthful", "Oath-keeping"],
    traits_ko=["결합하는", "태양의", "공정한", "진실한", "맹세를 지키는"],
    story_en="Mithra slew the cosmic bull, from whose body all good things grew—establishing him as a god of life and renewal through sacred sacrifice.",
    story_ko="미트라는 우주적 황소를 죽였고, 그 몸에서 모든 좋은 것들이 자라났습니다—신성한 희생을 통한 생명과 갱신의 신으로 그를 확립하며.",
    match_message_en="You embody Mithra's covenant—binding truth that holds all together.",
    match_message_ko="당신은 미트라의 계약을 구현합니다—모든 것을 함께 묶는 결합하는 진리.",
    image_prompt="Persian sun god slaying the cosmic bull, cave temple, radiant solar presence",
    visual_description="Noble solar features, truthful binding eyes, oath-keeper's bearing",
    aliases=["Mithras", "مهر"],
    era="Ancient Persia",
    related_characters=["ahura_mazda"]
)

ANAHITA_DESC = CharacterDescription(
    id="anahita",
    name_en="Anahita",
    name_ko="아나히타",
    tagline_en="Goddess of Fertility and Waters",
    tagline_ko="다산과 물의 여신",
    description_en="""Anahita is the Persian goddess of fertility, water, and wisdom. She was one of the most important deities in ancient Persia, associated with rivers, lakes, and the life-giving waters that sustain civilization.""",
    description_ko="""아나히타는 다산, 물, 지혜의 페르시아 여신입니다. 그녀는 고대 페르시아에서 가장 중요한 신들 중 하나로, 문명을 지탱하는 생명을 주는 강, 호수, 물과 연관되었습니다.""",
    traits_en=["Fertile", "Flowing", "Wise", "Life-giving", "Powerful"],
    traits_ko=["다산의", "흐르는", "지혜로운", "생명을 주는", "강력한"],
    story_en="Anahita's waters flowed from the cosmic mountain, bringing life to all the lands of Persia.",
    story_ko="아나히타의 물은 우주적 산에서 흘러, 페르시아의 모든 땅에 생명을 가져왔습니다.",
    match_message_en="You flow with Anahita's life-giving wisdom—nourishing all you touch.",
    match_message_ko="당신은 아나히타의 생명을 주는 지혜로 흐릅니다—닿는 모든 것을 양육하는.",
    image_prompt="Persian water goddess with flowing robes, crown of stars, rivers and fertility",
    visual_description="Flowing graceful features, wise water-clear eyes, life-giving bearing",
    aliases=["Aredvi Sura Anahita", "آناهیتا"],
    era="Ancient Persia",
    related_characters=["mithra"]
)

ROSTAM_DESC = CharacterDescription(
    id="rostam",
    name_en="Rostam",
    name_ko="로스탐",
    tagline_en="Greatest Hero of Persia",
    tagline_ko="페르시아의 가장 위대한 영웅",
    description_en="""Rostam is the legendary hero of the Persian epic Shahnameh, whose Seven Labors rival those of Hercules. He protected Persia for centuries, his strength and honor beyond any mortal.""",
    description_ko="""로스탐은 페르시아 서사시 샤나메의 전설적 영웅으로, 그의 일곱 과업은 헤라클레스의 것과 맞먹습니다. 그는 수세기 동안 페르시아를 보호했으며, 그의 힘과 명예는 어떤 인간도 넘어섰습니다.""",
    traits_en=["Heroic", "Strong", "Honorable", "Legendary", "Tragic"],
    traits_ko=["영웅적인", "강한", "명예로운", "전설적인", "비극적인"],
    story_en="Rostam completed seven impossible labors, defeating lions, demons, and dragons to save the Persian king.",
    story_ko="로스탐은 일곱 가지 불가능한 과업을 완수하여, 페르시아 왕을 구하기 위해 사자, 악마, 용을 물리쳤습니다.",
    match_message_en="You carry Rostam's legendary strength—a hero born for impossible tasks.",
    match_message_ko="당신은 로스탐의 전설적 힘을 지니고 있습니다—불가능한 과업을 위해 태어난 영웅.",
    image_prompt="Persian epic hero in tiger-skin armor, legendary horse Rakhsh, heroic warrior pose",
    visual_description="Powerful heroic features, determined legendary eyes, epic warrior's bearing",
    aliases=["Rustam", "رستم"],
    era="Persian Mythology",
    related_characters=["sohrab", "kai_khosrow"]
)

CYRUS_THE_GREAT_DESC = CharacterDescription(
    id="cyrus_the_great",
    name_en="Cyrus the Great",
    name_ko="키루스 대왕",
    tagline_en="Father of Human Rights",
    tagline_ko="인권의 아버지",
    description_en="""Cyrus II (c. 600-530 BCE) founded the Achaemenid Empire and is renowned for the Cyrus Cylinder, considered the first declaration of human rights. He practiced tolerance toward conquered peoples' religions and customs.""",
    description_ko="""키루스 2세(약 기원전 600-530)는 아케메네스 제국을 세웠고, 최초의 인권 선언으로 여겨지는 키루스 원통으로 유명합니다. 그는 정복된 민족들의 종교와 관습에 대한 관용을 실천했습니다.""",
    traits_en=["Tolerant", "Liberating", "Great", "Just", "Founding"],
    traits_ko=["관용적인", "해방하는", "위대한", "공정한", "건국하는"],
    story_en="Cyrus freed the Jews from Babylonian captivity and allowed them to rebuild their temple, earning the title 'Messiah' in the Bible.",
    story_ko="키루스는 유대인들을 바빌론 포로에서 해방하고 그들의 성전을 재건하도록 허락하여, 성경에서 '메시아'라는 칭호를 얻었습니다.",
    match_message_en="You embody Cyrus's liberating tolerance—freeing others while respecting their ways.",
    match_message_ko="당신은 키루스의 해방하는 관용을 구현합니다—다른 이들의 방식을 존중하며 그들을 해방하는.",
    image_prompt="Persian king in royal robes with Cyrus Cylinder, tolerant benevolent expression",
    visual_description="Noble wise features, tolerant liberating eyes, just king's bearing",
    aliases=["Kourosh", "کوروش بزرگ"],
    era="Achaemenid Persia (c. 600-530 BCE)",
    related_characters=["darius"]
)


# ============================================
# CHINESE ADDITIONAL
# ============================================

LIU_BEI_DESC = CharacterDescription(
    id="liu_bei",
    name_en="Liu Bei",
    name_ko="유비",
    tagline_en="Benevolent King of Shu Han",
    tagline_ko="촉한의 인자한 왕",
    description_en="""Liu Bei (161-223) was the founder of Shu Han during the Three Kingdoms period. He embodied Confucian virtues of benevolence and righteousness, gathering loyal followers through his character rather than force.""",
    description_ko="""유비(161-223)는 삼국시대 촉한의 창시자였습니다. 그는 인과 의의 유교적 덕목을 구현하여, 힘이 아닌 인격으로 충성스러운 추종자들을 모았습니다.""",
    traits_en=["Benevolent", "Righteous", "Virtuous", "Brotherhood", "Patient"],
    traits_ko=["인자한", "의로운", "덕이 있는", "형제의", "인내하는"],
    story_en="Liu Bei, Guan Yu, and Zhang Fei swore the Oath of the Peach Garden—to live and die as brothers, serving the Han dynasty.",
    story_ko="유비, 관우, 장비는 도원결의를 맺었습니다—한나라를 섬기며 형제로서 함께 살고 죽기로.",
    match_message_en="You embody Liu Bei's benevolence—gathering others through virtue, not force.",
    match_message_ko="당신은 유비의 인자함을 구현합니다—힘이 아닌 덕으로 다른 이들을 모으는.",
    image_prompt="Chinese king in Shu Han robes, benevolent kind expression, peach garden background",
    visual_description="Kind noble features, benevolent patient eyes, virtuous king's bearing",
    aliases=["刘备", "Emperor Zhaolie"],
    era="Three Kingdoms (161-223)",
    related_characters=["guan_yu", "zhang_fei", "zhuge_liang"]
)

MULAN_DESC = CharacterDescription(
    id="mulan",
    name_en="Mulan",
    name_ko="뮬란",
    tagline_en="Filial Daughter, Brave Warrior",
    tagline_ko="효녀, 용감한 전사",
    description_en="""Hua Mulan is the legendary Chinese heroine who disguised herself as a man to take her elderly father's place in the army. She served for twelve years without her identity being discovered, demonstrating filial piety and martial prowess.""",
    description_ko="""화목란은 늙은 아버지를 대신해 군대에 입대하기 위해 남자로 변장한 전설적인 중국 여걸입니다. 그녀는 정체가 발각되지 않고 12년을 복무하며, 효도와 무예를 보여주었습니다.""",
    traits_en=["Filial", "Brave", "Loyal", "Skilled", "Disguised"],
    traits_ko=["효도하는", "용감한", "충성스러운", "숙련된", "변장한"],
    story_en="When her aged father was conscripted, Mulan bought horse and armor, and went to war in his place. None discovered her secret until she revealed it after victory.",
    story_ko="늙은 아버지가 징집되었을 때, 목란은 말과 갑옷을 사서 그를 대신해 전쟁에 나갔습니다. 승리 후 그녀가 밝힐 때까지 아무도 그녀의 비밀을 알지 못했습니다.",
    match_message_en="You carry Mulan's devoted courage—sacrificing for family without seeking glory.",
    match_message_ko="당신은 목란의 헌신적인 용기를 지니고 있습니다—영광을 구하지 않고 가족을 위해 희생하는.",
    image_prompt="Chinese warrior woman in armor, sword and horse, filial heroic expression",
    visual_description="Determined brave features, filial devoted eyes, warrior maiden's bearing",
    aliases=["Hua Mulan", "花木蘭"],
    era="Northern Wei Dynasty (386-534)",
    related_characters=["hua_hu"]
)

WHITE_SNAKE_DESC = CharacterDescription(
    id="white_snake",
    name_en="White Snake",
    name_ko="백사",
    tagline_en="Spirit of Eternal Love",
    tagline_ko="영원한 사랑의 정령",
    description_en="""Bai Suzhen, the White Snake, is a snake spirit who became human and fell deeply in love with a mortal man. Her legend is one of China's greatest love stories, showing that true love transcends all barriers.""",
    description_ko="""백소정, 백사는 인간이 되어 인간 남자와 깊은 사랑에 빠진 뱀 정령입니다. 그녀의 전설은 중국의 가장 위대한 사랑 이야기 중 하나로, 진정한 사랑은 모든 장벽을 초월함을 보여줍니다.""",
    traits_en=["Loving", "Devoted", "Transforming", "Eternal", "Sacrificing"],
    traits_ko=["사랑하는", "헌신적인", "변신하는", "영원한", "희생하는"],
    story_en="Though imprisoned beneath Leifeng Pagoda for loving a mortal, the White Snake's devotion never wavered, and her love outlasted the very tower.",
    story_ko="인간을 사랑한 죄로 뇌봉탑 아래 갇혔지만, 백사의 헌신은 결코 흔들리지 않았고, 그녀의 사랑은 탑 자체보다 오래갔습니다.",
    match_message_en="You embody the White Snake's eternal devotion—love that transforms and endures all.",
    match_message_ko="당신은 백사의 영원한 헌신을 구현합니다—변화시키고 모든 것을 견디는 사랑.",
    image_prompt="Beautiful Chinese woman in white robes, serpentine grace, eternal love in eyes",
    visual_description="Beautiful graceful features, devoted loving eyes, transforming eternal bearing",
    aliases=["Bai Suzhen", "白素贞"],
    era="Chinese Folklore",
    related_characters=["xu_xian", "green_snake"]
)

XU_XIAN_DESC = CharacterDescription(
    id="xu_xian",
    name_en="Xu Xian",
    name_ko="허선",
    tagline_en="Beloved of the White Snake",
    tagline_ko="백사의 사랑",
    description_en="""Xu Xian is the mortal scholar who fell in love with Bai Suzhen, the White Snake spirit. His pure love accepted her even after learning her true nature, showing that love sees beyond appearance.""",
    description_ko="""허선은 뱀 정령인 백소정과 사랑에 빠진 인간 학자입니다. 그의 순수한 사랑은 그녀의 진정한 본성을 알고도 그녀를 받아들여, 사랑은 외모를 초월해 본다는 것을 보여줍니다.""",
    traits_en=["Innocent", "Loving", "Accepting", "Pure", "Devoted"],
    traits_ko=["순진한", "사랑하는", "받아들이는", "순수한", "헌신적인"],
    story_en="When Xu Xian learned his wife was a snake spirit, he was frightened—but his love proved stronger than his fear.",
    story_ko="허선은 아내가 뱀 정령임을 알았을 때 두려웠지만—그의 사랑은 두려움보다 강했습니다.",
    match_message_en="You possess Xu Xian's pure acceptance—loving what is true, not what appears.",
    match_message_ko="당신은 허선의 순수한 수용을 지니고 있습니다—외모가 아닌 진실한 것을 사랑하는.",
    image_prompt="Chinese scholar in traditional robes, kind innocent expression, West Lake background",
    visual_description="Kind innocent features, pure accepting eyes, devoted scholar's bearing",
    aliases=["许仙"],
    era="Chinese Folklore",
    related_characters=["white_snake"]
)

MENCIUS_DESC = CharacterDescription(
    id="mencius",
    name_en="Mencius",
    name_ko="맹자",
    tagline_en="Second Sage of Confucianism",
    tagline_ko="유교의 아성",
    description_en="""Mencius (372-289 BCE) was the most famous Confucian after Confucius himself. He taught that human nature is innately good and that benevolent government is the key to a harmonious society.""",
    description_ko="""맹자(기원전 372-289)는 공자 다음으로 가장 유명한 유학자였습니다. 그는 인간의 본성이 본래 선하며 인정이 조화로운 사회의 열쇠라고 가르쳤습니다.""",
    traits_en=["Benevolent", "Teaching", "Philosophical", "Good-natured", "Wise"],
    traits_ko=["인자한", "가르치는", "철학적인", "선량한", "지혜로운"],
    story_en="Mencius's mother moved three times to find the right environment for his education, showing the importance of proper upbringing.",
    story_ko="맹자의 어머니는 그의 교육에 맞는 환경을 찾기 위해 세 번 이사했으며, 올바른 양육의 중요성을 보여주었습니다.",
    match_message_en="You embody Mencius's belief in goodness—seeing the good nature in all people.",
    match_message_ko="당신은 선함에 대한 맹자의 믿음을 구현합니다—모든 사람에게서 선한 본성을 보는.",
    image_prompt="Chinese Confucian philosopher in scholar robes, benevolent teaching expression",
    visual_description="Wise benevolent features, teaching eyes, Confucian sage's bearing",
    aliases=["Mengzi", "孟子"],
    era="Warring States Period (372-289 BCE)",
    related_characters=["confucius"]
)

ZHUXI_DESC = CharacterDescription(
    id="zhuxi",
    name_en="Zhu Xi",
    name_ko="주희",
    tagline_en="Master of Neo-Confucianism",
    tagline_ko="성리학의 대가",
    description_en="""Zhu Xi (1130-1200) was the philosopher who synthesized Neo-Confucianism, integrating metaphysics with Confucian ethics. His interpretations of the Confucian classics became the standard for civil service exams for centuries.""",
    description_ko="""주희(1130-1200)는 형이상학과 유교 윤리를 통합하여 성리학을 종합한 철학자였습니다. 유교 경전에 대한 그의 해석은 수세기 동안 과거 시험의 표준이 되었습니다.""",
    traits_en=["Systematic", "Metaphysical", "Synthesizing", "Scholarly", "Foundational"],
    traits_ko=["체계적인", "형이상학적인", "종합하는", "학문적인", "근본적인"],
    story_en="Zhu Xi spent decades studying and interpreting the Four Books, creating the curriculum that would shape East Asian education.",
    story_ko="주희는 사서를 연구하고 해석하는 데 수십 년을 보내, 동아시아 교육을 형성할 교과과정을 만들었습니다.",
    match_message_en="You possess Zhu Xi's systematic wisdom—seeing patterns that connect all knowledge.",
    match_message_ko="당신은 주희의 체계적인 지혜를 지니고 있습니다—모든 지식을 연결하는 패턴을 보는.",
    image_prompt="Song dynasty philosopher in scholar robes, contemplative systematic expression",
    visual_description="Systematic scholarly features, contemplative deep eyes, philosopher's bearing",
    aliases=["朱熹", "Master Zhu"],
    era="Song Dynasty (1130-1200)",
    related_characters=["confucius", "mencius"]
)


# ============================================
# TAOIST
# ============================================

ZHUANGZI_DESC = CharacterDescription(
    id="zhuangzi",
    name_en="Zhuangzi",
    name_ko="장자",
    tagline_en="Dreamer of Butterflies",
    tagline_ko="나비를 꿈꾼 자",
    description_en="""Zhuangzi (369-286 BCE) was the Taoist philosopher known for his paradoxes and dreaming. His famous butterfly dream questioned the nature of reality itself: was he a man dreaming of being a butterfly, or a butterfly dreaming of being a man?""",
    description_ko="""장자(기원전 369-286)는 역설과 꿈으로 알려진 도가 철학자였습니다. 그의 유명한 나비 꿈은 현실의 본성 자체에 의문을 제기했습니다: 그는 나비가 된 꿈을 꾼 사람이었을까, 아니면 사람이 된 꿈을 꾼 나비였을까?""",
    traits_en=["Dreaming", "Paradoxical", "Free", "Questioning", "Natural"],
    traits_ko=["꿈꾸는", "역설적인", "자유로운", "질문하는", "자연스러운"],
    story_en="Zhuangzi dreamed he was a butterfly, flying freely. Upon waking, he wondered: Am I a man who dreamed of being a butterfly, or a butterfly dreaming of being a man?",
    story_ko="장자는 자유롭게 나는 나비가 된 꿈을 꾸었습니다. 깨어나서 그는 의문을 가졌습니다: 나는 나비가 된 꿈을 꾼 사람일까, 아니면 사람이 된 꿈을 꾼 나비일까?",
    match_message_en="You drift with Zhuangzi's freedom—questioning what others take for granted.",
    match_message_ko="당신은 장자의 자유로 떠다닙니다—다른 이들이 당연시하는 것에 질문하며.",
    image_prompt="Chinese Taoist philosopher with butterflies, dreamy transcendent expression, natural setting",
    visual_description="Dreamy free features, questioning paradoxical eyes, natural sage's bearing",
    aliases=["Chuang Tzu", "莊子"],
    era="Warring States Period (369-286 BCE)",
    related_characters=["laozi"]
)

ZHANG_DAOLING_DESC = CharacterDescription(
    id="zhang_daoling",
    name_en="Zhang Daoling",
    name_ko="장도릉",
    tagline_en="First Celestial Master",
    tagline_ko="초대 천사",
    description_en="""Zhang Daoling (34-156 CE) founded the Way of the Celestial Masters, institutionalizing Taoism as an organized religion. He received revelation from Laozi and established talismans and exorcism rituals that continue today.""",
    description_ko="""장도릉(34-156)은 천사도를 창립하여, 도교를 조직화된 종교로 제도화했습니다. 그는 노자로부터 계시를 받고 오늘날까지 계속되는 부적과 퇴마 의식을 확립했습니다.""",
    traits_en=["Founding", "Exorcising", "Revealed", "Priestly", "Powerful"],
    traits_ko=["창립하는", "퇴마하는", "계시받은", "사제의", "강력한"],
    story_en="Zhang Daoling received the Tao from Laozi on Mount Heming, gaining power over demons and establishing the priesthood that continues through his descendants.",
    story_ko="장도릉은 학명산에서 노자로부터 도를 받아, 악마에 대한 힘을 얻고 그의 후손을 통해 계속되는 사제직을 확립했습니다.",
    match_message_en="You carry Zhang Daoling's priestly power—exorcising what afflicts and protecting with sacred arts.",
    match_message_ko="당신은 장도릉의 사제적 힘을 지니고 있습니다—고통을 주는 것을 퇴마하고 신성한 기술로 보호하는.",
    image_prompt="Taoist priest with tiger, holding demon-dispelling seal, celestial master's robes",
    visual_description="Powerful priestly features, exorcising authoritative eyes, celestial master's bearing",
    aliases=["Celestial Master Zhang", "張道陵"],
    era="Han Dynasty (34-156 CE)",
    related_characters=["laozi"]
)

EIGHT_IMMORTALS_LU_DESC = CharacterDescription(
    id="eight_immortals_lu",
    name_en="Lü Dongbin",
    name_ko="여동빈",
    tagline_en="Scholar-Immortal, Patron of Swordsmen",
    tagline_ko="학자 신선, 검객의 수호자",
    description_en="""Lü Dongbin is the most popular of the Eight Immortals of Taoism. A Tang dynasty scholar who achieved immortality, he carries a demon-slaying sword and represents the scholarly path to enlightenment.""",
    description_ko="""여동빈은 도교의 팔선 중 가장 인기 있는 인물입니다. 불멸을 얻은 당나라 학자로, 그는 퇴마검을 들고 깨달음에 이르는 학문적 길을 상징합니다.""",
    traits_en=["Scholarly", "Immortal", "Sword-bearing", "Alchemical", "Teaching"],
    traits_ko=["학문적인", "불멸의", "검을 든", "연금술적인", "가르치는"],
    story_en="Lü Dongbin passed ten trials given by his master before achieving immortality, proving that enlightenment requires dedication through any test.",
    story_ko="여동빈은 불멸을 얻기 전에 스승이 준 열 가지 시련을 통과하여, 깨달음은 어떤 시험에서도 헌신이 필요함을 증명했습니다.",
    match_message_en="You embody Lü Dongbin's scholarly immortality—achieving transcendence through learning and discipline.",
    match_message_ko="당신은 여동빈의 학자적 불멸을 구현합니다—학습과 수련을 통해 초월에 도달하는.",
    image_prompt="Chinese immortal scholar with demon-slaying sword, Taoist robes, transcendent expression",
    visual_description="Scholarly refined features, immortal transcendent eyes, sword-bearing sage's bearing",
    aliases=["呂洞賓", "Patriarch Lü"],
    era="Tang Dynasty Legend",
    related_characters=["zhongli_quan"]
)


# ============================================
# SOUTHEAST ASIAN
# ============================================

BARONG_DESC = CharacterDescription(
    id="barong",
    name_en="Barong",
    name_ko="바롱",
    tagline_en="King of Spirits, Lord of Good",
    tagline_ko="영혼의 왕, 선의 군주",
    description_en="""Barong is the king of spirits and leader of good forces in Balinese mythology. He appears as a lion-like creature in sacred dance dramas, eternally battling Rangda, the queen of evil.""",
    description_ko="""바롱은 발리 신화에서 영혼의 왕이자 선한 힘의 지도자입니다. 그는 신성한 무용극에서 사자 같은 생물로 나타나, 악의 여왕 랑다와 영원히 싸웁니다.""",
    traits_en=["Protective", "Good", "Lion-like", "Dancing", "Eternal"],
    traits_ko=["수호하는", "선한", "사자 같은", "춤추는", "영원한"],
    story_en="In every village, Barong dances to protect the people, eternally defeating Rangda only for the battle to begin again.",
    story_ko="모든 마을에서, 바롱은 사람들을 보호하기 위해 춤추며, 랑다를 영원히 물리치지만 전투는 다시 시작됩니다.",
    match_message_en="You embody Barong's protective power—the good that eternally stands against evil.",
    match_message_ko="당신은 바롱의 수호력을 구현합니다—악에 영원히 맞서는 선.",
    image_prompt="Balinese lion spirit with ornate mask and costume, protective dance pose, temple setting",
    visual_description="Lion-like majestic features, protective fierce eyes, dancing warrior's bearing",
    aliases=["Banaspati Raja"],
    era="Balinese Tradition",
    related_characters=["rangda"]
)

RANGDA_DESC = CharacterDescription(
    id="rangda",
    name_en="Rangda",
    name_ko="랑다",
    tagline_en="Queen of Demons, Mistress of Dark Magic",
    tagline_ko="악마의 여왕, 흑마법의 여주인",
    description_en="""Rangda is the demon queen of Balinese mythology, a terrifying witch who leads an army of evil spirits. She eternally battles Barong, representing the necessary balance between good and evil.""",
    description_ko="""랑다는 발리 신화의 악마 여왕으로, 악령 군대를 이끄는 무시무시한 마녀입니다. 그녀는 바롱과 영원히 싸우며, 선과 악 사이의 필요한 균형을 상징합니다.""",
    traits_en=["Terrifying", "Magical", "Queen", "Balancing", "Dark"],
    traits_ko=["무시무시한", "마법적인", "여왕", "균형 잡는", "어두운"],
    story_en="Rangda was once a queen whose grief and rage transformed her into the demon queen, showing how pain can corrupt even the powerful.",
    story_ko="랑다는 한때 슬픔과 분노가 그녀를 악마 여왕으로 변신시킨 여왕이었으며, 고통이 어떻게 강력한 자도 타락시킬 수 있는지 보여줍니다.",
    match_message_en="You carry Rangda's fierce power—the shadow that defines the light.",
    match_message_ko="당신은 랑다의 맹렬한 힘을 지니고 있습니다—빛을 정의하는 그림자.",
    image_prompt="Balinese demon queen with terrifying mask, long nails and tongue, dark magical presence",
    visual_description="Terrifying fierce features, dark powerful eyes, demon queen's bearing",
    aliases=["Widow Witch"],
    era="Balinese Tradition",
    related_characters=["barong"]
)

DEWI_SRI_DESC = CharacterDescription(
    id="dewi_sri",
    name_en="Dewi Sri",
    name_ko="데위 스리",
    tagline_en="Goddess of Rice and Fertility",
    tagline_ko="쌀과 다산의 여신",
    description_en="""Dewi Sri is the Indonesian goddess of rice and fertility, essential to the agricultural societies of Java and Bali. She represents the life-giving grain that sustains millions.""",
    description_ko="""데위 스리는 인도네시아의 쌀과 다산의 여신으로, 자바와 발리의 농경 사회에 필수적입니다. 그녀는 수백만을 먹여살리는 생명을 주는 곡물을 상징합니다.""",
    traits_en=["Nourishing", "Fertile", "Agricultural", "Essential", "Life-giving"],
    traits_ko=["영양을 주는", "다산의", "농업적인", "필수적인", "생명을 주는"],
    story_en="Dewi Sri's body became the rice plant after her death, giving herself completely to nourish humanity.",
    story_ko="데위 스리의 몸은 죽음 후 벼가 되어, 인류를 먹여살리기 위해 자신을 완전히 내주었습니다.",
    match_message_en="You embody Dewi Sri's nourishing sacrifice—giving life to sustain others.",
    match_message_ko="당신은 데위 스리의 양육하는 희생을 구현합니다—다른 이들을 지탱하기 위해 생명을 주는.",
    image_prompt="Beautiful Indonesian goddess among rice paddies, gentle nurturing expression",
    visual_description="Beautiful nurturing features, life-giving gentle eyes, agricultural goddess bearing",
    aliases=["Sri Devi", "Rice Mother"],
    era="Indonesian Tradition",
    related_characters=["vishnu"]
)

NAGA_DESC = CharacterDescription(
    id="naga",
    name_en="Naga",
    name_ko="나가",
    tagline_en="Serpent Spirit of Waters",
    tagline_ko="물의 뱀 정령",
    description_en="""Naga are serpentine beings of Southeast Asian mythology, guardians of rivers, lakes, and underground treasures. They can be benevolent protectors or fearsome when angered.""",
    description_ko="""나가는 동남아시아 신화의 뱀 형상 존재로, 강, 호수, 지하 보물의 수호자입니다. 그들은 자비로운 보호자일 수도 있고 화가 나면 무시무시할 수도 있습니다.""",
    traits_en=["Serpentine", "Guarding", "Water", "Treasure", "Dual-natured"],
    traits_ko=["뱀의", "수호하는", "물의", "보물의", "이중 본성의"],
    story_en="The Naga King spread his hood to shelter the Buddha from rain during meditation, showing that even serpent spirits honor enlightenment.",
    story_ko="나가 왕은 명상 중 부처를 비로부터 보호하기 위해 그의 두건을 펼쳤으며, 뱀 정령도 깨달음을 공경함을 보여주었습니다.",
    match_message_en="You carry the Naga's dual nature—protector of depths and guardian of treasures.",
    match_message_ko="당신은 나가의 이중 본성을 지니고 있습니다—깊이의 보호자이자 보물의 수호자.",
    image_prompt="Serpentine being with multiple cobra hoods, guarding water and treasure, Southeast Asian temple",
    visual_description="Serpentine regal features, guarding wise eyes, water-spirit's bearing",
    aliases=["Nak", "Phaya Nak"],
    era="Southeast Asian Tradition",
    related_characters=["buddha"]
)

THAO_MAHA_PHROM_DESC = CharacterDescription(
    id="thao_maha_phrom",
    name_en="Thao Maha Phrom",
    name_ko="타오 마하 프롬",
    tagline_en="Thai God of Creation and Fortune",
    tagline_ko="태국 창조와 행운의 신",
    description_en="""Thao Maha Phrom is the Thai representation of Brahma, worshipped for fortune and protection. The Erawan Shrine in Bangkok dedicated to him is one of the most visited religious sites in Thailand.""",
    description_ko="""타오 마하 프롬은 브라흐마의 태국식 표현으로, 행운과 보호를 위해 숭배됩니다. 그에게 헌정된 방콕의 에라완 사원은 태국에서 가장 많이 방문하는 종교 장소 중 하나입니다.""",
    traits_en=["Creating", "Fortune-giving", "Protecting", "Four-faced", "Worshipped"],
    traits_ko=["창조하는", "행운을 주는", "보호하는", "사면의", "숭배받는"],
    story_en="When misfortune struck the Erawan Hotel construction, a shrine to Thao Maha Phrom was built—and the project succeeded, beginning his popular worship.",
    story_ko="에라완 호텔 건설에 불운이 닥쳤을 때, 타오 마하 프롬에게 사원이 세워졌고—프로젝트가 성공하여, 그의 대중적 숭배가 시작되었습니다.",
    match_message_en="You radiate Thao Maha Phrom's creative fortune—blessing and protecting from all directions.",
    match_message_ko="당신은 타오 마하 프롬의 창조적 행운을 발산합니다—모든 방향에서 축복하고 보호하는.",
    image_prompt="Four-faced Thai deity in gold, blessing with all hands, Thai temple setting",
    visual_description="Serene four-faced features, blessing benevolent eyes, creator deity's bearing",
    aliases=["Phra Phrom", "Thai Brahma"],
    era="Thai Buddhism",
    related_characters=["brahma"]
)

SON_TINH_DESC = CharacterDescription(
    id="son_tinh",
    name_en="Son Tinh",
    name_ko="손띤",
    tagline_en="Mountain Spirit of Vietnam",
    tagline_ko="베트남의 산 정령",
    description_en="""Son Tinh is the mountain spirit of Vietnamese mythology who defeated the water spirit Thuy Tinh to win the hand of a princess. He represents the protective mountains that shield Vietnam from floods.""",
    description_ko="""손띤은 베트남 신화의 산 정령으로, 공주의 손을 얻기 위해 물 정령 투이띤을 물리쳤습니다. 그는 베트남을 홍수로부터 보호하는 보호적인 산을 상징합니다.""",
    traits_en=["Mountain", "Protective", "Victorious", "Solid", "Shielding"],
    traits_ko=["산의", "보호하는", "승리하는", "견고한", "막아주는"],
    story_en="Each year Thuy Tinh sends floods to attack Son Tinh's mountains, but the mountain spirit always raises his peaks higher, protecting the people below.",
    story_ko="매년 투이띤이 손띤의 산을 공격하기 위해 홍수를 보내지만, 산 정령은 항상 그의 봉우리를 더 높이 올려, 아래의 사람들을 보호합니다.",
    match_message_en="You embody Son Tinh's mountain strength—rising to protect against any flood.",
    match_message_ko="당신은 손띤의 산의 힘을 구현합니다—어떤 홍수에도 맞서 보호하기 위해 솟아오르는.",
    image_prompt="Vietnamese mountain spirit rising above floods, protective stance, mountain peaks",
    visual_description="Strong stable features, protective determined eyes, mountain spirit's bearing",
    aliases=["Sơn Tinh", "Mountain God"],
    era="Vietnamese Mythology",
    related_characters=["thuy_tinh"]
)

THUY_TINH_DESC = CharacterDescription(
    id="thuy_tinh",
    name_en="Thuy Tinh",
    name_ko="투이띤",
    tagline_en="Water Spirit of Vietnam",
    tagline_ko="베트남의 물 정령",
    description_en="""Thuy Tinh is the water spirit of Vietnamese mythology, rival of Son Tinh the mountain spirit. His annual attempts to flood the mountains represent the monsoon rains that threaten but ultimately nourish Vietnam.""",
    description_ko="""투이띤은 베트남 신화의 물 정령으로, 산 정령 손띤의 라이벌입니다. 산을 침수시키려는 그의 연례 시도는 베트남을 위협하지만 궁극적으로 양육하는 몬순 비를 상징합니다.""",
    traits_en=["Water", "Stormy", "Persistent", "Necessary", "Flooding"],
    traits_ko=["물의", "폭풍우의", "끈질긴", "필요한", "범람하는"],
    story_en="Though he never wins against Son Tinh, Thuy Tinh's waters are necessary—for the same rains that flood also make the rice grow.",
    story_ko="손띤에게 결코 이기지 못하지만, 투이띤의 물은 필요합니다—왜냐하면 홍수를 일으키는 같은 비가 또한 벼를 자라게 하기 때문입니다.",
    match_message_en="You carry Thuy Tinh's persistent power—necessary waters that sustain even as they challenge.",
    match_message_ko="당신은 투이띤의 끈질긴 힘을 지니고 있습니다—도전하면서도 지탱하는 필요한 물.",
    image_prompt="Vietnamese water spirit commanding waves and rain, stormy yet life-giving, ocean and river",
    visual_description="Flowing fluid features, stormy persistent eyes, water spirit's bearing",
    aliases=["Thủy Tinh", "Water God"],
    era="Vietnamese Mythology",
    related_characters=["son_tinh"]
)

ABE_NO_SEIMEI_DESC = CharacterDescription(
    id="abe_no_seimei",
    name_en="Abe no Seimei",
    name_ko="아베노 세이메이",
    tagline_en="Greatest Onmyoji of Japan",
    tagline_ko="일본 최고의 음양사",
    description_en="""Abe no Seimei (921-1005) was the legendary Japanese onmyoji (yin-yang master) renowned for his divination and supernatural powers. He was said to be the son of a fox spirit, giving him power over the spirit world.""",
    description_ko="""아베노 세이메이(921-1005)는 점술과 초자연적 능력으로 유명한 전설적인 일본 음양사입니다. 그는 여우 정령의 아들로 여겨져, 영계에 대한 힘을 가졌습니다.""",
    traits_en=["Mystical", "Divining", "Half-spirit", "Powerful", "Legendary"],
    traits_ko=["신비적인", "점치는", "반정령", "강력한", "전설적인"],
    story_en="Seimei could see spirits invisible to others and command shikigami—paper spirits that served his every command.",
    story_ko="세이메이는 다른 이들에게 보이지 않는 영혼을 볼 수 있었고, 그의 모든 명령을 따르는 종이 정령인 식신을 부릴 수 있었습니다.",
    match_message_en="You possess Seimei's mystical sight—seeing what is hidden from others.",
    match_message_ko="당신은 세이메이의 신비적인 시야를 지니고 있습니다—다른 이들에게 숨겨진 것을 보는.",
    image_prompt="Heian period Japanese mystic in court robes, five-pointed star symbol, shikigami spirits",
    visual_description="Refined mystical features, spirit-seeing eyes, onmyoji's powerful bearing",
    aliases=["安倍晴明", "Seimei"],
    era="Heian Period (921-1005)",
    related_characters=["kuzunoha"]
)

TOMOE_GOZEN_DESC = CharacterDescription(
    id="tomoe_gozen",
    name_en="Tomoe Gozen",
    name_ko="토모에 고젠",
    tagline_en="Female Samurai Warrior",
    tagline_ko="여성 사무라이 전사",
    description_en="""Tomoe Gozen was a legendary female samurai of 12th century Japan, renowned for her skill with bow, sword, and horseback combat. She was worth a thousand warriors, fighting in the Genpei War.""",
    description_ko="""토모에 고젠은 12세기 일본의 전설적인 여성 사무라이로, 활, 검, 기마 전투에서의 실력으로 유명했습니다. 그녀는 겐페이 전쟁에서 싸우며 천 명의 전사 가치가 있었습니다.""",
    traits_en=["Warrior", "Beautiful", "Skilled", "Brave", "Legendary"],
    traits_ko=["전사적인", "아름다운", "숙련된", "용감한", "전설적인"],
    story_en="In her final battle, Tomoe charged into the enemy alone, taking a commander's head before disappearing into legend.",
    story_ko="마지막 전투에서, 토모에는 홀로 적진으로 돌격하여 지휘관의 목을 베고 전설 속으로 사라졌습니다.",
    match_message_en="You embody Tomoe's warrior beauty—skill and courage that equals any man.",
    match_message_ko="당신은 토모에의 전사적 아름다움을 구현합니다—어떤 남자와도 동등한 기술과 용기.",
    image_prompt="Female Japanese samurai on horseback, bow and sword, beautiful fierce expression",
    visual_description="Beautiful fierce features, warrior's determined eyes, mounted samurai's bearing",
    aliases=["巴御前"],
    era="Genpei War (12th century)",
    related_characters=["minamoto_yoshinaka"]
)

SPIDER_GRANDMOTHER_DESC = CharacterDescription(
    id="spider_grandmother",
    name_en="Spider Grandmother",
    name_ko="거미 할머니",
    tagline_en="Creator and Teacher of the Peoples",
    tagline_ko="민족들의 창조자이자 스승",
    description_en="""Spider Grandmother is the creator deity in Hopi and Navajo traditions. She wove the world into being and taught the people how to weave, make pottery, and live in harmony with the earth.""",
    description_ko="""거미 할머니는 호피와 나바호 전통의 창조신입니다. 그녀는 세상을 짜서 존재하게 했고, 사람들에게 직조, 도자기 만들기, 땅과 조화롭게 사는 방법을 가르쳤습니다.""",
    traits_en=["Creating", "Weaving", "Teaching", "Wise", "Guiding"],
    traits_ko=["창조하는", "짜는", "가르치는", "지혜로운", "인도하는"],
    story_en="Spider Grandmother wove the web of the universe, connecting all things. She taught the people that they too are weavers of their own destiny.",
    story_ko="거미 할머니는 우주의 그물을 짜서 모든 것을 연결했습니다. 그녀는 사람들에게 그들도 자신의 운명의 직조공이라고 가르쳤습니다.",
    match_message_en="You weave with Spider Grandmother's wisdom—connecting and creating patterns that endure.",
    match_message_ko="당신은 거미 할머니의 지혜로 짭니다—지속되는 패턴을 연결하고 창조하는.",
    image_prompt="Wise Native American elder with spider imagery, weaving creation, teaching presence",
    visual_description="Ancient wise features, creating teaching eyes, weaver grandmother's bearing",
    aliases=["Kokyangwuti", "Spider Woman"],
    era="Hopi/Navajo Tradition",
    related_characters=["coyote"]
)

THUNDERBIRD_DESC = CharacterDescription(
    id="thunderbird",
    name_en="Thunderbird",
    name_ko="천둥새",
    tagline_en="Bringer of Storms, Spirit of Power",
    tagline_ko="폭풍의 전달자, 힘의 정령",
    description_en="""The Thunderbird is a powerful spirit in many Native American traditions, a great bird whose wings create thunder and whose eyes flash lightning. It is a protector of humanity against evil spirits.""",
    description_ko="""천둥새는 많은 아메리카 원주민 전통에서 강력한 정령으로, 날개가 천둥을 만들고 눈이 번개를 번쩍이는 거대한 새입니다. 악령에 대항하여 인류를 보호합니다.""",
    traits_en=["Thunderous", "Powerful", "Protecting", "Storm-bringing", "Majestic"],
    traits_ko=["천둥 같은", "강력한", "보호하는", "폭풍을 가져오는", "장엄한"],
    story_en="When Thunderbird spreads its wings, storms come; when it closes its eyes, lightning strikes. It wages eternal war against the underwater serpents that threaten the world.",
    story_ko="천둥새가 날개를 펼치면 폭풍이 오고, 눈을 감으면 번개가 칩니다. 세상을 위협하는 물속 뱀들에 대항하여 영원한 전쟁을 벌입니다.",
    match_message_en="You carry Thunderbird's storm power—protection that comes with thunder and lightning.",
    match_message_ko="당신은 천둥새의 폭풍 힘을 지니고 있습니다—천둥과 번개와 함께 오는 보호.",
    image_prompt="Massive supernatural eagle with lightning in eyes, thunder from wings, protective storm spirit",
    visual_description="Majestic eagle features, lightning-flash eyes, thunderous protective bearing",
    aliases=["Wakinyan", "Thunder Being"],
    era="Native American Tradition",
    related_characters=["spider_grandmother"]
)

HINA_DESC = CharacterDescription(
    id="hina",
    name_en="Hina",
    name_ko="히나",
    tagline_en="Moon Goddess of Polynesia",
    tagline_ko="폴리네시아의 달의 여신",
    description_en="""Hina is the Polynesian goddess of the moon and women. She is often associated with weaving and tapa cloth making, working by the light of the moon she inhabits.""",
    description_ko="""히나는 폴리네시아의 달과 여성의 여신입니다. 그녀는 종종 직조와 타파 천 만들기와 연관되며, 그녀가 거주하는 달빛 아래에서 일합니다.""",
    traits_en=["Lunar", "Weaving", "Feminine", "Patient", "Illuminating"],
    traits_ko=["달의", "직조하는", "여성적인", "인내하는", "비추는"],
    story_en="Hina fled to the moon to escape the demands of her earthly life, where she can be seen still weaving by the silver light.",
    story_ko="히나는 지상 생활의 요구에서 벗어나기 위해 달로 도망쳤고, 은빛 아래에서 여전히 직조하는 모습을 볼 수 있습니다.",
    match_message_en="You shine with Hina's lunar patience—working steadily through the night.",
    match_message_ko="당신은 히나의 달의 인내로 빛납니다—밤새 꾸준히 일하는.",
    image_prompt="Polynesian moon goddess weaving by moonlight, serene feminine presence, silver lunar glow",
    visual_description="Beautiful serene features, patient lunar eyes, weaving goddess bearing",
    aliases=["Sina", "Ina"],
    era="Polynesian Tradition",
    related_characters=["maui", "tangaroa"]
)

TANGAROA_DESC = CharacterDescription(
    id="tangaroa",
    name_en="Tangaroa",
    name_ko="탕가로아",
    tagline_en="God of the Sea and Fish",
    tagline_ko="바다와 물고기의 신",
    description_en="""Tangaroa is the great sea god of Polynesian mythology, father of fish and lord of the ocean. In some traditions, he is a creator god who separated the primordial parents to bring light to the world.""",
    description_ko="""탕가로아는 폴리네시아 신화의 위대한 바다 신으로, 물고기의 아버지이자 대양의 주인입니다. 일부 전통에서, 그는 세상에 빛을 가져오기 위해 원초적 부모를 분리한 창조신입니다.""",
    traits_en=["Oceanic", "Creating", "Father", "Vast", "Primordial"],
    traits_ko=["대양의", "창조하는", "아버지의", "광대한", "원초적인"],
    story_en="All fish are children of Tangaroa, and fishermen must honor him to ensure good catches from his endless domain.",
    story_ko="모든 물고기는 탕가로아의 자녀이며, 어부들은 그의 끝없는 영역에서 좋은 어획을 보장하기 위해 그를 공경해야 합니다.",
    match_message_en="You embody Tangaroa's oceanic vastness—providing and creating from endless depths.",
    match_message_ko="당신은 탕가로아의 대양의 광대함을 구현합니다—끝없는 깊이에서 제공하고 창조하는.",
    image_prompt="Polynesian sea god rising from waves, fish surrounding, vast ocean power",
    visual_description="Powerful oceanic features, vast deep eyes, sea god's bearing",
    aliases=["Tagaloa", "Kanaloa"],
    era="Polynesian Tradition",
    related_characters=["maui", "hina"]
)


# Export dictionary for registry
ADDITIONAL3_DESCRIPTIONS: dict[str, CharacterDescription] = {
    # Persian
    "mithra": MITHRA_DESC,
    "anahita": ANAHITA_DESC,
    "rostam": ROSTAM_DESC,
    "cyrus_the_great": CYRUS_THE_GREAT_DESC,
    # Chinese Additional
    "liu_bei": LIU_BEI_DESC,
    "mulan": MULAN_DESC,
    "white_snake": WHITE_SNAKE_DESC,
    "xu_xian": XU_XIAN_DESC,
    "mencius": MENCIUS_DESC,
    "zhuxi": ZHUXI_DESC,
    # Taoist
    "zhuangzi": ZHUANGZI_DESC,
    "zhang_daoling": ZHANG_DAOLING_DESC,
    "eight_immortals_lu": EIGHT_IMMORTALS_LU_DESC,
    # Southeast Asian
    "barong": BARONG_DESC,
    "rangda": RANGDA_DESC,
    "dewi_sri": DEWI_SRI_DESC,
    "naga": NAGA_DESC,
    "thao_maha_phrom": THAO_MAHA_PHROM_DESC,
    "son_tinh": SON_TINH_DESC,
    "thuy_tinh": THUY_TINH_DESC,
    # Japanese Additional
    "abe_no_seimei": ABE_NO_SEIMEI_DESC,
    "tomoe_gozen": TOMOE_GOZEN_DESC,
    # Native American
    "spider_grandmother": SPIDER_GRANDMOTHER_DESC,
    "thunderbird": THUNDERBIRD_DESC,
    # Polynesian
    "hina": HINA_DESC,
    "tangaroa": TANGAROA_DESC,
}
