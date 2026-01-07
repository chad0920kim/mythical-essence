"""
Character Descriptions Database
Contains detailed descriptions for all mythological figures in multiple languages
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CharacterDescription:
    """Detailed description for a mythological character."""
    id: str

    # Basic info (used for all languages as fallback)
    name_en: str
    name_ko: str

    # Short tagline (1 line)
    tagline_en: str
    tagline_ko: str

    # Main description (2-3 paragraphs)
    description_en: str
    description_ko: str

    # Personality traits (3-5 keywords)
    traits_en: list[str]
    traits_ko: list[str]

    # Famous story or legend
    story_en: str
    story_ko: str

    # Match message (shown when user matches with this character)
    match_message_en: str
    match_message_ko: str

    # Image generation prompt (for AI image generation)
    image_prompt: str

    # Visual description for face matching
    visual_description: str

    # Additional names/aliases
    aliases: list[str] = field(default_factory=list)

    # Historical period (if applicable)
    era: Optional[str] = None

    # Related characters
    related_characters: list[str] = field(default_factory=list)


# ============================================
# GREEK MYTHOLOGY DESCRIPTIONS
# ============================================

ZEUS_DESC = CharacterDescription(
    id="zeus",
    name_en="Zeus",
    name_ko="제우스",
    tagline_en="King of the Olympian Gods, Ruler of Sky and Thunder",
    tagline_ko="올림포스의 신들의 왕, 하늘과 번개의 지배자",
    description_en="""Zeus is the supreme deity of the Greek pantheon, ruling over Mount Olympus as the king of all gods. He overthrew his father Cronus to claim dominion over the sky and thunder, wielding his mighty thunderbolt as the ultimate symbol of divine authority.

Known for his commanding presence and absolute power, Zeus maintains cosmic order while presiding over justice, hospitality, and oaths. His judgments are final, and his word is law among both gods and mortals.

Despite his regal bearing, Zeus is also known for his passionate nature and numerous romantic entanglements, which have given rise to many of mythology's greatest heroes and tragic tales.""",
    description_ko="""제우스는 그리스 신화의 최고신으로, 올림포스 산에서 모든 신들의 왕으로 군림합니다. 그는 아버지 크로노스를 물리치고 하늘과 번개에 대한 지배권을 얻었으며, 강력한 번개를 신성한 권위의 상징으로 사용합니다.

위압적인 존재감과 절대적인 권력으로 알려진 제우스는 우주의 질서를 유지하면서 정의, 환대, 맹세를 관장합니다. 그의 판결은 최종적이며, 그의 말은 신과 인간 모두에게 법과 같습니다.

왕다운 품격에도 불구하고, 제우스는 열정적인 성격과 수많은 연애로도 유명하며, 이는 신화 속 위대한 영웅들과 비극적인 이야기들의 기원이 되었습니다.""",
    traits_en=["Authoritative", "Powerful", "Just", "Passionate", "Commanding"],
    traits_ko=["권위적인", "강력한", "공정한", "열정적인", "위엄있는"],
    story_en="Zeus led the Olympians in the Titanomachy, a great war against the Titans. After a decade of fierce battle, he emerged victorious and divided the cosmos with his brothers—Poseidon received the seas, Hades the underworld, while Zeus claimed the sky and became supreme ruler of all.",
    story_ko="제우스는 타이탄과의 대전쟁인 티타노마키아에서 올림포스 신들을 이끌었습니다. 10년간의 치열한 전투 끝에 승리를 거두고 형제들과 우주를 나누었습니다. 포세이돈은 바다를, 하데스는 지하세계를, 그리고 제우스는 하늘을 차지하여 모든 것의 최고 지배자가 되었습니다.",
    match_message_en="You possess the commanding presence of a born leader. Like Zeus, you carry an air of natural authority that others instinctively respect. Your strong features reflect inner strength and the capacity to make decisive judgments.",
    match_message_ko="당신은 타고난 지도자의 위엄 있는 존재감을 지니고 있습니다. 제우스처럼, 다른 사람들이 본능적으로 존경하는 자연스러운 권위의 아우라를 가지고 있습니다. 당신의 강인한 이목구비는 내면의 힘과 결단력 있는 판단을 내리는 능력을 반영합니다.",
    image_prompt="Majestic bearded man with silver-white hair, wearing golden crown and royal purple robes, holding a glowing lightning bolt, seated on a marble throne among clouds on Mount Olympus, divine golden light, ancient Greek aesthetic, highly detailed portrait, dramatic lighting",
    visual_description="Strong square jaw, deep-set commanding eyes, prominent brow, distinguished beard, mature but powerful features, intense authoritative gaze",
    aliases=["Jupiter", "Jove", "Dias"],
    era="Ancient Greece",
    related_characters=["hera", "poseidon", "hades", "athena", "apollo"]
)

ATHENA_DESC = CharacterDescription(
    id="athena",
    name_en="Athena",
    name_ko="아테나",
    tagline_en="Goddess of Wisdom, Strategic Warfare, and Crafts",
    tagline_ko="지혜, 전략적 전쟁, 기술의 여신",
    description_en="""Athena is the revered goddess of wisdom, courage, and strategic warfare in Greek mythology. Born fully armored from Zeus's head, she embodies the perfect union of intellect and strength, representing civilization's highest ideals.

Unlike Ares who represents the brutal chaos of war, Athena champions strategic thinking, just causes, and the defense of cities. She is the patron of heroes, guiding them with her wisdom and protecting them with her aegis.

As goddess of crafts and practical arts, Athena also represents the civilizing influence of skill and knowledge, from weaving to shipbuilding to agriculture.""",
    description_ko="""아테나는 그리스 신화에서 지혜, 용기, 전략적 전쟁의 여신으로 숭배받습니다. 제우스의 머리에서 완전무장한 채로 태어난 그녀는 지성과 힘의 완벽한 결합을 구현하며, 문명의 가장 높은 이상을 대표합니다.

전쟁의 잔인한 혼돈을 상징하는 아레스와 달리, 아테나는 전략적 사고, 정당한 대의, 도시의 방어를 옹호합니다. 그녀는 영웅들의 수호자로서 지혜로 그들을 인도하고 아이기스로 보호합니다.

기술과 실용 예술의 여신으로서, 아테나는 직조부터 조선, 농업에 이르기까지 기술과 지식의 문명화 영향을 대표합니다.""",
    traits_en=["Wise", "Strategic", "Just", "Skilled", "Protective"],
    traits_ko=["지혜로운", "전략적인", "공정한", "숙련된", "보호하는"],
    story_en="Athena competed with Poseidon for patronage of Athens. While Poseidon struck his trident to create a salt spring, Athena planted an olive tree—a gift of peace, food, and prosperity. The Athenians chose Athena, and the city bears her name to this day.",
    story_ko="아테나는 아테네의 수호신 자리를 놓고 포세이돈과 경쟁했습니다. 포세이돈이 삼지창으로 소금 샘을 만들어낸 반면, 아테나는 올리브 나무를 심었습니다—평화, 식량, 번영의 선물이었습니다. 아테네인들은 아테나를 선택했고, 그 도시는 오늘날까지 그녀의 이름을 따릅니다.",
    match_message_en="Your features reflect the sharp intellect and composed wisdom of Athena. You possess both the keen analytical mind and the quiet confidence of one who thinks before acting. Your gaze speaks of strategic depth and considered judgment.",
    match_message_ko="당신의 이목구비는 아테나의 날카로운 지성과 차분한 지혜를 반영합니다. 행동하기 전에 생각하는 사람의 예리한 분석력과 조용한 자신감을 모두 갖추고 있습니다. 당신의 눈빛은 전략적 깊이와 신중한 판단력을 말해줍니다.",
    image_prompt="Noble Greek goddess with piercing grey eyes, wearing golden helmet with crest, silver armor over white robes, holding spear and aegis shield with Medusa's head, owl perched nearby, olive branch, ancient Athens temple background, wise and powerful expression, detailed classical Greek art style",
    visual_description="Oval face with refined features, bright intelligent grey eyes, straight nose, balanced symmetrical features, composed serene expression, noble bearing",
    aliases=["Minerva", "Pallas Athena", "Athene"],
    era="Ancient Greece",
    related_characters=["zeus", "poseidon", "ares", "apollo", "hermes"]
)

APOLLO_DESC = CharacterDescription(
    id="apollo",
    name_en="Apollo",
    name_ko="아폴론",
    tagline_en="God of Sun, Music, Poetry, and Healing",
    tagline_ko="태양, 음악, 시, 치유의 신",
    description_en="""Apollo is one of the most important and complex of the Olympian deities, embodying the ideal of masculine beauty and excellence. As the god of the sun, he drives his golden chariot across the sky each day, bringing light and warmth to the world.

Beyond his solar duties, Apollo is the patron of music, poetry, and the arts. His lyre produces the most beautiful music ever heard, and he leads the Muses in their celestial performances. He also embodies prophecy and truth, speaking through the Oracle at Delphi.

As a god of healing and medicine, Apollo taught humanity the art of medicine, though his arrows could also bring plague. This duality reflects his nature as a god of both creation and destruction.""",
    description_ko="""아폴론은 올림포스 신들 중 가장 중요하고 복잡한 신으로, 남성적 아름다움과 탁월함의 이상을 구현합니다. 태양의 신으로서 그는 매일 황금 전차를 타고 하늘을 가로질러 세상에 빛과 온기를 가져다줍니다.

태양의 임무 외에도, 아폴론은 음악, 시, 예술의 수호신입니다. 그의 리라는 세상에서 가장 아름다운 음악을 연주하며, 그는 뮤즈들의 천상의 공연을 이끕니다. 또한 예언과 진실을 구현하며, 델포이의 신탁을 통해 말합니다.

치유와 의술의 신으로서, 아폴론은 인류에게 의술을 가르쳤지만, 그의 화살은 역병을 가져올 수도 있었습니다. 이 이중성은 창조와 파괴 모두의 신으로서의 그의 본성을 반영합니다.""",
    traits_en=["Radiant", "Artistic", "Prophetic", "Healing", "Perfect"],
    traits_ko=["빛나는", "예술적인", "예언적인", "치유하는", "완벽한"],
    story_en="Apollo fell deeply in love with Daphne, a river nymph. When he pursued her, she called upon her father to save her, and was transformed into a laurel tree. Heartbroken, Apollo declared the laurel sacred and wore its leaves as a crown forever after.",
    story_ko="아폴론은 강의 님프인 다프네와 깊은 사랑에 빠졌습니다. 그가 그녀를 쫓자, 그녀는 아버지에게 구원을 요청했고, 월계수로 변했습니다. 상심한 아폴론은 월계수를 신성한 것으로 선언하고 영원히 그 잎으로 만든 관을 썼습니다.",
    match_message_en="Your features radiate the harmonious beauty of Apollo. There is a luminous quality to your appearance, a perfect balance that speaks of artistic sensibility and inner light. You carry the brightness of one touched by creative inspiration.",
    match_message_ko="당신의 이목구비는 아폴론의 조화로운 아름다움을 발산합니다. 당신의 외모에는 빛나는 품질이 있으며, 예술적 감수성과 내면의 빛을 말해주는 완벽한 균형이 있습니다. 창조적 영감에 닿은 사람의 밝음을 지니고 있습니다.",
    image_prompt="Ideally beautiful young Greek god with golden hair like sunbeams, perfect symmetrical features, wearing white and gold robes, holding golden lyre, laurel wreath crown, radiant golden aura like the sun, standing in a sunlit temple, classical Greek sculptural beauty",
    visual_description="Perfect oval face, bright wide eyes, ideally proportioned features, golden complexion, radiant and youthful appearance, harmonious symmetry",
    aliases=["Phoebus", "Phoebus Apollo"],
    era="Ancient Greece",
    related_characters=["artemis", "zeus", "dionysus", "hermes", "athena"]
)

APHRODITE_DESC = CharacterDescription(
    id="aphrodite",
    name_en="Aphrodite",
    name_ko="아프로디테",
    tagline_en="Goddess of Love, Beauty, and Desire",
    tagline_ko="사랑, 아름다움, 욕망의 여신",
    description_en="""Aphrodite is the goddess of love, beauty, pleasure, and passion in Greek mythology. Born from the sea foam near Cyprus, she emerged as the most beautiful being in existence, capable of inspiring desire in all who beheld her.

Her power extends beyond mere physical attraction to encompass all forms of love and connection. She influences romantic love, friendship, and even the bonds between parents and children. Her golden girdle has the power to make anyone fall in love.

Despite her association with pleasure, Aphrodite also represents the transformative and sometimes destructive power of love. She understands that true beauty comes from within and that love can be both humanity's greatest gift and its most formidable challenge.""",
    description_ko="""아프로디테는 그리스 신화에서 사랑, 아름다움, 쾌락, 열정의 여신입니다. 키프로스 근처의 바다 거품에서 태어난 그녀는 존재하는 모든 것 중 가장 아름다운 존재로 나타났으며, 그녀를 바라보는 모든 이에게 욕망을 불러일으킬 수 있었습니다.

그녀의 힘은 단순한 육체적 매력을 넘어 모든 형태의 사랑과 연결을 포함합니다. 그녀는 낭만적 사랑, 우정, 심지어 부모와 자녀 사이의 유대에도 영향을 미칩니다. 그녀의 황금 허리띠는 누구든 사랑에 빠지게 만드는 힘이 있습니다.

쾌락과의 연관에도 불구하고, 아프로디테는 사랑의 변형적이고 때로는 파괴적인 힘도 대표합니다. 그녀는 진정한 아름다움이 내면에서 온다는 것과 사랑이 인류의 가장 큰 선물이자 가장 큰 도전이 될 수 있음을 이해합니다.""",
    traits_en=["Beautiful", "Passionate", "Alluring", "Graceful", "Transformative"],
    traits_ko=["아름다운", "열정적인", "매혹적인", "우아한", "변화를 주는"],
    story_en="When Paris of Troy was asked to judge who was the most beautiful goddess—Hera, Athena, or Aphrodite—each offered him a bribe. Aphrodite promised him the most beautiful woman in the world: Helen. Paris chose Aphrodite, sparking the Trojan War.",
    story_ko="트로이의 파리스가 헤라, 아테나, 아프로디테 중 가장 아름다운 여신을 판정하라는 요청을 받았을 때, 각각이 그에게 뇌물을 제안했습니다. 아프로디테는 세상에서 가장 아름다운 여인 헬레네를 약속했습니다. 파리스는 아프로디테를 선택했고, 이것이 트로이 전쟁의 불씨가 되었습니다.",
    match_message_en="Your features embody the captivating grace of Aphrodite. There is an undeniable magnetism in your appearance, a soft beauty that draws others naturally. Your face speaks of one who understands the power of genuine connection and heartfelt emotion.",
    match_message_ko="당신의 이목구비는 아프로디테의 매혹적인 우아함을 구현합니다. 당신의 외모에는 부인할 수 없는 매력이 있으며, 다른 사람들을 자연스럽게 끌어당기는 부드러운 아름다움이 있습니다. 당신의 얼굴은 진정한 연결과 진심 어린 감정의 힘을 이해하는 사람을 말해줍니다.",
    image_prompt="Breathtakingly beautiful Greek goddess emerging from sea foam, flowing golden hair, perfect soft features, wearing flowing white and pink robes, golden jewelry, surrounded by roses and doves, seashells and pearls, soft romantic lighting, idealized feminine beauty, Renaissance painting style",
    visual_description="Heart-shaped face, soft wide eyes, full lips, delicate features, perfect symmetry, graceful expression, captivating gentle gaze",
    aliases=["Venus", "Cytherea", "Cypris"],
    era="Ancient Greece",
    related_characters=["ares", "hephaestus", "eros", "helen", "paris"]
)

POSEIDON_DESC = CharacterDescription(
    id="poseidon",
    name_en="Poseidon",
    name_ko="포세이돈",
    tagline_en="God of the Sea, Earthquakes, and Horses",
    tagline_ko="바다, 지진, 말의 신",
    description_en="""Poseidon is the mighty god of the sea, one of the three sons of Cronus who divided the cosmos after defeating the Titans. With his powerful trident, he commands all waters, from the smallest stream to the vast ocean depths.

Known for his temperamental nature, Poseidon can be as calm as a peaceful lagoon or as violent as a raging storm. When angered, he strikes the earth with his trident, causing earthquakes and shipwrecks. Sailors pray to him for safe passage across the treacherous seas.

Beyond the waves, Poseidon is also the creator and tamer of horses, which he gave to humanity. His palace lies deep beneath the Aegean Sea, built of coral and adorned with pearls.""",
    description_ko="""포세이돈은 강력한 바다의 신으로, 타이탄을 물리친 후 우주를 나눈 크로노스의 세 아들 중 하나입니다. 그의 강력한 삼지창으로 그는 가장 작은 시내부터 광활한 심해까지 모든 물을 지배합니다.

변덕스러운 성격으로 알려진 포세이돈은 평화로운 석호처럼 고요할 수도 있고 맹렬한 폭풍처럼 격렬할 수도 있습니다. 화가 나면 삼지창으로 땅을 내리쳐 지진과 난파선을 일으킵니다. 선원들은 위험한 바다를 안전하게 건너기 위해 그에게 기도합니다.

파도 너머, 포세이돈은 또한 말의 창조자이자 조련사로, 인류에게 말을 선물했습니다. 그의 궁전은 에게해 깊은 곳에 있으며, 산호로 지어지고 진주로 장식되어 있습니다.""",
    traits_en=["Powerful", "Temperamental", "Majestic", "Unpredictable", "Commanding"],
    traits_ko=["강력한", "변덕스러운", "장엄한", "예측불가한", "지배적인"],
    story_en="When Odysseus blinded Poseidon's son, the cyclops Polyphemus, the sea god's wrath knew no bounds. For ten long years, Poseidon prevented Odysseus from returning home, sending storms, sea monsters, and disasters to thwart his every attempt.",
    story_ko="오디세우스가 포세이돈의 아들인 외눈박이 거인 폴리페모스의 눈을 멀게 했을 때, 바다의 신의 분노는 한계가 없었습니다. 10년 동안, 포세이돈은 오디세우스가 집으로 돌아가는 것을 막으며 폭풍, 바다 괴물, 재앙을 보내 그의 모든 시도를 좌절시켰습니다.",
    match_message_en="Your features carry the depth and power of Poseidon. There is an oceanic quality to your presence—vast, commanding, and filled with untold depths. Your strong features speak of one who can weather any storm.",
    match_message_ko="당신의 이목구비는 포세이돈의 깊이와 힘을 담고 있습니다. 당신의 존재감에는 해양적인 품질이 있습니다—광대하고, 위엄 있고, 말할 수 없는 깊이로 가득합니다. 당신의 강한 이목구비는 어떤 폭풍도 견딜 수 있는 사람을 말해줍니다.",
    image_prompt="Powerful Greek god with wild sea-foam colored hair and beard, deep blue-green eyes like the ocean, muscular build, holding golden trident, wearing flowing robes of sea-green and blue, surrounded by crashing waves and sea creatures, underwater palace in background, dramatic stormy lighting",
    visual_description="Square strong jaw, deep-set intense eyes, prominent weathered features, powerful build, wild flowing hair, commanding authoritative expression",
    aliases=["Neptune", "Earth-Shaker", "Hippios"],
    era="Ancient Greece",
    related_characters=["zeus", "hades", "amphitrite", "triton", "polyphemus"]
)


HERA_DESC = CharacterDescription(
    id="hera",
    name_en="Hera",
    name_ko="헤라",
    tagline_en="Queen of the Gods, Goddess of Marriage and Family",
    tagline_ko="신들의 여왕, 결혼과 가족의 여신",
    description_en="""Hera is the queen of the Olympian gods and the goddess of marriage, women, childbirth, and family. As Zeus's wife and sister, she rules alongside him from Mount Olympus, embodying the sanctity of marriage despite her husband's many infidelities.

Known for her majestic beauty and regal bearing, Hera is the most powerful goddess of the Greek pantheon. Her symbols include the peacock, whose many-eyed tail feathers represent her watchfulness, and the cow, symbolizing her nurturing nature.

Though often portrayed as jealous and vengeful toward Zeus's lovers and illegitimate children, Hera's wrath represents the defense of the marital bond. She is fiercely protective of legitimate marriage and the stability of family, punishing those who violate these sacred institutions.""",
    description_ko="""헤라는 올림포스 신들의 여왕이자 결혼, 여성, 출산, 가족의 여신입니다. 제우스의 아내이자 누이로서, 남편의 많은 불륜에도 불구하고 결혼의 신성함을 구현하며 올림포스 산에서 함께 통치합니다.

장엄한 아름다움과 왕족다운 품위로 알려진 헤라는 그리스 판테온에서 가장 강력한 여신입니다. 그녀의 상징으로는 그녀의 경계심을 나타내는 많은 눈 모양의 꼬리 깃털을 가진 공작과 양육적 본성을 상징하는 소가 있습니다.

종종 제우스의 연인들과 사생아들에 대해 질투심 많고 복수심 강한 것으로 묘사되지만, 헤라의 분노는 결혼 유대의 수호를 대표합니다. 그녀는 정당한 결혼과 가족의 안정을 맹렬하게 보호하며, 이러한 신성한 제도를 위반하는 자들을 벌합니다.""",
    traits_en=["Regal", "Protective", "Jealous", "Powerful", "Loyal"],
    traits_ko=["왕족다운", "보호하는", "질투하는", "강력한", "충성스러운"],
    story_en="When Zeus courted Hera, she initially rejected him. Zeus transformed into a wounded cuckoo bird, and when the compassionate Hera held him to her breast, he revealed himself and won her. Their sacred wedding lasted 300 years.",
    story_ko="제우스가 헤라에게 구애했을 때, 그녀는 처음에 거절했습니다. 제우스는 다친 뻐꾸기로 변신했고, 자비로운 헤라가 그를 가슴에 안았을 때 정체를 드러내 그녀를 얻었습니다. 그들의 신성한 결혼식은 300년 동안 지속되었습니다.",
    match_message_en="Your features carry the regal dignity of Hera. There is a commanding presence to your appearance—the look of one who demands respect and loyalty. Your face speaks of one who fiercely protects what they hold sacred.",
    match_message_ko="당신의 이목구비는 헤라의 왕족다운 존엄을 담고 있습니다. 당신의 외모에는 위엄 있는 존재감이 있습니다—존경과 충성을 요구하는 사람의 모습. 당신의 얼굴은 자신이 신성하게 여기는 것을 맹렬하게 보호하는 사람을 말해줍니다.",
    image_prompt="Majestic Greek goddess with crown and flowing robes of royal purple and gold, holding lotus-tipped scepter, peacocks surrounding her, beautiful but stern expression, Mount Olympus throne room, regal queenly bearing",
    visual_description="Noble oval face, large proud eyes, elegant features with stern beauty, expression of authority and dignity",
    aliases=["Juno", "Queen of Heaven"],
    era="Ancient Greece",
    related_characters=["zeus", "athena", "ares", "hephaestus", "hercules"]
)

ARTEMIS_DESC = CharacterDescription(
    id="artemis",
    name_en="Artemis",
    name_ko="아르테미스",
    tagline_en="Goddess of the Hunt, Wilderness, and Moon",
    tagline_ko="사냥, 야생, 달의 여신",
    description_en="""Artemis is the virgin goddess of the hunt, wilderness, wild animals, and the moon. Twin sister of Apollo, she roams the forests with her band of nymphs, hunting with her silver bow and living free from the constraints of civilization.

Fiercely independent, Artemis swore eternal virginity and punishes any who threaten her or her followers' chastity. She protects young women and children, presides over childbirth, and represents the wild, untamed aspects of nature.

Though a goddess of the hunt, Artemis is also protector of animals and the wilderness itself. She embodies the paradox of the ancient world's relationship with nature—revering and protecting it while also taking sustenance from it.""",
    description_ko="""아르테미스는 사냥, 야생, 야생 동물, 달의 처녀 여신입니다. 아폴론의 쌍둥이 여동생으로, 은색 활로 사냥하며 문명의 제약에서 자유롭게 살며 님프들과 함께 숲을 돌아다닙니다.

맹렬하게 독립적인 아르테미스는 영원한 순결을 맹세했으며 자신이나 추종자들의 정절을 위협하는 자를 벌합니다. 그녀는 젊은 여성과 아이들을 보호하고, 출산을 주관하며, 자연의 야생적이고 길들여지지 않은 측면을 대표합니다.

사냥의 여신이지만, 아르테미스는 동물과 야생 그 자체의 보호자이기도 합니다. 그녀는 고대 세계의 자연과의 관계의 역설을 구현합니다—자연을 숭배하고 보호하면서도 그것으로부터 양분을 취하는.""",
    traits_en=["Independent", "Fierce", "Pure", "Protective", "Wild"],
    traits_ko=["독립적인", "맹렬한", "순수한", "보호하는", "야생의"],
    story_en="When the hunter Actaeon accidentally saw Artemis bathing, she transformed him into a stag. His own hunting dogs, not recognizing their master, tore him apart—a warning about the price of violating the goddess's sacred privacy.",
    story_ko="사냥꾼 악타이온이 우연히 목욕하는 아르테미스를 보았을 때, 그녀는 그를 수사슴으로 변신시켰습니다. 그의 사냥개들은 주인을 알아보지 못하고 그를 갈기갈기 찢었습니다—여신의 신성한 사생활을 침해하는 대가에 대한 경고였습니다.",
    match_message_en="Your features reflect the wild independence of Artemis. There is an untamed quality to your gaze—the look of one who walks their own path and answers to no one. Your face speaks of freedom, fierce protection, and connection to nature.",
    match_message_ko="당신의 이목구비는 아르테미스의 야생적 독립성을 반영합니다. 당신의 눈빛에는 길들여지지 않은 품질이 있습니다—자신만의 길을 걷고 누구에게도 대답하지 않는 사람의 모습. 당신의 얼굴은 자유, 맹렬한 보호, 그리고 자연과의 연결을 말해줍니다.",
    image_prompt="Athletic Greek goddess in hunting tunic, silver bow and quiver, crescent moon crown, surrounded by forest and hunting dogs, deer nearby, moonlit wilderness setting, wild beautiful features, fierce independent expression",
    visual_description="Athletic features, bright alert eyes, natural wild beauty, expression of fierce independence and connection to wilderness",
    aliases=["Diana", "Cynthia", "Phoebe"],
    era="Ancient Greece",
    related_characters=["apollo", "zeus", "leto", "orion", "actaeon"]
)

ARES_DESC = CharacterDescription(
    id="ares",
    name_en="Ares",
    name_ko="아레스",
    tagline_en="God of War, Violence, and Bloodshed",
    tagline_ko="전쟁, 폭력, 유혈의 신",
    description_en="""Ares is the Greek god of war, representing its brutal, violent, and untamed aspects. Unlike Athena who embodies strategic warfare, Ares revels in the chaos, bloodshed, and physical violence of battle. He is the embodiment of the savage brutality that war unleashes.

Despite being one of the twelve Olympians, Ares was not widely loved among the Greeks—they respected him but feared him. Even Zeus called him the most hated of all his children. Yet Ares represents a truth about human nature that cannot be denied.

Ares finds his most famous relationship with Aphrodite, goddess of love. Their affair, exposed by Hephaestus, produced several children including Eros. This union of war and love reflects the ancient understanding that passion drives both creation and destruction.""",
    description_ko="""아레스는 그리스의 전쟁 신으로, 전쟁의 잔인하고, 폭력적이고, 길들여지지 않은 측면을 대표합니다. 전략적 전쟁을 구현하는 아테나와 달리, 아레스는 전투의 혼돈, 유혈, 물리적 폭력을 즐깁니다. 그는 전쟁이 풀어놓는 야만적 잔인함의 구현입니다.

열두 올림포스 신 중 하나임에도 불구하고, 아레스는 그리스인들 사이에서 널리 사랑받지 못했습니다—그들은 그를 존경했지만 두려워했습니다. 심지어 제우스조차 그를 자신의 모든 자녀 중 가장 미워한다고 말했습니다. 그러나 아레스는 부정할 수 없는 인간 본성에 대한 진실을 대표합니다.

아레스는 사랑의 여신 아프로디테와의 관계로 가장 유명합니다. 헤파이스토스에 의해 폭로된 그들의 불륜은 에로스를 포함한 여러 자녀를 낳았습니다. 전쟁과 사랑의 이 결합은 열정이 창조와 파괴 모두를 이끈다는 고대의 이해를 반영합니다.""",
    traits_en=["Fierce", "Violent", "Passionate", "Fearless", "Brutal"],
    traits_ko=["맹렬한", "폭력적인", "열정적인", "두려움 없는", "잔인한"],
    story_en="When Ares and Aphrodite were caught together in Hephaestus's golden net, the smith god summoned all the Olympians to witness their shame. Yet Ares felt no embarrassment—he stood proud even in capture, embodying his nature of unashamed aggression.",
    story_ko="아레스와 아프로디테가 헤파이스토스의 황금 그물에 함께 잡혔을 때, 대장장이 신은 모든 올림포스 신들을 불러 그들의 수치를 목격하게 했습니다. 그러나 아레스는 부끄러움을 느끼지 않았습니다—그는 포획당한 상태에서도 당당히 서서 부끄러움 없는 공격성의 본성을 구현했습니다.",
    match_message_en="Your features carry the fierce intensity of Ares. There is a raw power to your appearance—the look of one who faces conflict without hesitation. Your face speaks of passion, courage, and the warrior spirit that does not back down.",
    match_message_ko="당신의 이목구비는 아레스의 맹렬한 강렬함을 담고 있습니다. 당신의 외모에는 거친 힘이 있습니다—망설임 없이 갈등에 맞서는 사람의 모습. 당신의 얼굴은 열정, 용기, 그리고 물러서지 않는 전사의 정신을 말해줍니다.",
    image_prompt="Muscular Greek god of war in bronze armor and plumed helmet, fierce red eyes, spear and shield, battlefield with fire and chaos behind him, aggressive powerful stance, blood-red cloak, intimidating fearsome presence",
    visual_description="Strong angular features, fierce intense eyes, powerful jaw, expression of barely contained aggression and warrior intensity",
    aliases=["Mars", "Enyalius"],
    era="Ancient Greece",
    related_characters=["athena", "aphrodite", "zeus", "hephaestus", "phobos"]
)

HADES_DESC = CharacterDescription(
    id="hades",
    name_en="Hades",
    name_ko="하데스",
    tagline_en="God of the Underworld and the Dead",
    tagline_ko="지하세계와 죽은 자들의 신",
    description_en="""Hades is the god of the underworld and ruler of the dead, one of the three sons of Cronus who divided the cosmos with his brothers Zeus and Poseidon. Though often feared, Hades is not evil—he is the stern but fair judge of the deceased, ensuring each soul receives its proper fate.

Unlike the other Olympians who dwell on Mount Olympus, Hades rules from his dark realm below, rarely visiting the world above. He possesses the Helm of Darkness, which renders him invisible, and guards the vast wealth of the earth—precious metals and gems buried within.

Though his abduction of Persephone is his most famous myth, Hades proved to be a devoted husband. His realm, while somber, is orderly and just. He represents the inevitable end that awaits all mortals, neither cruel nor kind—simply unavoidable.""",
    description_ko="""하데스는 지하세계의 신이자 죽은 자들의 지배자로, 형제 제우스, 포세이돈과 함께 우주를 나눈 크로노스의 세 아들 중 하나입니다. 종종 두려움의 대상이지만, 하데스는 악하지 않습니다—그는 엄격하지만 공정한 죽은 자들의 심판자로, 각 영혼이 적절한 운명을 받도록 보장합니다.

올림포스 산에 거주하는 다른 올림포스 신들과 달리, 하데스는 아래의 어두운 영역에서 통치하며, 지상 세계를 거의 방문하지 않습니다. 그는 그를 보이지 않게 만드는 어둠의 투구를 소유하고, 땅 속에 묻힌 귀금속과 보석—지구의 광대한 부를 지킵니다.

페르세포네 납치가 그의 가장 유명한 신화이지만, 하데스는 헌신적인 남편임이 증명되었습니다. 그의 영역은 우울하지만 질서 있고 공정합니다. 그는 모든 필멸자를 기다리는 피할 수 없는 끝을 대표합니다—잔인하지도 친절하지도 않은, 단순히 피할 수 없는.""",
    traits_en=["Just", "Stern", "Wealthy", "Patient", "Inevitable"],
    traits_ko=["공정한", "엄격한", "부유한", "인내하는", "피할 수 없는"],
    story_en="When Hades fell in love with Persephone, he abducted her to the underworld. Her mother Demeter's grief caused eternal winter until a compromise was reached: Persephone would spend half the year below, half above—thus creating the seasons.",
    story_ko="하데스가 페르세포네와 사랑에 빠졌을 때, 그는 그녀를 지하세계로 납치했습니다. 그녀의 어머니 데메테르의 슬픔은 영원한 겨울을 일으켰고, 결국 타협에 이르렀습니다: 페르세포네는 일 년의 절반을 아래에서, 절반을 위에서 보낼 것이다—이렇게 계절이 만들어졌습니다.",
    match_message_en="Your features carry the solemn authority of Hades. There is a quiet, inevitable power to your presence—the look of one who understands deep truths others avoid. Your face speaks of patience, fairness, and the dignity of accepting what must be.",
    match_message_ko="당신의 이목구비는 하데스의 엄숙한 권위를 담고 있습니다. 당신의 존재에는 조용하고 피할 수 없는 힘이 있습니다—다른 사람들이 피하는 깊은 진실을 이해하는 사람의 모습. 당신의 얼굴은 인내, 공정함, 그리고 피할 수 없는 것을 받아들이는 존엄을 말해줍니다.",
    image_prompt="Dark majestic Greek god with pale skin and black hair, wearing dark robes and crown of black iron, holding bident, seated on obsidian throne, Cerberus the three-headed dog nearby, underworld palace with river Styx, somber but regal presence",
    visual_description="Pale stern features, deep dark eyes, sharp angular face, expression of somber authority and inevitable judgment",
    aliases=["Pluto", "Aidoneus", "The Rich One", "The Unseen One"],
    era="Ancient Greece",
    related_characters=["zeus", "poseidon", "persephone", "demeter", "cerberus"]
)

HERMES_DESC = CharacterDescription(
    id="hermes",
    name_en="Hermes",
    name_ko="헤르메스",
    tagline_en="Messenger of the Gods, God of Travel and Thieves",
    tagline_ko="신들의 전령, 여행과 도둑의 신",
    description_en="""Hermes is the swift messenger of the gods, the divine trickster, and the patron of travelers, merchants, thieves, and all who live by their wits. With his winged sandals and helmet, he moves freely between the mortal world, Mount Olympus, and even the underworld.

Born mischievous, Hermes stole Apollo's sacred cattle on the day of his birth and invented the lyre from a tortoise shell. Rather than punishing him, the gods recognized his cleverness and made him their messenger—the only one who can travel anywhere without restriction.

Hermes guides the souls of the dead to the underworld and serves as the patron of boundaries and transitions. He represents the liminal spaces between—neither fully here nor there—and embodies the clever adaptability needed to navigate life's crossroads.""",
    description_ko="""헤르메스는 신들의 빠른 전령이자, 신성한 트릭스터이며, 여행자, 상인, 도둑, 그리고 재치로 살아가는 모든 이들의 수호신입니다. 날개 달린 샌들과 투구로 그는 인간 세계, 올림포스 산, 심지어 지하세계 사이를 자유롭게 이동합니다.

태어나자마자 장난기 많았던 헤르메스는 태어난 날 아폴론의 신성한 소를 훔치고 거북이 껍질로 리라를 발명했습니다. 신들은 그를 벌하는 대신 그의 영리함을 인정하고 그를 전령으로 삼았습니다—제한 없이 어디든 여행할 수 있는 유일한 존재.

헤르메스는 죽은 자들의 영혼을 지하세계로 인도하고 경계와 전환의 수호신 역할을 합니다. 그는 여기도 저기도 아닌 경계의 공간을 대표하며, 인생의 교차로를 헤쳐나가는 데 필요한 영리한 적응력을 구현합니다.""",
    traits_en=["Quick", "Clever", "Adaptable", "Eloquent", "Mischievous"],
    traits_ko=["빠른", "영리한", "적응력 있는", "웅변적인", "장난기 있는"],
    story_en="On the day he was born, Hermes crawled from his crib, found Apollo's sacred cattle, and stole them, walking them backwards to confuse the tracks. When confronted, the infant offered Apollo the newly invented lyre, and the sun god was so delighted he forgave the theft entirely.",
    story_ko="태어난 날, 헤르메스는 요람에서 기어 나와 아폴론의 신성한 소를 찾아 훔쳤고, 발자국을 혼란시키기 위해 뒤로 걷게 했습니다. 대면했을 때, 유아는 아폴론에게 새로 발명한 리라를 제안했고, 태양신은 너무 기뻐서 도둑질을 완전히 용서했습니다.",
    match_message_en="Your features carry the quick intelligence of Hermes. There is a lively, adaptable quality to your appearance—the look of one who thinks fast and can talk their way through any situation. Your face speaks of wit, charm, and the ability to bridge any gap.",
    match_message_ko="당신의 이목구비는 헤르메스의 빠른 지성을 담고 있습니다. 당신의 외모에는 활기차고 적응력 있는 품질이 있습니다—빠르게 생각하고 어떤 상황이든 말로 헤쳐나갈 수 있는 사람의 모습. 당신의 얼굴은 재치, 매력, 그리고 어떤 간극이든 연결하는 능력을 말해줍니다.",
    image_prompt="Youthful Greek god with winged sandals and petasos hat, holding caduceus staff with intertwined serpents, athletic build, mischievous smile, standing at a crossroads, dawn light, quick agile appearance ready for flight",
    visual_description="Youthful mobile features, bright quick eyes, expressive face, mischievous smile, appearance suggesting speed and cleverness",
    aliases=["Mercury", "Psychopompos", "Argeiphontes"],
    era="Ancient Greece",
    related_characters=["zeus", "apollo", "maia", "pan", "perseus"]
)

DIONYSUS_DESC = CharacterDescription(
    id="dionysus",
    name_en="Dionysus",
    name_ko="디오니소스",
    tagline_en="God of Wine, Ecstasy, and Theater",
    tagline_ko="포도주, 황홀경, 연극의 신",
    description_en="""Dionysus is the god of wine, festivity, ecstasy, and theater—the youngest of the Olympians and the only one with a mortal mother. He represents the liberating power of wine and the transformative experience of stepping outside one's ordinary self.

Twice-born, Dionysus was rescued from his dying mother Semele by Zeus, who sewed the infant into his own thigh until he was ready to be born again. This dual birth marks him as a god of death and rebirth, transformation and renewal.

Dionysus's worship involved ecstatic rituals where participants transcended their normal identities through wine, dance, and music. He embodies the parts of human nature that civilization tries to suppress—the wild, the instinctive, the ecstatic. He is both liberator and destroyer.""",
    description_ko="""디오니소스는 포도주, 축제, 황홀경, 연극의 신으로—올림포스 신들 중 가장 어리고 인간 어머니를 둔 유일한 신입니다. 그는 포도주의 해방적 힘과 평범한 자아 밖으로 나가는 변형적 경험을 대표합니다.

두 번 태어난 디오니소스는 죽어가는 어머니 세멜레로부터 제우스에 의해 구출되었고, 제우스는 유아를 다시 태어날 준비가 될 때까지 자신의 허벅지에 꿰매 놓았습니다. 이 이중적 탄생은 그를 죽음과 재탄생, 변형과 갱신의 신으로 표시합니다.

디오니소스 숭배는 참가자들이 포도주, 춤, 음악을 통해 평범한 정체성을 초월하는 황홀한 의식을 수반했습니다. 그는 문명이 억압하려는 인간 본성의 부분들을 구현합니다—야생적인, 본능적인, 황홀한. 그는 해방자이자 파괴자입니다.""",
    traits_en=["Ecstatic", "Liberating", "Wild", "Transformative", "Dual-natured"],
    traits_ko=["황홀한", "해방하는", "야생의", "변형적인", "이중적인"],
    story_en="When King Pentheus of Thebes refused to honor Dionysus and tried to imprison him, the god drove the women of Thebes into a frenzy. Pentheus's own mother, in her madness, tore her son apart with her bare hands, mistaking him for a lion.",
    story_ko="테베의 왕 펜테우스가 디오니소스를 공경하지 않고 가두려 했을 때, 신은 테베의 여성들을 광란에 빠뜨렸습니다. 펜테우스의 어머니는 광기 속에서 아들을 사자로 착각하고 맨손으로 갈기갈기 찢었습니다.",
    match_message_en="Your features carry the intoxicating presence of Dionysus. There is an otherworldly quality to your appearance—the look of one who has touched states beyond the ordinary. Your face speaks of liberation, transformation, and the wild joy that exists beyond civilization's boundaries.",
    match_message_ko="당신의 이목구비는 디오니소스의 취하게 하는 존재감을 담고 있습니다. 당신의 외모에는 이세계적인 품질이 있습니다—평범함을 넘어선 상태에 닿은 사람의 모습. 당신의 얼굴은 해방, 변형, 그리고 문명의 경계를 넘어 존재하는 야생의 기쁨을 말해줍니다.",
    image_prompt="Beautiful androgynous Greek god with ivy crown and flowing hair, holding thyrsus staff and wine cup, surrounded by grapevines and panthers, followers dancing in ecstasy behind him, both masculine and feminine beauty, wild joyous expression",
    visual_description="Beautiful androgynous features, dreamy ecstatic eyes, sensual full lips, expression of wild joy and transcendence",
    aliases=["Bacchus", "Bromios", "Twice-Born"],
    era="Ancient Greece",
    related_characters=["zeus", "semele", "ariadne", "apollo", "hera"]
)

PERSEPHONE_DESC = CharacterDescription(
    id="persephone",
    name_en="Persephone",
    name_ko="페르세포네",
    tagline_en="Queen of the Underworld, Goddess of Spring",
    tagline_ko="지하세계의 여왕, 봄의 여신",
    description_en="""Persephone is the dual goddess who reigns as queen of the underworld alongside Hades while also embodying the return of spring and the cycle of growth. Her yearly journey between the dark realm below and the bright world above creates the seasons themselves.

Daughter of Demeter and Zeus, Persephone was gathering flowers when Hades abducted her to be his queen. Her mother's grief caused all growth to cease until Zeus intervened. Because Persephone ate pomegranate seeds in the underworld, she must return there for part of each year.

This myth reflects the ancient understanding of death and rebirth, the necessity of descent before ascent. Persephone embodies transformation—the maiden becomes the queen, the innocent becomes the powerful, and the cycle of life, death, and renewal continues eternally.""",
    description_ko="""페르세포네는 하데스와 함께 지하세계의 여왕으로 군림하면서도 봄의 귀환과 성장의 순환을 구현하는 이중적 여신입니다. 아래의 어두운 영역과 위의 밝은 세계 사이의 연례 여행이 계절 자체를 만듭니다.

데메테르와 제우스의 딸인 페르세포네는 꽃을 모으다가 하데스에 의해 납치되어 그의 여왕이 되었습니다. 그녀의 어머니의 슬픔은 제우스가 개입할 때까지 모든 성장을 멈추게 했습니다. 페르세포네가 지하세계에서 석류 씨앗을 먹었기 때문에, 그녀는 매년 일부 기간 그곳으로 돌아가야 합니다.

이 신화는 죽음과 재탄생, 상승 전의 하강의 필요성에 대한 고대의 이해를 반영합니다. 페르세포네는 변형을 구현합니다—처녀가 여왕이 되고, 순수한 자가 강력해지며, 삶, 죽음, 갱신의 순환이 영원히 계속됩니다.""",
    traits_en=["Dual-natured", "Transformative", "Powerful", "Graceful", "Cyclic"],
    traits_ko=["이중적인", "변형적인", "강력한", "우아한", "순환적인"],
    story_en="When Persephone first arrived in the underworld, she was a frightened maiden. But over time, she grew into her role as queen, becoming so powerful that even the dead feared her anger. She who was once a victim became the dread queen whose word was law.",
    story_ko="페르세포네가 처음 지하세계에 도착했을 때, 그녀는 겁먹은 처녀였습니다. 그러나 시간이 지나면서 여왕으로서의 역할로 성장하여, 죽은 자들조차 그녀의 분노를 두려워할 정도로 강력해졌습니다. 한때 희생자였던 그녀는 말이 법인 두려운 여왕이 되었습니다.",
    match_message_en="Your features reflect the dual nature of Persephone. There is both light and shadow in your appearance—the freshness of spring and the depth of darker knowledge. Your face speaks of transformation, of one who has descended and returned stronger.",
    match_message_ko="당신의 이목구비는 페르세포네의 이중적 본성을 반영합니다. 당신의 외모에는 빛과 그림자가 모두 있습니다—봄의 신선함과 더 어두운 지식의 깊이. 당신의 얼굴은 변형을, 내려갔다가 더 강해져 돌아온 사람을 말해줍니다.",
    image_prompt="Beautiful Greek goddess with two aspects—one half showing spring flowers and bright colors, the other showing dark underworld queen with crown, holding pomegranate, surrounded by both flowers and shadows, ethereal transformative beauty",
    visual_description="Delicate beautiful features with depth, eyes that hold both innocence and ancient wisdom, expression suggesting hidden power beneath gentle surface",
    aliases=["Proserpina", "Kore", "The Maiden", "Dread Persephone"],
    era="Ancient Greece",
    related_characters=["hades", "demeter", "zeus", "hecate", "dionysus"]
)


# ============================================
# NORSE MYTHOLOGY DESCRIPTIONS
# ============================================

ODIN_DESC = CharacterDescription(
    id="odin",
    name_en="Odin",
    name_ko="오딘",
    tagline_en="Allfather, God of Wisdom, War, and Death",
    tagline_ko="만물의 아버지, 지혜, 전쟁, 죽음의 신",
    description_en="""Odin is the supreme deity of Norse mythology, known as the Allfather and ruler of Asgard. He is a complex god who embodies wisdom, war, poetry, and death, constantly seeking knowledge at any cost.

Unlike gods who gained power through birthright alone, Odin sacrificed himself on the World Tree Yggdrasil for nine days to gain the wisdom of the runes. He also traded one of his eyes for a drink from Mímir's well of knowledge, forever marking his face with the price of wisdom.

Accompanied by his ravens Huginn (Thought) and Muninn (Memory), and his wolves Geri and Freki, Odin watches over the nine realms. He gathers fallen warriors to his hall Valhalla, preparing for the final battle of Ragnarök.""",
    description_ko="""오딘은 북유럽 신화의 최고신으로, 만물의 아버지이자 아스가르드의 지배자로 알려져 있습니다. 그는 지혜, 전쟁, 시, 죽음을 구현하는 복잡한 신으로, 어떤 대가를 치르더라도 끊임없이 지식을 추구합니다.

단순히 태생적 권리로 힘을 얻은 신들과 달리, 오딘은 룬의 지혜를 얻기 위해 세계수 이그드라실에서 9일 동안 자신을 희생했습니다. 또한 미미르의 지식의 샘에서 한 모금 마시기 위해 한쪽 눈을 바쳤으며, 이로써 그의 얼굴에는 영원히 지혜의 대가가 새겨졌습니다.

생각의 까마귀 후긴과 기억의 까마귀 무닌, 그리고 늑대 게리와 프레키와 함께, 오딘은 아홉 세계를 지켜봅니다. 그는 전사한 전사들을 발할라 전당에 모아 최후의 전투 라그나로크를 준비합니다.""",
    traits_en=["Wise", "Sacrificial", "Mysterious", "All-seeing", "Relentless"],
    traits_ko=["지혜로운", "희생적인", "신비로운", "모든 것을 보는", "끈질긴"],
    story_en="To gain the wisdom of the runes, Odin hung himself from Yggdrasil for nine days and nights, pierced by his own spear, without food or water. On the ninth night, screaming, he grasped the runes and their secrets were revealed to him.",
    story_ko="룬의 지혜를 얻기 위해, 오딘은 자신의 창에 꿰뚫린 채 음식도 물도 없이 9일 밤낮을 이그드라실에 매달렸습니다. 아홉 번째 밤, 비명을 지르며 그는 룬을 움켜쥐었고 그 비밀이 그에게 드러났습니다.",
    match_message_en="Your features bear the mark of Odin's seeking wisdom. There is a depth to your gaze that speaks of one who has seen much and understood more. Like the Allfather, your face tells of sacrifices made for greater knowledge.",
    match_message_ko="당신의 이목구비는 오딘의 지혜 추구의 표식을 지니고 있습니다. 당신의 눈빛에는 많이 보고 더 많이 이해한 사람을 말해주는 깊이가 있습니다. 만물의 아버지처럼, 당신의 얼굴은 더 큰 지식을 위해 치른 희생을 말해줍니다.",
    image_prompt="Ancient wise Norse god with long grey beard, one eye covered or missing, wearing dark cloak and wide-brimmed hat, holding the spear Gungnir, two ravens perched on shoulders, two wolves at feet, runes glowing around him, mystical Norse forest background, weathered powerful face",
    visual_description="Long weathered face, one deep penetrating eye, prominent brow, long grey beard, intense knowing gaze, ancient wisdom in features",
    aliases=["Wotan", "Woden", "Allfather", "One-Eye"],
    era="Viking Age",
    related_characters=["thor", "loki", "frigg", "baldur", "freya"]
)

THOR_DESC = CharacterDescription(
    id="thor",
    name_en="Thor",
    name_ko="토르",
    tagline_en="God of Thunder, Protector of Mankind",
    tagline_ko="천둥의 신, 인류의 수호자",
    description_en="""Thor is the mighty god of thunder, son of Odin and the earth goddess Jörð. He is the strongest of all the Norse gods, wielding the legendary hammer Mjölnir, which can level mountains and returns to his hand after being thrown.

Unlike his father's subtle wisdom, Thor embodies straightforward strength and unwavering courage. He is the protector of Asgard and Midgard (Earth), constantly battling giants and monsters that threaten the realms. His red beard crackles with lightning when he rides his chariot across the storm clouds.

Despite his fearsome power, Thor is beloved by common people for his honest nature and his role as their defender. He is quick to anger but equally quick to forgive, and his hearty appetite for food and drink is legendary.""",
    description_ko="""토르는 강력한 천둥의 신으로, 오딘과 대지의 여신 요르드의 아들입니다. 그는 모든 북유럽 신들 중 가장 강하며, 산을 평평하게 만들고 던진 후 손으로 돌아오는 전설적인 망치 묠니르를 휘두릅니다.

아버지의 미묘한 지혜와 달리, 토르는 직접적인 힘과 흔들림 없는 용기를 구현합니다. 그는 아스가르드와 미드가르드(지구)의 수호자로, 세계를 위협하는 거인과 괴물들과 끊임없이 싸웁니다. 그가 폭풍 구름을 가로질러 전차를 탈 때 그의 붉은 수염은 번개로 튀깁니다.

무시무시한 힘에도 불구하고, 토르는 정직한 성격과 인류의 수호자 역할로 일반 사람들에게 사랑받습니다. 그는 쉽게 화를 내지만 똑같이 쉽게 용서하며, 음식과 음료에 대한 왕성한 식욕은 전설적입니다.""",
    traits_en=["Strong", "Brave", "Honest", "Protective", "Fierce"],
    traits_ko=["강한", "용감한", "정직한", "보호하는", "맹렬한"],
    story_en="When the giant Thrym stole Mjölnir and demanded Freya as ransom, Thor disguised himself as a bride. At the wedding feast, he ate an entire ox, eight salmon, and drank three barrels of mead before revealing himself and slaying all the giants with his recovered hammer.",
    story_ko="거인 트림이 묠니르를 훔치고 프레이야를 몸값으로 요구했을 때, 토르는 신부로 변장했습니다. 결혼 피로연에서 그는 황소 한 마리, 연어 여덟 마리를 먹고 미드 세 통을 마신 후 정체를 드러내고 되찾은 망치로 모든 거인을 죽였습니다.",
    match_message_en="Your features carry the robust strength of Thor. There is an honest, straightforward quality to your appearance—open and unguarded. Like the Thunderer, your strong features speak of one who faces challenges head-on with unwavering courage.",
    match_message_ko="당신의 이목구비는 토르의 건장한 힘을 담고 있습니다. 당신의 외모에는 정직하고 직접적인 품질이 있습니다—열려 있고 경계하지 않는. 천둥신처럼, 당신의 강한 이목구비는 흔들림 없는 용기로 도전에 정면으로 맞서는 사람을 말해줍니다.",
    image_prompt="Powerful muscular Norse god with wild red hair and beard, blue eyes like lightning, wearing Viking armor with cape, holding the hammer Mjölnir crackling with electricity, storm clouds and lightning behind him, riding a chariot pulled by goats, fierce determined expression",
    visual_description="Square powerful jaw, wide bright eyes, strong prominent features, red complexion, broad open face, fierce but honest expression",
    aliases=["Donar", "Þórr", "Thunderer"],
    era="Viking Age",
    related_characters=["odin", "loki", "sif", "mjolnir", "jormungandr"]
)

FREYA_DESC = CharacterDescription(
    id="freya",
    name_en="Freya",
    name_ko="프레이야",
    tagline_en="Goddess of Love, Beauty, and War",
    tagline_ko="사랑, 아름다움, 전쟁의 여신",
    description_en="""Freya is the most renowned of the Norse goddesses, embodying love, beauty, fertility, and also war and death. She rules over the heavenly field of Fólkvangr, where she receives half of all warriors slain in battle—the other half going to Odin's Valhalla.

The most beautiful of all goddesses, Freya possesses the legendary necklace Brísingamen and a cloak of falcon feathers that allows her to transform and fly. She rides a chariot pulled by two cats and is accompanied by a boar named Hildisvíni.

As the goddess of seiðr (magic), Freya taught Odin himself the mystical arts. She weeps tears of red gold for her lost husband Óðr, searching for him across the nine realms.""",
    description_ko="""프레이야는 북유럽 여신들 중 가장 유명하며, 사랑, 아름다움, 풍요, 그리고 전쟁과 죽음을 구현합니다. 그녀는 천상의 들판 폴크방르를 지배하며, 전투에서 전사한 모든 전사의 절반을 받습니다—나머지 절반은 오딘의 발할라로 갑니다.

모든 여신 중 가장 아름다운 프레이야는 전설적인 목걸이 브리싱가멘과 변신하여 날 수 있게 해주는 매 깃털 망토를 소유합니다. 그녀는 두 마리 고양이가 끄는 전차를 타고 힐디스비니라는 멧돼지와 동행합니다.

세이드(마법)의 여신으로서, 프레이야는 오딘 자신에게 신비로운 기술을 가르쳤습니다. 그녀는 잃어버린 남편 오드르를 위해 붉은 금의 눈물을 흘리며, 아홉 세계를 가로질러 그를 찾습니다.""",
    traits_en=["Beautiful", "Magical", "Fierce", "Passionate", "Independent"],
    traits_ko=["아름다운", "마법적인", "맹렬한", "열정적인", "독립적인"],
    story_en="To obtain the beautiful necklace Brísingamen, Freya spent a night with each of the four dwarven craftsmen who forged it. When Loki told Odin of this, Odin made her start a war between two kings as punishment—for Freya loved battle as much as beauty.",
    story_ko="아름다운 목걸이 브리싱가멘을 얻기 위해, 프레이야는 그것을 만든 네 명의 드워프 장인 각각과 하룻밤을 보냈습니다. 로키가 이것을 오딘에게 말했을 때, 오딘은 벌로 그녀에게 두 왕 사이에 전쟁을 일으키게 했습니다—프레이야는 아름다움만큼이나 전투를 사랑했기 때문입니다.",
    match_message_en="Your features reflect Freya's captivating blend of beauty and strength. There is both softness and fire in your appearance—the grace of love and the intensity of one who knows her own power. Your face speaks of passion and independence.",
    match_message_ko="당신의 이목구비는 프레이야의 매혹적인 아름다움과 강함의 조화를 반영합니다. 당신의 외모에는 부드러움과 불 같은 면이 모두 있습니다—사랑의 우아함과 자신의 힘을 아는 사람의 강렬함. 당신의 얼굴은 열정과 독립성을 말해줍니다.",
    image_prompt="Stunningly beautiful Norse goddess with flowing golden hair, wearing the glowing necklace Brísingamen, falcon feather cloak, riding a chariot pulled by two large cats, boar companion nearby, amber and gold colors, magical aura, Nordic forest and aurora background, fierce yet beautiful expression",
    visual_description="Oval face with delicate yet strong features, bright luminous eyes, golden hair, perfect symmetry, expression of both warmth and fierce determination",
    aliases=["Freyja", "Vanadís", "Lady of the Vanir"],
    era="Viking Age",
    related_characters=["odin", "thor", "loki", "freyr", "frigg"]
)

LOKI_DESC = CharacterDescription(
    id="loki",
    name_en="Loki",
    name_ko="로키",
    tagline_en="God of Mischief, Trickery, and Chaos",
    tagline_ko="장난, 속임수, 혼돈의 신",
    description_en="""Loki is the most unpredictable figure in Norse mythology—a shape-shifting trickster who is both friend and foe to the gods. Neither fully Aesir nor giant, he walks between worlds, bound by his own inscrutable motives.

His cunning mind has both helped and hindered the gods countless times. He retrieved Thor's hammer, created magical gifts for the gods, but also caused Baldur's death and fathered monsters including Fenrir the wolf, Jörmungandr the world serpent, and Hel, ruler of the dead.

Loki embodies the chaos necessary for change and growth, but also the destruction that comes from unchecked mischief. At Ragnarök, he will lead the forces of chaos against the gods, yet without him, many of the gods' greatest treasures would never exist.""",
    description_ko="""로키는 북유럽 신화에서 가장 예측할 수 없는 인물입니다—신들의 친구이자 적인 변신하는 트릭스터입니다. 아스가르드 신도 거인도 아닌 그는 세계 사이를 걸으며, 자신만의 불가해한 동기에 묶여 있습니다.

그의 교활한 두뇌는 신들을 수없이 돕기도 하고 방해하기도 했습니다. 그는 토르의 망치를 되찾고, 신들을 위한 마법 선물을 만들었지만, 발드르의 죽음을 일으키고 늑대 펜리르, 세계뱀 요르문간드, 죽은 자의 지배자 헬 등 괴물들의 아버지이기도 합니다.

로키는 변화와 성장에 필요한 혼돈을 구현하지만, 통제되지 않은 장난에서 오는 파괴도 구현합니다. 라그나로크에서 그는 신들에 맞서 혼돈의 세력을 이끌 것이지만, 그가 없었다면 신들의 가장 위대한 보물들 중 많은 것이 존재하지 않았을 것입니다.""",
    traits_en=["Cunning", "Unpredictable", "Chaotic", "Clever", "Ambiguous"],
    traits_ko=["교활한", "예측불가한", "혼란스러운", "영리한", "모호한"],
    story_en="When the gods needed a wall built around Asgard, Loki suggested hiring a giant who demanded the sun, moon, and Freya as payment. To prevent this, Loki transformed into a mare to distract the giant's stallion—and later gave birth to Sleipnir, Odin's eight-legged horse.",
    story_ko="신들이 아스가르드 주위에 성벽을 세워야 했을 때, 로키는 태양, 달, 프레이야를 대가로 요구하는 거인을 고용할 것을 제안했습니다. 이를 막기 위해, 로키는 거인의 종마를 유혹하려고 암말로 변신했고—나중에 오딘의 여덟 다리 말 슬레이프니르를 낳았습니다.",
    match_message_en="Your features carry Loki's mercurial charm. There is a quicksilver quality to your appearance—sharp, clever, and impossible to pin down. Your face speaks of one who sees possibilities others miss and walks their own unpredictable path.",
    match_message_ko="당신의 이목구비는 로키의 변덕스러운 매력을 담고 있습니다. 당신의 외모에는 수은 같은 품질이 있습니다—날카롭고, 영리하고, 규정지을 수 없는. 당신의 얼굴은 다른 사람들이 놓치는 가능성을 보고 자신만의 예측불가한 길을 걷는 사람을 말해줍니다.",
    image_prompt="Handsome but mischievous Norse god with sharp angular features, red or black hair, green cunning eyes, wearing green and gold, surrounded by flames and illusions, multiple overlapping images suggesting shapeshifting, sly smirk, chaotic magical energy, ambiguous neither good nor evil appearance",
    visual_description="Sharp angular features, asymmetrical face, bright clever eyes, quick expressions, thin face with pointed chin, mercurial shifting appearance",
    aliases=["Loptr", "Hveðrungr", "Sky-Treader"],
    era="Viking Age",
    related_characters=["odin", "thor", "sigyn", "fenrir", "hel", "baldur"]
)


# ============================================
# KOREAN MYTHOLOGY & HISTORICAL FIGURES
# ============================================

ADMIRAL_YI_DESC = CharacterDescription(
    id="admiral_yi",
    name_en="Admiral Yi Sun-sin",
    name_ko="이순신 장군",
    tagline_en="Legendary Naval Commander, Inventor of the Turtle Ship",
    tagline_ko="전설적인 해군 사령관, 거북선의 발명가",
    description_en="""Admiral Yi Sun-sin is Korea's greatest military hero, an undefeated naval commander who saved his nation during the Japanese invasions of 1592-1598. Against overwhelming odds and despite facing political persecution, he never lost a single battle in his 23 naval engagements.

His tactical genius was matched only by his moral integrity. Even when stripped of his rank and tortured due to political machinations, he returned to service when called, commanding just 13 ships against 333 Japanese vessels—and won decisively at the Battle of Myeongnyang.

Yi's innovations in naval warfare, including the legendary turtle ship (geobukseon), changed the course of history. He died in battle at Noryang, his last words reportedly being "The battle is at its height. Beat my war drums. Do not announce my death." """,
    description_ko="""이순신 장군은 한국의 가장 위대한 군사 영웅으로, 1592-1598년 일본의 침략 동안 조국을 구한 불패의 해군 사령관입니다. 압도적인 역경과 정치적 박해에도 불구하고, 그는 23번의 해전에서 단 한 번도 패하지 않았습니다.

그의 전술적 천재성은 도덕적 청렴함에 필적했습니다. 정치적 음모로 직위를 박탈당하고 고문당했을 때조차, 부름을 받으면 복무에 복귀하여 단 13척의 배로 333척의 일본 함대에 맞서 명량해전에서 결정적인 승리를 거두었습니다.

거북선을 포함한 해전에서의 혁신은 역사의 흐름을 바꾸었습니다. 그는 노량해전에서 전사했으며, 마지막 말은 "전투가 급하니, 나의 죽음을 알리지 말라"였다고 전해집니다.""",
    traits_en=["Strategic", "Loyal", "Innovative", "Righteous", "Undefeated"],
    traits_ko=["전략적인", "충성스러운", "혁신적인", "의로운", "불패의"],
    story_en="At Myeongnyang, Admiral Yi faced impossible odds—13 ships against 333. Using the treacherous currents of the strait, he funneled the Japanese fleet into a narrow channel where their numbers became a disadvantage. He sank 31 ships without losing any of his own.",
    story_ko="명량에서 이순신 장군은 불가능한 역경에 직면했습니다—13척 대 333척. 해협의 위험한 해류를 이용하여, 그는 일본 함대를 좁은 수로로 유인하여 그들의 수적 우위가 오히려 불리하게 만들었습니다. 그는 자신의 배를 단 한 척도 잃지 않고 31척을 격침시켰습니다.",
    match_message_en="Your features reflect the unwavering resolve of Admiral Yi. There is strength and dignity in your face—the look of one who would never abandon their duty or their honor, regardless of personal cost. Your gaze speaks of strategic depth and iron determination.",
    match_message_ko="당신의 이목구비는 이순신 장군의 흔들림 없는 결의를 반영합니다. 당신의 얼굴에는 강함과 존엄이 있습니다—개인적 대가와 관계없이 의무나 명예를 절대 저버리지 않을 사람의 모습. 당신의 눈빛은 전략적 깊이와 철의 결단력을 말해줍니다.",
    image_prompt="Korean admiral in traditional Joseon military armor and helmet, strong dignified face, commanding gaze, standing on turtle ship deck, Korean naval battle in background, dramatic sea and sky, war drums, detailed historical Korean aesthetic, heroic pose",
    visual_description="Square strong jaw, deep determined eyes, stern dignified expression, mature features showing resolve and wisdom, commanding presence",
    aliases=["충무공", "Chungmugong", "Yi Sun-sin"],
    era="Joseon Dynasty (1545-1598)",
    related_characters=["sejong_the_great", "gwanggaeto", "jumong"]
)

SEJONG_DESC = CharacterDescription(
    id="sejong_the_great",
    name_en="King Sejong the Great",
    name_ko="세종대왕",
    tagline_en="Creator of Hangul, Patron of Science and Culture",
    tagline_ko="한글의 창제자, 과학과 문화의 후원자",
    description_en="""King Sejong the Great is revered as the wisest and most beloved monarch in Korean history. During his 32-year reign (1418-1450), he oversaw a golden age of scientific, cultural, and artistic achievement that transformed Korean civilization.

His greatest legacy is the creation of Hangul, the Korean alphabet, in 1443. Designed to be easy for common people to learn, it replaced the complex Chinese characters that kept literacy out of reach for most Koreans. Sejong famously declared: "A wise man can acquaint himself with them before the morning is over; a stupid man can learn them in the space of ten days."

Beyond Hangul, Sejong sponsored innovations in astronomy, agriculture, medicine, and music. He established the Hall of Worthies to nurture scholars and created instruments like the rain gauge and sundial that advanced Korean science centuries ahead of Europe.""",
    description_ko="""세종대왕은 한국 역사상 가장 현명하고 사랑받는 군주로 추앙받습니다. 32년간의 재위 기간(1418-1450) 동안, 그는 한국 문명을 변화시킨 과학, 문화, 예술의 황금기를 이끌었습니다.

그의 가장 위대한 유산은 1443년 한글의 창제입니다. 일반 백성들이 쉽게 배울 수 있도록 설계된 한글은 대부분의 한국인들에게 문해력을 멀게 했던 복잡한 한자를 대체했습니다. 세종은 "지혜로운 자는 아침이 지나기 전에 익히고, 어리석은 자도 열흘이면 배울 수 있다"고 선언했습니다.

한글 외에도, 세종은 천문학, 농업, 의학, 음악의 혁신을 후원했습니다. 그는 학자들을 육성하기 위해 집현전을 설립하고 측우기와 해시계 같은 기구를 만들어 한국 과학을 유럽보다 수 세기 앞서게 했습니다.""",
    traits_en=["Wise", "Benevolent", "Innovative", "Scholarly", "Compassionate"],
    traits_ko=["지혜로운", "인자한", "혁신적인", "학문적인", "자비로운"],
    story_en="Sejong worked on Hangul in secret for years, fearing resistance from Confucian scholars who valued Chinese characters. When finally revealed, some officials protested that teaching commoners to read was dangerous. Sejong persisted, declaring literacy a right, not a privilege.",
    story_ko="세종은 한자를 중시하는 유학자들의 반발을 우려하여 수년간 비밀리에 한글 작업을 했습니다. 마침내 공개되었을 때, 일부 관리들은 평민에게 글을 가르치는 것이 위험하다고 항의했습니다. 세종은 문해력은 특권이 아닌 권리라고 선언하며 뜻을 굽히지 않았습니다.",
    match_message_en="Your features reflect King Sejong's wise benevolence. There is a thoughtful, scholarly quality to your face—the look of one who seeks to understand and to help others understand. Your gentle yet determined expression speaks of leadership through wisdom rather than force.",
    match_message_ko="당신의 이목구비는 세종대왕의 지혜로운 인자함을 반영합니다. 당신의 얼굴에는 사려 깊고 학문적인 품질이 있습니다—이해하고 다른 사람들이 이해하도록 돕고자 하는 사람의 모습. 당신의 온화하지만 결연한 표정은 강압이 아닌 지혜를 통한 리더십을 말해줍니다.",
    image_prompt="Wise Korean king in royal Joseon dragon robes and crown, gentle scholarly face with kind eyes, holding a scroll with Hangul characters, surrounded by books and scientific instruments, palace library background, soft warm lighting, benevolent regal expression",
    visual_description="Rounded gentle face, soft wise eyes, scholarly appearance, benevolent expression, dignified but approachable features",
    aliases=["세종", "Sejong", "The Great King"],
    era="Joseon Dynasty (1397-1450)",
    related_characters=["admiral_yi", "gwanggaeto", "seon_deok"]
)

GUMIHO_DESC = CharacterDescription(
    id="gumiho",
    name_en="Gumiho (Nine-Tailed Fox)",
    name_ko="구미호",
    tagline_en="Mystical Nine-Tailed Fox Spirit",
    tagline_ko="신비로운 아홉 꼬리 여우 정령",
    description_en="""The Gumiho is a legendary creature from Korean folklore—a fox that has lived for a thousand years and gained the ability to transform into a beautiful woman. With each century of life, it grows an additional tail, until it possesses nine tails of immense magical power.

In traditional tales, the Gumiho often seeks to become fully human, which requires consuming human hearts or livers. However, some stories tell of Gumiho who use their powers for good, or who fall genuinely in love and struggle against their nature.

The Gumiho embodies the duality of attraction and danger, beauty and destruction. It represents the seductive power of the unknown and the possibility of transformation—for better or worse.""",
    description_ko="""구미호는 한국 민속의 전설적인 존재로—천 년을 산 여우가 아름다운 여인으로 변신하는 능력을 얻은 것입니다. 한 세기를 살 때마다 꼬리가 하나씩 자라, 아홉 개의 꼬리에 막대한 마법의 힘을 갖게 됩니다.

전통적인 이야기에서, 구미호는 종종 완전한 인간이 되고자 하며, 이를 위해 인간의 심장이나 간을 먹어야 합니다. 그러나 일부 이야기에서는 자신의 능력을 선하게 사용하거나, 진심으로 사랑에 빠져 본성과 싸우는 구미호를 다룹니다.

구미호는 매력과 위험, 아름다움과 파괴의 이중성을 구현합니다. 미지의 유혹적인 힘과 변신의 가능성—좋든 나쁘든—을 대표합니다.""",
    traits_en=["Seductive", "Mysterious", "Powerful", "Transformative", "Dual-natured"],
    traits_ko=["유혹적인", "신비로운", "강력한", "변신하는", "이중적인"],
    story_en="A young scholar fell in love with a beautiful woman, not knowing she was a Gumiho. When he discovered her true nature, she expected him to flee in terror. Instead, he declared his love unchanged. Moved by his devotion, she gave up her immortality to become human and lived with him until old age.",
    story_ko="젊은 선비가 아름다운 여인과 사랑에 빠졌는데, 그녀가 구미호인 줄 몰랐습니다. 그가 그녀의 정체를 알았을 때, 그녀는 그가 공포에 질려 도망갈 것이라 예상했습니다. 대신, 그는 사랑이 변함없다고 선언했습니다. 그의 헌신에 감동받아, 그녀는 불멸을 포기하고 인간이 되어 그와 노년까지 함께 살았습니다.",
    match_message_en="Your features carry the enchanting allure of the Gumiho. There is a captivating mystery to your appearance—beautiful yet somehow otherworldly. Your face speaks of hidden depths, transformation, and the mesmerizing power that exists between worlds.",
    match_message_ko="당신의 이목구비는 구미호의 매혹적인 매력을 담고 있습니다. 당신의 외모에는 매혹적인 신비로움이 있습니다—아름답지만 어딘가 이세계적인. 당신의 얼굴은 숨겨진 깊이, 변신, 그리고 세계 사이에 존재하는 매혹적인 힘을 말해줍니다.",
    image_prompt="Beautiful Korean woman with fox-like features, sharp alluring eyes, long flowing black hair with hints of red, wearing traditional hanbok with fox motifs, nine ethereal fox tails behind her, moonlit Korean forest background, mysterious seductive expression, magical aura",
    visual_description="Heart-shaped face, sharp captivating eyes, elegant pointed features, alluring expression, beauty with an edge of danger, fox-like grace",
    aliases=["구미호", "Nine-tailed Fox", "Yeowu"],
    era="Korean Folklore",
    related_characters=["dokkaebi", "samsin", "kitsune"]
)


# ============================================
# CHINESE FIGURES
# ============================================

CONFUCIUS_DESC = CharacterDescription(
    id="confucius",
    name_en="Confucius",
    name_ko="공자",
    tagline_en="The Great Sage, Father of Chinese Philosophy",
    tagline_ko="위대한 성인, 중국 철학의 아버지",
    description_en="""Confucius (551-479 BCE) is China's most influential philosopher, whose teachings on ethics, family, and governance have shaped East Asian civilization for over 2,500 years. Born during the turbulent Spring and Autumn period, he dedicated his life to restoring social harmony through moral cultivation.

His philosophy centers on ren (benevolence), li (ritual propriety), and the cultivation of virtue through education and self-improvement. He believed that social order flows from personal virtue—when rulers are moral, the people will naturally follow.

Though he held only minor official positions in his lifetime, Confucius's teachings, compiled by his disciples in the Analerta, became the foundation of Chinese imperial education and continue to influence billions of people today.""",
    description_ko="""공자(기원전 551-479년)는 중국의 가장 영향력 있는 철학자로, 윤리, 가족, 통치에 관한 가르침은 2,500년 이상 동아시아 문명을 형성해왔습니다. 혼란스러운 춘추시대에 태어나, 그는 도덕적 수양을 통해 사회적 조화를 회복하는 데 일생을 바쳤습니다.

그의 철학은 인(仁, 인자함), 예(禮, 예법), 그리고 교육과 자기 수양을 통한 덕의 함양을 중심으로 합니다. 그는 사회 질서가 개인의 덕에서 흘러나온다고 믿었습니다—통치자가 도덕적이면, 백성들은 자연히 따를 것입니다.

생전에는 미미한 관직만 맡았지만, 그의 제자들이 편찬한 논어에 담긴 공자의 가르침은 중국 제국 교육의 기반이 되었고, 오늘날까지 수십억 명에게 영향을 미치고 있습니다.""",
    traits_en=["Wise", "Virtuous", "Scholarly", "Patient", "Moral"],
    traits_ko=["지혜로운", "덕스러운", "학문적인", "인내하는", "도덕적인"],
    story_en="A disciple asked Confucius about the essence of his teaching. He replied: 'It is simply this: loyalty and consideration. Do not do to others what you would not want done to yourself.' This Golden Rule became the ethical foundation of Confucian thought.",
    story_ko="제자가 공자에게 가르침의 본질을 물었습니다. 그가 대답했습니다: '그것은 간단히 충(忠)과 서(恕)입니다. 자신이 원하지 않는 것을 남에게 하지 마십시오.' 이 황금률은 유교 사상의 윤리적 기초가 되었습니다.",
    match_message_en="Your features reflect the cultivated wisdom of Confucius. There is a gentle scholarly quality to your face—patient, thoughtful, and deeply moral. Your expression speaks of one who values education, virtue, and the proper ordering of relationships.",
    match_message_ko="당신의 이목구비는 공자의 수양된 지혜를 반영합니다. 당신의 얼굴에는 부드러운 학자적 품질이 있습니다—인내심 있고, 사려 깊고, 깊이 도덕적인. 당신의 표정은 교육, 덕, 그리고 인간관계의 올바른 질서를 중시하는 사람을 말해줍니다.",
    image_prompt="Ancient Chinese sage with long grey beard, kind wise eyes, wearing traditional Han dynasty scholar robes, holding bamboo scroll with Chinese characters, students listening in background, peaceful Chinese garden setting, gentle wise expression, warm scholarly atmosphere",
    visual_description="Round gentle face, soft wise eyes, long thin beard, scholarly dignified appearance, patient serene expression, embodiment of cultivated virtue",
    aliases=["孔子", "Kong Zi", "Kong Qiu", "Master Kong"],
    era="Spring and Autumn Period (551-479 BCE)",
    related_characters=["mencius", "laozi", "zhuangzi", "zhuxi"]
)

GUAN_YU_DESC = CharacterDescription(
    id="guan_yu",
    name_en="Guan Yu",
    name_ko="관우",
    tagline_en="God of War, Symbol of Loyalty and Righteousness",
    tagline_ko="전쟁의 신, 충의와 의리의 상징",
    description_en="""Guan Yu was a legendary general during China's Three Kingdoms period (220-280 CE), whose unwavering loyalty to his sworn brother Liu Bei made him the eternal symbol of righteousness in Chinese culture. After his death, he was deified and is worshipped as the God of War.

His distinctive appearance—tall stature, red face, long flowing beard, and crescent moon blade (guandao)—made him instantly recognizable. But it was his character that earned immortality: he refused enormous bribes and honors from rival lord Cao Cao, traveling thousands of miles to return to Liu Bei.

Today, Guan Yu is worshipped not only by soldiers but by police, triads, and businessmen alike. He represents the virtues of loyalty, righteousness, and keeping one's word regardless of personal cost.""",
    description_ko="""관우는 중국 삼국시대(220-280년)의 전설적인 장군으로, 의형제 유비에 대한 흔들림 없는 충성심으로 중국 문화에서 의로움의 영원한 상징이 되었습니다. 사후 신격화되어 전쟁의 신으로 숭배받습니다.

그의 독특한 외모—큰 키, 붉은 얼굴, 길게 흐르는 수염, 그리고 청룡언월도—는 그를 즉시 알아볼 수 있게 했습니다. 그러나 불멸을 얻게 한 것은 그의 인격이었습니다: 그는 적장 조조의 엄청난 뇌물과 영예를 거절하고, 유비에게 돌아가기 위해 천 리를 여행했습니다.

오늘날 관우는 군인뿐 아니라 경찰, 조직폭력배, 사업가들에게도 숭배됩니다. 그는 충성, 의로움, 그리고 개인적 대가와 관계없이 약속을 지키는 덕목을 대표합니다.""",
    traits_en=["Loyal", "Righteous", "Brave", "Honorable", "Fierce"],
    traits_ko=["충성스러운", "의로운", "용감한", "명예로운", "맹렬한"],
    story_en="Cao Cao captured Guan Yu and showered him with gifts, titles, and a beautiful wife, hoping to win his loyalty. Guan Yu accepted nothing, and when he learned Liu Bei's location, he returned every gift and departed. He passed through five passes, slaying six generals who tried to stop him.",
    story_ko="조조는 관우를 사로잡고 선물, 직위, 아름다운 아내를 주며 그의 충성을 얻으려 했습니다. 관우는 아무것도 받지 않았고, 유비의 위치를 알게 되자 모든 선물을 돌려주고 떠났습니다. 그는 다섯 관문을 지나며 그를 막으려는 여섯 장군을 베었습니다.",
    match_message_en="Your features carry the fierce loyalty of Guan Yu. There is strength and unwavering resolve in your face—the look of one who would never betray a trust or break a promise. Your intense gaze speaks of righteousness that cannot be bought or compromised.",
    match_message_ko="당신의 이목구비는 관우의 맹렬한 충성심을 담고 있습니다. 당신의 얼굴에는 힘과 흔들림 없는 결의가 있습니다—절대 신뢰를 배신하거나 약속을 어기지 않을 사람의 모습. 당신의 강렬한 눈빛은 사거나 타협할 수 없는 의로움을 말해줍니다.",
    image_prompt="Mighty Chinese warrior god with distinctive red face, long flowing black beard, fierce loyal eyes, wearing green robes and armor, holding the Green Dragon Crescent Blade (guandao), dramatic battle stance, Chinese temple or battlefield background, heroic divine warrior",
    visual_description="Square strong jaw, intense fierce eyes, prominent red-toned features, long beard, powerful commanding presence, expression of fierce loyalty",
    aliases=["关羽", "Guan Gong", "Lord Guan", "武聖"],
    era="Three Kingdoms Period (160-220 CE)",
    related_characters=["liu_bei", "zhang_fei", "zhuge_liang", "cao_cao"]
)


# ============================================
# EGYPTIAN MYTHOLOGY DESCRIPTIONS
# ============================================

RA_DESC = CharacterDescription(
    id="ra",
    name_en="Ra",
    name_ko="라",
    tagline_en="Supreme Sun God, Creator of All Life",
    tagline_ko="최고의 태양신, 모든 생명의 창조자",
    description_en="""Ra is the supreme deity of ancient Egyptian religion, the god of the sun and creator of all life. Each day, he sails his solar barque across the sky, bringing light and warmth to the world. Each night, he travels through the underworld, battling the chaos serpent Apophis to ensure the sun rises again.

As the first god, Ra created himself from the primordial waters of Nun, then spoke all other gods and the world into existence. He is depicted with a falcon head crowned with the sun disk, embodying the life-giving power of the sun itself.

Ra's name means simply "sun," and his influence was so great that he merged with other major gods—becoming Amun-Ra, king of the gods, and Ra-Horakhty, god of the horizon. He represents the eternal cycle of death and rebirth that defined Egyptian cosmology.""",
    description_ko="""라는 고대 이집트 종교의 최고 신으로, 태양의 신이자 모든 생명의 창조자입니다. 매일 그는 태양의 배를 타고 하늘을 가로질러 세상에 빛과 온기를 가져다줍니다. 매일 밤, 그는 지하세계를 여행하며 혼돈의 뱀 아포피스와 싸워 태양이 다시 떠오르도록 합니다.

최초의 신으로서, 라는 눈의 원초적 물에서 스스로를 창조한 후, 모든 다른 신들과 세계를 말로 존재하게 했습니다. 그는 태양 원반으로 왕관을 쓴 매의 머리로 묘사되며, 태양 자체의 생명을 주는 힘을 구현합니다.

라의 이름은 단순히 "태양"을 의미하며, 그의 영향력은 너무 커서 다른 주요 신들과 합쳐졌습니다—신들의 왕 아문-라, 지평선의 신 라-호라크티가 되었습니다. 그는 이집트 우주론을 정의한 죽음과 재탄생의 영원한 순환을 대표합니다.""",
    traits_en=["Radiant", "Eternal", "Creative", "Powerful", "Life-giving"],
    traits_ko=["빛나는", "영원한", "창조적인", "강력한", "생명을 주는"],
    story_en="Each night, Ra descends into the Duat (underworld) where the chaos serpent Apophis tries to devour him and prevent sunrise. With the help of other gods, particularly Set, Ra defeats Apophis each night, ensuring the sun rises again—symbolizing the eternal triumph of order over chaos.",
    story_ko="매일 밤, 라는 두아트(지하세계)로 내려가며 혼돈의 뱀 아포피스가 그를 삼켜 일출을 막으려 합니다. 다른 신들, 특히 세트의 도움으로 라는 매일 밤 아포피스를 물리쳐 태양이 다시 떠오르게 합니다—이는 혼돈에 대한 질서의 영원한 승리를 상징합니다.",
    match_message_en="Your features radiate the eternal brilliance of Ra. There is a warm, life-giving quality to your presence—commanding yet nurturing. Your face speaks of one who brings light wherever they go and whose spirit cannot be dimmed by darkness.",
    match_message_ko="당신의 이목구비는 라의 영원한 광채를 발산합니다. 당신의 존재에는 따뜻하고 생명을 주는 품질이 있습니다—위엄 있으면서도 양육하는. 당신의 얼굴은 가는 곳마다 빛을 가져다주고 어둠에 의해 정신이 꺾이지 않는 사람을 말해줍니다.",
    image_prompt="Majestic Egyptian god with falcon head, golden sun disk crown with uraeus cobra, wearing royal Egyptian regalia, holding ankh and was-scepter, blazing golden aura like the sun, Egyptian temple with hieroglyphics background, divine radiant light",
    visual_description="Sharp angular features, intense golden eyes, regal bearing, radiant warm complexion, commanding divine presence",
    aliases=["Re", "Amun-Ra", "Ra-Horakhty", "رع"],
    era="Ancient Egypt",
    related_characters=["horus", "isis", "osiris", "thoth", "set"]
)

ISIS_DESC = CharacterDescription(
    id="isis",
    name_en="Isis",
    name_ko="이시스",
    tagline_en="Goddess of Magic, Motherhood, and Wisdom",
    tagline_ko="마법, 모성, 지혜의 여신",
    description_en="""Isis is the greatest goddess of ancient Egypt, revered as the ideal mother, wife, and patron of magic. Her worship spread throughout the Roman Empire, making her one of the most beloved deities of the ancient world.

Sister and wife to Osiris, mother of Horus, Isis embodies the fierce protective love of motherhood. When Set murdered Osiris and scattered his body across Egypt, Isis searched tirelessly, gathered every piece, and used her unmatched magical powers to resurrect him long enough to conceive their son Horus.

As the goddess of magic, Isis possessed knowledge that rivaled even Ra himself. She is often depicted with a throne-shaped crown or cow horns with a sun disk, symbolizing her roles as queen and mother. Her name means "throne," representing the power behind the pharaoh.""",
    description_ko="""이시스는 고대 이집트의 가장 위대한 여신으로, 이상적인 어머니, 아내, 마법의 수호자로 숭배받았습니다. 그녀에 대한 숭배는 로마 제국 전역에 퍼져, 고대 세계에서 가장 사랑받는 신 중 하나가 되었습니다.

오시리스의 여동생이자 아내, 호루스의 어머니인 이시스는 모성의 맹렬한 보호적 사랑을 구현합니다. 세트가 오시리스를 살해하고 그의 몸을 이집트 전역에 흩뿌렸을 때, 이시스는 지칠 줄 모르고 찾아다니며 모든 조각을 모으고, 비할 데 없는 마법의 힘을 사용하여 그들의 아들 호루스를 잉태할 만큼 충분히 그를 부활시켰습니다.

마법의 여신으로서, 이시스는 라 자신에 필적하는 지식을 소유했습니다. 그녀는 종종 왕좌 모양의 왕관이나 태양 원반이 있는 소뿔로 묘사되며, 여왕과 어머니로서의 역할을 상징합니다. 그녀의 이름은 "왕좌"를 의미하며, 파라오 뒤의 권력을 대표합니다.""",
    traits_en=["Magical", "Devoted", "Wise", "Protective", "Compassionate"],
    traits_ko=["마법적인", "헌신적인", "지혜로운", "보호하는", "자비로운"],
    story_en="Isis tricked Ra into revealing his secret name by creating a serpent from his own spittle. When it bit him and only she could heal him, Ra was forced to tell her his true name, giving her power over him. This made Isis the most powerful magician in existence.",
    story_ko="이시스는 라의 침으로 뱀을 만들어 그의 비밀 이름을 밝히도록 속였습니다. 뱀이 그를 물었을 때 오직 그녀만이 그를 치유할 수 있었고, 라는 그녀에게 진정한 이름을 말해야 했으며, 이로써 그녀에게 그에 대한 권력을 주었습니다. 이것은 이시스를 존재하는 가장 강력한 마법사로 만들었습니다.",
    match_message_en="Your features reflect the profound wisdom and compassion of Isis. There is a nurturing yet powerful quality to your appearance—the look of one who protects fiercely and loves unconditionally. Your eyes hold the depth of ancient mysteries and maternal devotion.",
    match_message_ko="당신의 이목구비는 이시스의 깊은 지혜와 자비를 반영합니다. 당신의 외모에는 양육하면서도 강력한 품질이 있습니다—맹렬하게 보호하고 무조건적으로 사랑하는 사람의 모습. 당신의 눈은 고대의 신비와 모성적 헌신의 깊이를 담고 있습니다.",
    image_prompt="Beautiful Egyptian goddess with throne crown or cow horns with sun disk, flowing black hair, kohl-lined eyes, wearing white and gold robes, holding ankh and lotus, magical aura, wings spread protectively, ancient Egyptian temple background",
    visual_description="Elegant oval face, large expressive eyes with kohl, graceful features, serene yet powerful expression, beauty with depth and wisdom",
    aliases=["Aset", "Eset", "إيزيس"],
    era="Ancient Egypt",
    related_characters=["osiris", "horus", "set", "nephthys", "ra"]
)

OSIRIS_DESC = CharacterDescription(
    id="osiris",
    name_en="Osiris",
    name_ko="오시리스",
    tagline_en="God of the Underworld, Death, and Resurrection",
    tagline_ko="지하세계, 죽음, 부활의 신",
    description_en="""Osiris is the god of the dead and ruler of the Egyptian underworld, but he is no god of darkness—he represents the hope of life after death and the promise of resurrection. As the first mummy and first resurrected being, he gave humanity the gift of eternal life.

Originally a great king who civilized Egypt, teaching agriculture and establishing laws, Osiris was murdered by his jealous brother Set. Through the magic of his devoted wife Isis, he was resurrected to rule the afterlife, judging the souls of the dead.

Depicted with green or black skin symbolizing rebirth and fertile soil, Osiris holds the crook and flail of kingship. He judges every soul in the Hall of Two Truths, weighing their hearts against the feather of Ma'at to determine their fate in eternity.""",
    description_ko="""오시리스는 죽은 자의 신이자 이집트 지하세계의 지배자이지만, 어둠의 신은 아닙니다—그는 사후 생명의 희망과 부활의 약속을 대표합니다. 최초의 미라이자 최초의 부활한 존재로서, 그는 인류에게 영원한 생명의 선물을 주었습니다.

원래 이집트를 문명화하고 농업을 가르치고 법을 세운 위대한 왕이었던 오시리스는 질투심 많은 형제 세트에 의해 살해되었습니다. 헌신적인 아내 이시스의 마법을 통해, 그는 죽은 자들의 영혼을 심판하며 사후세계를 다스리기 위해 부활했습니다.

재탄생과 비옥한 토양을 상징하는 녹색 또는 검은 피부로 묘사되며, 오시리스는 왕권의 갈고리와 도리깨를 들고 있습니다. 그는 두 진실의 전당에서 모든 영혼을 심판하며, 마아트의 깃털에 대해 그들의 심장을 달아 영원에서의 운명을 결정합니다.""",
    traits_en=["Just", "Resurrected", "Merciful", "Eternal", "Civilizing"],
    traits_ko=["공정한", "부활한", "자비로운", "영원한", "문명화하는"],
    story_en="Set trapped Osiris in a golden coffin and threw it into the Nile. Isis searched the world and found it in Byblos, grown into a great tree. But Set found the body again, cut it into fourteen pieces, and scattered them across Egypt. Isis gathered every piece, and with her magic, resurrected Osiris as lord of the afterlife.",
    story_ko="세트는 오시리스를 황금 관에 가두고 나일강에 던졌습니다. 이시스는 세계를 수색하여 비블로스에서 큰 나무로 자란 것을 발견했습니다. 그러나 세트가 시신을 다시 발견하여 열네 조각으로 잘라 이집트 전역에 흩뿌렸습니다. 이시스는 모든 조각을 모았고, 그녀의 마법으로 오시리스를 사후세계의 왕으로 부활시켰습니다.",
    match_message_en="Your features carry the solemn dignity of Osiris. There is a quiet strength in your face—the look of one who has endured great trials and emerged transformed. Your expression speaks of fair judgment and the wisdom that comes from profound experience.",
    match_message_ko="당신의 이목구비는 오시리스의 엄숙한 존엄을 담고 있습니다. 당신의 얼굴에는 조용한 힘이 있습니다—큰 시련을 견디고 변형되어 나온 사람의 모습. 당신의 표정은 공정한 심판과 깊은 경험에서 오는 지혜를 말해줍니다.",
    image_prompt="Majestic Egyptian god with green skin symbolizing rebirth, wearing atef crown with ostrich feathers, wrapped in white mummy bandages, holding crook and flail crossed over chest, serene expression, underworld throne room with scales of justice, divine peaceful light",
    visual_description="Serene dignified face, calm wise eyes, features that suggest both death and renewal, peaceful yet authoritative expression",
    aliases=["Usir", "Wesir", "أوزيريس"],
    era="Ancient Egypt",
    related_characters=["isis", "horus", "set", "nephthys", "anubis"]
)

ANUBIS_DESC = CharacterDescription(
    id="anubis",
    name_en="Anubis",
    name_ko="아누비스",
    tagline_en="God of Mummification and Guide of Souls",
    tagline_ko="미라화의 신이자 영혼의 인도자",
    description_en="""Anubis is the jackal-headed god of mummification, funerary rites, and the guardian of the dead. He invented embalming when he helped Isis prepare Osiris's body, creating the first mummy and establishing the sacred rituals that preserved Egyptian bodies for eternal life.

As the guide of souls, Anubis leads the deceased through the underworld to the Hall of Two Truths, where he performs the crucial weighing of the heart ceremony. With precise and impartial judgment, he places the heart on the scales against the feather of Ma'at.

Despite his association with death, Anubis is not a fearsome deity—he is a protector and helper, ensuring that the dead receive proper rites and safely reach the afterlife. His black color represents not death but the fertile Nile soil and the promise of regeneration.""",
    description_ko="""아누비스는 미라화, 장례 의식의 자칼 머리 신이자 죽은 자의 수호자입니다. 그는 이시스가 오시리스의 시신을 준비하는 것을 도우며 방부 처리를 발명하여, 최초의 미라를 만들고 이집트 시신을 영원한 생명을 위해 보존하는 신성한 의식을 확립했습니다.

영혼의 인도자로서, 아누비스는 죽은 자를 지하세계를 통해 두 진실의 전당으로 인도하며, 거기서 중요한 심장 무게 재기 의식을 수행합니다. 정확하고 공정한 판단으로, 그는 마아트의 깃털에 대해 심장을 저울 위에 놓습니다.

죽음과의 연관에도 불구하고, 아누비스는 두려운 신이 아닙니다—그는 보호자이자 도우미로, 죽은 자들이 적절한 의식을 받고 안전하게 사후세계에 도달하도록 보장합니다. 그의 검은색은 죽음이 아니라 비옥한 나일강 토양과 재생의 약속을 대표합니다.""",
    traits_en=["Protective", "Precise", "Impartial", "Guiding", "Sacred"],
    traits_ko=["보호하는", "정확한", "공정한", "인도하는", "신성한"],
    story_en="When Osiris was murdered, Anubis performed the first mummification, wrapping the god's body with sacred bandages and performing the rituals that would allow Osiris to live eternally in the afterlife. This sacred knowledge was then passed to Egyptian priests.",
    story_ko="오시리스가 살해되었을 때, 아누비스는 최초의 미라화를 수행하여 신의 몸을 신성한 붕대로 감싸고 오시리스가 사후세계에서 영원히 살 수 있게 하는 의식을 행했습니다. 이 신성한 지식은 그 후 이집트 사제들에게 전해졌습니다.",
    match_message_en="Your features bear the solemn guardianship of Anubis. There is a protective, watchful quality to your face—the look of one who guides others through dark passages safely. Your steady gaze speaks of impartial judgment and the sacred duty to protect.",
    match_message_ko="당신의 이목구비는 아누비스의 엄숙한 수호를 지니고 있습니다. 당신의 얼굴에는 보호적이고 경계하는 품질이 있습니다—다른 사람들을 어두운 통로를 통해 안전하게 인도하는 사람의 모습. 당신의 꾸준한 눈빛은 공정한 심판과 보호해야 할 신성한 의무를 말해줍니다.",
    image_prompt="Powerful Egyptian god with black jackal head, pointed ears alert, golden Egyptian jewelry and collar, holding ankh and was-scepter, scales of judgment nearby, dark underworld temple setting with canopic jars, mysterious sacred atmosphere",
    visual_description="Sharp angular features, alert watchful eyes, dignified bearing, features suggesting both gentleness and authority, protective guardian appearance",
    aliases=["Anpu", "Inpu", "أنوبيس"],
    era="Ancient Egypt",
    related_characters=["osiris", "isis", "thoth", "set", "nephthys"]
)

HORUS_DESC = CharacterDescription(
    id="horus",
    name_en="Horus",
    name_ko="호루스",
    tagline_en="God of Sky, Kingship, and Protection",
    tagline_ko="하늘, 왕권, 보호의 신",
    description_en="""Horus is the falcon-headed god of the sky, whose eyes are the sun and moon. He is the divine prototype of all pharaohs, and every Egyptian king was considered a living manifestation of Horus on earth.

Son of Isis and Osiris, Horus was raised in secret to one day avenge his father's murder by Set. After a series of fierce battles that lasted eighty years, Horus defeated Set and claimed the throne of Egypt, unifying the Two Lands under his divine rule.

The Eye of Horus, lost and restored during his battles with Set, became one of the most powerful symbols in Egyptian magic—representing healing, protection, and the restoration of what was broken. Horus embodies rightful kingship, filial piety, and the triumph of order.""",
    description_ko="""호루스는 하늘의 매 머리 신으로, 그의 눈은 태양과 달입니다. 그는 모든 파라오의 신성한 원형이며, 모든 이집트 왕은 지상에서 호루스의 살아있는 현현으로 여겨졌습니다.

이시스와 오시리스의 아들인 호루스는 언젠가 아버지의 살인에 대해 세트에게 복수하기 위해 비밀리에 양육되었습니다. 80년 동안 지속된 일련의 치열한 전투 끝에, 호루스는 세트를 물리치고 이집트의 왕좌를 차지하여 그의 신성한 통치 아래 두 땅을 통일했습니다.

세트와의 전투 중 잃어버리고 회복된 호루스의 눈은 이집트 마법에서 가장 강력한 상징 중 하나가 되었습니다—치유, 보호, 그리고 깨진 것의 회복을 대표합니다. 호루스는 정당한 왕권, 효도, 그리고 질서의 승리를 구현합니다.""",
    traits_en=["Righteous", "Protective", "Victorious", "Royal", "Avenging"],
    traits_ko=["의로운", "보호하는", "승리하는", "왕족의", "복수하는"],
    story_en="During their battles, Set tore out Horus's left eye and Horus castrated Set. The god Thoth restored Horus's eye, which became the wedjat—the Eye of Horus—symbol of healing and wholeness. The gods judged in Horus's favor, granting him the throne of Egypt.",
    story_ko="전투 중, 세트는 호루스의 왼쪽 눈을 뽑았고 호루스는 세트를 거세했습니다. 토트 신이 호루스의 눈을 회복시켰고, 이것이 웨자트—호루스의 눈—치유와 온전함의 상징이 되었습니다. 신들은 호루스의 편에서 판결하여 그에게 이집트의 왕좌를 주었습니다.",
    match_message_en="Your features carry the noble bearing of Horus. There is a sharp, protective quality to your gaze—the look of a rightful ruler who fights for justice. Your face speaks of one who overcomes all obstacles to claim their rightful place.",
    match_message_ko="당신의 이목구비는 호루스의 고귀한 품위를 담고 있습니다. 당신의 눈빛에는 날카롭고 보호적인 품질이 있습니다—정의를 위해 싸우는 정당한 통치자의 모습. 당신의 얼굴은 정당한 자리를 차지하기 위해 모든 장애물을 극복하는 사람을 말해줍니다.",
    image_prompt="Noble Egyptian god with falcon head, wearing double crown of Upper and Lower Egypt (pschent), Eye of Horus glowing, holding was-scepter and ankh, royal Egyptian regalia, sky and sun behind him, victorious powerful pose",
    visual_description="Sharp noble features, piercing intense eyes, regal bearing, features suggesting both warrior strength and divine kingship",
    aliases=["Heru", "Hor", "حورس"],
    era="Ancient Egypt",
    related_characters=["isis", "osiris", "set", "hathor", "ra"]
)

BASTET_DESC = CharacterDescription(
    id="bastet",
    name_en="Bastet",
    name_ko="바스테트",
    tagline_en="Goddess of Home, Cats, and Protection",
    tagline_ko="가정, 고양이, 보호의 여신",
    description_en="""Bastet is the cat-headed goddess of home, fertility, and protection. Originally depicted as a fierce lioness warrior, she evolved into the more gentle domestic cat goddess beloved by Egyptian families as their divine protector.

As a guardian deity, Bastet protected households from evil spirits, disease, and misfortune. Cats were sacred to her, and killing a cat—even accidentally—was punishable by death in ancient Egypt. Her temple at Bubastis was one of the most popular pilgrimage sites.

Despite her domestic associations, Bastet retained her fierce protective nature. She was called the "Eye of Ra" and could transform into the fearsome lioness Sekhmet when defending the innocent. She embodies the dual nature of cats—gentle and nurturing, yet capable of fierce protection.""",
    description_ko="""바스테트는 가정, 다산, 보호의 고양이 머리 여신입니다. 원래 맹렬한 암사자 전사로 묘사되었으나, 이집트 가정들이 신성한 보호자로 사랑하는 더 온화한 집고양이 여신으로 진화했습니다.

수호 신으로서, 바스테트는 가정을 악령, 질병, 불운으로부터 보호했습니다. 고양이는 그녀에게 신성했고, 고양이를 죽이는 것은—우연히라도—고대 이집트에서 사형에 처해질 수 있었습니다. 부바스티스에 있는 그녀의 신전은 가장 인기 있는 순례지 중 하나였습니다.

가정적 연관에도 불구하고, 바스테트는 맹렬한 보호적 본성을 유지했습니다. 그녀는 "라의 눈"이라 불렸고 무고한 자를 방어할 때 무시무시한 암사자 세크메트로 변신할 수 있었습니다. 그녀는 고양이의 이중적 본성을 구현합니다—온화하고 양육하면서도 맹렬한 보호가 가능한.""",
    traits_en=["Protective", "Graceful", "Nurturing", "Fierce", "Domestic"],
    traits_ko=["보호하는", "우아한", "양육하는", "맹렬한", "가정적인"],
    story_en="Every year, hundreds of thousands of pilgrims traveled to Bubastis for Bastet's festival, the largest in Egypt. They sailed down the Nile on boats, playing music and celebrating. At the temple, they brought mummified cats as offerings to the beloved goddess.",
    story_ko="매년, 수십만 명의 순례자들이 이집트에서 가장 큰 축제인 바스테트 축제를 위해 부바스티스로 여행했습니다. 그들은 배를 타고 나일강을 내려가며 음악을 연주하고 축하했습니다. 신전에서 그들은 사랑받는 여신에게 미라가 된 고양이를 제물로 바쳤습니다.",
    match_message_en="Your features reflect the graceful protection of Bastet. There is a gentle yet alert quality to your appearance—nurturing warmth combined with quiet vigilance. Your face speaks of one who creates safe havens and fiercely protects those they love.",
    match_message_ko="당신의 이목구비는 바스테트의 우아한 보호를 반영합니다. 당신의 외모에는 온화하면서도 민첩한 품질이 있습니다—조용한 경계와 결합된 양육적 온기. 당신의 얼굴은 안전한 피난처를 만들고 사랑하는 사람들을 맹렬하게 보호하는 사람을 말해줍니다.",
    image_prompt="Elegant Egyptian goddess with cat head, large alert green or gold eyes, wearing golden Egyptian jewelry and sistrum rattle, surrounded by cats, sitting gracefully in home temple setting, warm protective atmosphere, both gentle and fierce aspects",
    visual_description="Graceful features, large alert eyes, elegant bearing, expression of gentle warmth with underlying alertness, cat-like grace",
    aliases=["Bast", "Ubasti", "باستت"],
    era="Ancient Egypt",
    related_characters=["sekhmet", "ra", "hathor", "mut"]
)

SEKHMET_DESC = CharacterDescription(
    id="sekhmet",
    name_en="Sekhmet",
    name_ko="세크메트",
    tagline_en="Goddess of War, Destruction, and Healing",
    tagline_ko="전쟁, 파괴, 치유의 여신",
    description_en="""Sekhmet is the lioness-headed goddess of war and destruction, whose name means "She Who Is Powerful." Ra created her as his weapon of divine vengeance, and her fury is so terrible that she once nearly destroyed all humanity.

As the "Eye of Ra," Sekhmet embodied the scorching heat of the sun and the fury of divine judgment. Plagues and epidemics were attributed to her "messengers," and only her priests knew the rituals to appease her wrath.

Yet Sekhmet is also a goddess of healing. Her priests were renowned physicians, and she protected against the very diseases she could inflict. This duality—destruction and healing, war and medicine—reflects the ancient understanding that the power to harm and heal are two sides of the same force.""",
    description_ko="""세크메트는 전쟁과 파괴의 암사자 머리 여신으로, 그녀의 이름은 "강력한 그녀"를 의미합니다. 라가 그녀를 신성한 복수의 무기로 창조했고, 그녀의 분노는 너무 끔찍하여 한때 거의 모든 인류를 멸망시킬 뻔했습니다.

"라의 눈"으로서, 세크메트는 태양의 타오르는 열기와 신성한 심판의 분노를 구현했습니다. 역병과 전염병은 그녀의 "사자들" 탓으로 돌려졌고, 오직 그녀의 사제들만이 그녀의 분노를 달래는 의식을 알았습니다.

그러나 세크메트는 치유의 여신이기도 합니다. 그녀의 사제들은 유명한 의사들이었고, 그녀는 자신이 가할 수 있는 바로 그 질병들로부터 보호했습니다. 이 이중성—파괴와 치유, 전쟁과 의학—은 해를 끼치고 치유하는 힘이 같은 힘의 양면이라는 고대의 이해를 반영합니다.""",
    traits_en=["Powerful", "Fierce", "Healing", "Destructive", "Protective"],
    traits_ko=["강력한", "맹렬한", "치유하는", "파괴적인", "보호하는"],
    story_en="Ra sent Sekhmet to punish rebellious humans, but she became drunk on blood and would not stop killing. To save humanity, Ra flooded the fields with beer dyed red like blood. Sekhmet drank it, became intoxicated, and forgot her rampage, transforming into the gentle Hathor.",
    story_ko="라는 반항적인 인간들을 벌하기 위해 세크메트를 보냈지만, 그녀는 피에 취해 죽이는 것을 멈추지 않았습니다. 인류를 구하기 위해, 라는 피처럼 붉게 물들인 맥주로 들판을 가득 채웠습니다. 세크메트가 그것을 마시고 취해 난동을 잊었고, 온화한 하토르로 변신했습니다.",
    match_message_en="Your features carry the fierce power of Sekhmet. There is an intensity to your gaze that speaks of one capable of both great destruction and great healing. Your face reflects the understanding that true strength includes the power to protect and to restore.",
    match_message_ko="당신의 이목구비는 세크메트의 맹렬한 힘을 담고 있습니다. 당신의 눈빛에는 큰 파괴와 큰 치유 모두가 가능한 사람을 말해주는 강렬함이 있습니다. 당신의 얼굴은 진정한 힘이 보호하고 회복시키는 힘을 포함한다는 이해를 반영합니다.",
    image_prompt="Fierce Egyptian goddess with lioness head, wild mane, red sun disk crown, wearing blood-red robes, holding papyrus wand and ankh, flames and battlefield behind her, fearsome yet majestic, divine fury and healing power combined",
    visual_description="Fierce powerful features, intense blazing eyes, wild mane-like hair, expression of controlled fury and ancient power",
    aliases=["Sachmis", "Sakhmet", "سخمت"],
    era="Ancient Egypt",
    related_characters=["ra", "bastet", "hathor", "ptah", "mut"]
)

THOTH_DESC = CharacterDescription(
    id="thoth",
    name_en="Thoth",
    name_ko="토트",
    tagline_en="God of Wisdom, Writing, and Magic",
    tagline_ko="지혜, 기록, 마법의 신",
    description_en="""Thoth is the ibis-headed god of wisdom, writing, magic, and the moon. He is credited with inventing hieroglyphics, creating the calendar, and recording all knowledge in existence. Without Thoth's gift of writing, Egyptian civilization could not exist.

As the divine scribe, Thoth records the verdict of every soul in the Hall of Two Truths, documenting who passes into the afterlife and who is condemned. He also authored the sacred texts containing all magical knowledge, including the legendary Book of Thoth.

Thoth serves as mediator among the gods, using his wisdom and eloquence to resolve disputes. He restored Horus's eye and healed both Horus and Set after their battles. His mastery of magic is second to none, and he taught Isis the spells that allowed her to resurrect Osiris.""",
    description_ko="""토트는 지혜, 기록, 마법, 달의 따오기 머리 신입니다. 그는 상형문자를 발명하고, 달력을 만들고, 존재하는 모든 지식을 기록한 공로를 인정받습니다. 토트의 기록 선물 없이는 이집트 문명이 존재할 수 없었습니다.

신성한 서기관으로서, 토트는 두 진실의 전당에서 모든 영혼의 평결을 기록하며, 누가 사후세계로 넘어가고 누가 정죄되는지를 문서화합니다. 그는 또한 전설적인 토트의 책을 포함한 모든 마법 지식이 담긴 신성한 텍스트를 저술했습니다.

토트는 신들 사이의 중재자로서, 지혜와 웅변으로 분쟁을 해결합니다. 그는 호루스의 눈을 회복시켰고 전투 후 호루스와 세트 모두를 치유했습니다. 그의 마법 숙련도는 타의 추종을 불허하며, 이시스에게 오시리스를 부활시킬 수 있게 한 주문을 가르쳤습니다.""",
    traits_en=["Wise", "Scholarly", "Magical", "Eloquent", "Recording"],
    traits_ko=["지혜로운", "학문적인", "마법적인", "웅변의", "기록하는"],
    story_en="Thoth gambled with the Moon and won enough light to create five extra days, allowing Nut to give birth to Osiris, Isis, Set, Nephthys, and Horus the Elder—circumventing Ra's curse that she could bear no children in any month of the year.",
    story_ko="토트는 달과 도박을 하여 5일을 추가로 만들 만큼 충분한 빛을 이겨, 누트가 오시리스, 이시스, 세트, 네프티스, 그리고 대 호루스를 낳을 수 있게 했습니다—그녀가 한 해의 어떤 달에도 아이를 낳을 수 없다는 라의 저주를 피해서.",
    match_message_en="Your features reflect the scholarly wisdom of Thoth. There is an intellectual depth to your appearance—the look of one who values knowledge above all and seeks to understand the mysteries of existence. Your thoughtful expression speaks of both reason and magic.",
    match_message_ko="당신의 이목구비는 토트의 학문적 지혜를 반영합니다. 당신의 외모에는 지적인 깊이가 있습니다—무엇보다 지식을 중시하고 존재의 신비를 이해하려는 사람의 모습. 당신의 사려 깊은 표정은 이성과 마법 모두를 말해줍니다.",
    image_prompt="Wise Egyptian god with ibis head, long curved beak, wearing lunar disk and crescent crown, holding reed pen and palette or scroll, surrounded by hieroglyphic texts and books, library temple setting with moonlight, scholarly sacred atmosphere",
    visual_description="Long refined features, contemplative eyes, scholarly bearing, expression of deep thought and ancient knowledge",
    aliases=["Djehuti", "Tehuti", "Hermes Trismegistus", "تحوت"],
    era="Ancient Egypt",
    related_characters=["ra", "isis", "osiris", "ma'at", "seshat"]
)

SET_DESC = CharacterDescription(
    id="set",
    name_en="Set",
    name_ko="세트",
    tagline_en="God of Chaos, Storms, and the Desert",
    tagline_ko="혼돈, 폭풍, 사막의 신",
    description_en="""Set is the god of chaos, storms, violence, and the harsh desert. He is best known as the murderer of his brother Osiris, yet he is not simply evil—he is a necessary force of disorder that makes order meaningful.

With his distinctive Set-animal head (perhaps part aardvark, part donkey, part jackal), Set represents all that is foreign, wild, and untamed. He is the red land of the desert against the black fertile soil of the Nile, the outsider who challenges the established order.

Despite his villainous role in the Osiris myth, Set served an essential function. Each night aboard Ra's solar barque, Set's tremendous strength defeats the chaos serpent Apophis, ensuring the sun rises again. Without Set's violence, there would be no sunrise. He embodies the paradox that destruction is necessary for creation.""",
    description_ko="""세트는 혼돈, 폭풍, 폭력, 가혹한 사막의 신입니다. 그는 형제 오시리스의 살인자로 가장 잘 알려져 있지만, 단순히 악한 것은 아닙니다—그는 질서를 의미 있게 만드는 필수적인 무질서의 힘입니다.

독특한 세트-동물 머리(아마도 땅돼지, 당나귀, 자칼의 일부)를 가진 세트는 외국적이고, 야생적이고, 길들여지지 않은 모든 것을 대표합니다. 그는 나일강의 검은 비옥한 토양에 대항하는 사막의 붉은 땅이자, 확립된 질서에 도전하는 외부인입니다.

오시리스 신화에서의 악역에도 불구하고, 세트는 필수적인 기능을 수행했습니다. 매일 밤 라의 태양 배에서, 세트의 엄청난 힘이 혼돈의 뱀 아포피스를 물리쳐 태양이 다시 떠오르게 합니다. 세트의 폭력이 없다면, 일출이 없을 것입니다. 그는 파괴가 창조에 필요하다는 역설을 구현합니다.""",
    traits_en=["Chaotic", "Powerful", "Necessary", "Violent", "Unpredictable"],
    traits_ko=["혼란스러운", "강력한", "필수적인", "폭력적인", "예측불가한"],
    story_en="Set tricked Osiris at a banquet by displaying a beautiful coffin and promising it to whoever fit perfectly inside. When Osiris lay down, Set slammed the lid and threw the coffin into the Nile. This murder set in motion the great conflict with Horus that shaped Egyptian mythology.",
    story_ko="세트는 연회에서 아름다운 관을 전시하고 안에 완벽하게 맞는 사람에게 주겠다고 약속하며 오시리스를 속였습니다. 오시리스가 누웠을 때, 세트는 뚜껑을 세게 닫고 관을 나일강에 던졌습니다. 이 살인은 이집트 신화를 형성한 호루스와의 큰 갈등을 시작하게 했습니다.",
    match_message_en="Your features carry the raw power of Set. There is an untamed, challenging quality to your appearance—the look of one who exists outside conventional boundaries. Your face speaks of the strength found in chaos and the necessity of disruption for change.",
    match_message_ko="당신의 이목구비는 세트의 거친 힘을 담고 있습니다. 당신의 외모에는 길들여지지 않은, 도전적인 품질이 있습니다—관습적 경계 밖에 존재하는 사람의 모습. 당신의 얼굴은 혼돈에서 발견되는 힘과 변화를 위한 혼란의 필요성을 말해줍니다.",
    image_prompt="Powerful Egyptian god with mysterious Set-animal head (curved snout, tall square ears), red hair and eyes, wearing red and gold, surrounded by storms and desert sandstorms, muscular powerful build, both dangerous and necessary presence",
    visual_description="Sharp angular unusual features, intense restless eyes, wild appearance, expression of barely contained power and chaos",
    aliases=["Seth", "Sutekh", "Setesh", "ست"],
    era="Ancient Egypt",
    related_characters=["osiris", "isis", "horus", "nephthys", "apophis"]
)


# ============================================
# NORSE MYTHOLOGY - ADDITIONAL FIGURES
# ============================================

FRIGG_DESC = CharacterDescription(
    id="frigg",
    name_en="Frigg",
    name_ko="프리그",
    tagline_en="Queen of Asgard, Goddess of Marriage and Motherhood",
    tagline_ko="아스가르드의 여왕, 결혼과 모성의 여신",
    description_en="""Frigg is the queen of the Aesir gods and wife of Odin, ruling Asgard alongside the Allfather. She is the goddess of marriage, motherhood, and domestic arts, spinning the clouds from her palace Fensalir.

Unlike most gods, Frigg possesses the gift of foreknowledge—she knows the fates of all beings, though she never speaks of what she sees. This knowledge brings her both wisdom and sorrow, as she foresaw but could not prevent her son Baldur's death.

As the highest-ranking goddess, Frigg's authority is matched only by Odin himself. She is invoked for blessings on marriages and childbirth, and her wisdom in household matters made her the ideal of the Norse wife and mother.""",
    description_ko="""프리그는 아스가르드 신들의 여왕이자 오딘의 아내로, 만물의 아버지와 함께 아스가르드를 다스립니다. 그녀는 결혼, 모성, 가정 기술의 여신으로, 펜살리르 궁전에서 구름을 짜냅니다.

대부분의 신들과 달리, 프리그는 예지의 선물을 가지고 있습니다—그녀는 모든 존재의 운명을 알지만, 본 것에 대해 결코 말하지 않습니다. 이 지식은 그녀에게 지혜와 슬픔을 모두 가져다줍니다. 그녀는 아들 발드르의 죽음을 예견했지만 막을 수 없었습니다.

가장 높은 지위의 여신으로서, 프리그의 권위는 오딘 자신에게만 필적합니다. 그녀는 결혼과 출산에 대한 축복을 위해 기원되며, 가정 문제에 대한 지혜는 그녀를 북유럽 아내와 어머니의 이상으로 만들었습니다.""",
    traits_en=["Wise", "Foreseeing", "Maternal", "Regal", "Silent"],
    traits_ko=["지혜로운", "예지하는", "모성적인", "왕족다운", "침묵하는"],
    story_en="When Frigg foresaw Baldur's death, she traveled across all the nine realms, extracting promises from every creature and object never to harm him. But she overlooked the mistletoe, thinking it too young and harmless—a fatal mistake that Loki exploited.",
    story_ko="프리그가 발드르의 죽음을 예견했을 때, 그녀는 아홉 세계를 모두 여행하며 모든 생명체와 물체로부터 그를 해치지 않겠다는 약속을 받아냈습니다. 그러나 그녀는 겨우살이가 너무 어리고 무해하다고 생각하여 간과했고—이것이 로키가 이용한 치명적인 실수였습니다.",
    match_message_en="Your features reflect the quiet wisdom of Frigg. There is a knowing depth to your eyes—the look of one who sees much but speaks little. Your face carries the dignified strength of one who bears heavy knowledge with grace.",
    match_message_ko="당신의 이목구비는 프리그의 조용한 지혜를 반영합니다. 당신의 눈에는 아는 깊이가 있습니다—많이 보지만 적게 말하는 사람의 모습. 당신의 얼굴은 무거운 지식을 품위 있게 지닌 사람의 위엄 있는 힘을 담고 있습니다.",
    image_prompt="Regal Norse goddess in flowing white robes, spinning golden thread from clouds, crown of silver, wise knowing eyes that hold sorrow and wisdom, seated in misty palace Fensalir, falcon feathers, serene but sad expression",
    visual_description="Elegant mature features, wise knowing eyes, serene expression with underlying sadness, regal bearing, gentle but powerful presence",
    aliases=["Frigga", "Frige", "Frija"],
    era="Viking Age",
    related_characters=["odin", "baldur", "loki", "freya", "thor"]
)

BALDUR_DESC = CharacterDescription(
    id="baldur",
    name_en="Baldur",
    name_ko="발드르",
    tagline_en="God of Light, Joy, and Purity",
    tagline_ko="빛, 기쁨, 순수의 신",
    description_en="""Baldur is the beloved god of light, joy, purity, and beauty in Norse mythology. Son of Odin and Frigg, he was so fair and gracious that light shone from him, and he was loved by all beings in the nine realms.

His beauty was not merely physical—Baldur embodied all that was good and pure. He was the most beloved of all the gods, and his hall Breidablik was a place where nothing unclean could exist.

Baldur's death at Loki's machinations marks the beginning of the end for the Norse gods. His return from Hel after Ragnarök represents the hope of renewal and the rebirth of a purer world from the ashes of the old.""",
    description_ko="""발드르는 북유럽 신화에서 사랑받는 빛, 기쁨, 순수, 아름다움의 신입니다. 오딘과 프리그의 아들로, 그는 너무 아름답고 우아하여 빛이 그에게서 발산되었고, 아홉 세계의 모든 존재들에게 사랑받았습니다.

그의 아름다움은 단순히 육체적인 것이 아니었습니다—발드르는 선하고 순수한 모든 것을 구현했습니다. 그는 모든 신들 중 가장 사랑받았고, 그의 전당 브레이다블릭은 불결한 것이 존재할 수 없는 장소였습니다.

로키의 계략에 의한 발드르의 죽음은 북유럽 신들의 종말의 시작을 표시합니다. 라그나로크 후 헬에서의 그의 귀환은 갱신의 희망과 옛 세계의 잿더미에서 더 순수한 세계의 재탄생을 대표합니다.""",
    traits_en=["Pure", "Beautiful", "Beloved", "Radiant", "Innocent"],
    traits_ko=["순수한", "아름다운", "사랑받는", "빛나는", "순진한"],
    story_en="After Frigg secured promises from all things not to harm Baldur, the gods made sport of throwing weapons at him—all bounced off harmlessly. But Loki tricked blind Höðr into throwing a mistletoe dart, the one thing Frigg had overlooked. Baldur fell dead, and all creation wept.",
    story_ko="프리그가 모든 것으로부터 발드르를 해치지 않겠다는 약속을 받아낸 후, 신들은 그에게 무기를 던지는 것을 오락으로 삼았습니다—모두 무해하게 튕겨 나갔습니다. 그러나 로키는 눈먼 호드를 속여 프리그가 간과한 유일한 것인 겨우살이 화살을 던지게 했습니다. 발드르는 죽어 쓰러졌고, 모든 창조물이 울었습니다.",
    match_message_en="Your features radiate the pure light of Baldur. There is a luminous quality to your appearance—the look of one whose goodness shines outward. Your face speaks of inherent kindness and the beauty that comes from a pure heart.",
    match_message_ko="당신의 이목구비는 발드르의 순수한 빛을 발산합니다. 당신의 외모에는 빛나는 품질이 있습니다—선함이 밖으로 빛나는 사람의 모습. 당신의 얼굴은 내재된 친절함과 순수한 마음에서 오는 아름다움을 말해줍니다.",
    image_prompt="Radiantly beautiful Norse god with golden hair like sunlight, perfect features glowing with inner light, white and gold robes, surrounded by soft golden light, flowers blooming around him, expression of pure joy and innocence",
    visual_description="Perfect symmetrical features, radiant complexion, bright warm eyes, expression of pure goodness and joy, light seeming to emanate from within",
    aliases=["Balder", "Baldr", "The Beautiful"],
    era="Viking Age",
    related_characters=["odin", "frigg", "loki", "hodr", "nanna"]
)

TYR_DESC = CharacterDescription(
    id="tyr",
    name_en="Tyr",
    name_ko="티르",
    tagline_en="God of War, Justice, and Heroic Glory",
    tagline_ko="전쟁, 정의, 영웅적 영광의 신",
    description_en="""Tyr is the Norse god of war and justice, once considered the chief of the gods before Odin rose to prominence. Unlike the chaotic warfare of other war gods, Tyr represents the lawful aspects of battle—heroic courage, fair combat, and victory through honor.

He is most famous for his sacrifice: when the gods needed to bind the monstrous wolf Fenrir, only Tyr was brave enough to place his hand in the wolf's mouth as a pledge of good faith. When Fenrir realized he was trapped, he bit off Tyr's hand—but Tyr's sacrifice saved the gods.

Tyr embodies the warrior's code of honor, where keeping one's word matters more than personal loss. His missing hand is a constant reminder that sometimes justice requires sacrifice.""",
    description_ko="""티르는 북유럽의 전쟁과 정의의 신으로, 오딘이 부상하기 전에 한때 신들의 수장으로 여겨졌습니다. 다른 전쟁 신들의 혼란스러운 전쟁과 달리, 티르는 전투의 합법적인 측면—영웅적 용기, 공정한 전투, 명예를 통한 승리를 대표합니다.

그는 희생으로 가장 유명합니다: 신들이 괴물 늑대 펜리르를 묶어야 했을 때, 오직 티르만이 선의의 맹세로 늑대의 입에 손을 넣을 만큼 용감했습니다. 펜리르가 갇혔다는 것을 깨달았을 때, 그는 티르의 손을 물어뜯었습니다—그러나 티르의 희생은 신들을 구했습니다.

티르는 약속을 지키는 것이 개인적 손실보다 더 중요한 전사의 명예 규범을 구현합니다. 그의 잃어버린 손은 때때로 정의가 희생을 요구한다는 것을 끊임없이 상기시켜 줍니다.""",
    traits_en=["Brave", "Just", "Sacrificial", "Honorable", "Resolute"],
    traits_ko=["용감한", "공정한", "희생적인", "명예로운", "단호한"],
    story_en="Fenrir agreed to be bound only if one of the gods placed their hand in his mouth as surety. All the gods refused except Tyr. When the magical chain Gleipnir held, Fenrir bit off Tyr's hand in rage—but Tyr stood unflinching, having known the cost of keeping the gods safe.",
    story_ko="펜리르는 신들 중 한 명이 담보로 그의 입에 손을 넣는 조건으로만 묶이는 것에 동의했습니다. 티르를 제외한 모든 신들이 거부했습니다. 마법의 사슬 글레이프니르가 버텼을 때, 펜리르는 분노로 티르의 손을 물어뜯었습니다—그러나 티르는 신들을 안전하게 지키는 대가를 알면서도 눈 하나 깜짝하지 않고 서 있었습니다.",
    match_message_en="Your features carry the steadfast honor of Tyr. There is an unwavering quality to your gaze—the look of one who keeps their word regardless of personal cost. Your face speaks of courage that comes from deep conviction.",
    match_message_ko="당신의 이목구비는 티르의 확고한 명예를 담고 있습니다. 당신의 눈빛에는 흔들림 없는 품질이 있습니다—개인적 대가와 관계없이 약속을 지키는 사람의 모습. 당신의 얼굴은 깊은 신념에서 오는 용기를 말해줍니다.",
    image_prompt="Noble Norse warrior god with one hand, wearing battle armor, sword at side, resolute expression, standing at a thing (assembly) dispensing justice, wolves and ravens nearby, honorable warrior bearing despite missing hand",
    visual_description="Strong resolute features, steady unwavering eyes, noble warrior bearing, expression of absolute determination and honor",
    aliases=["Tiw", "Tiwaz", "Mars Thingsus"],
    era="Viking Age",
    related_characters=["odin", "fenrir", "thor", "loki"]
)

HEL_DESC = CharacterDescription(
    id="hel",
    name_en="Hel",
    name_ko="헬",
    tagline_en="Goddess of the Dead, Ruler of Helheim",
    tagline_ko="죽은 자의 여신, 헬헤임의 지배자",
    description_en="""Hel is the goddess of the dead and ruler of the underworld realm that bears her name. Daughter of Loki and the giantess Angrboda, she was cast into the depths by Odin and given dominion over those who die of old age, sickness, or without glory in battle.

Her appearance is striking and terrifying: one half of her body is that of a beautiful woman, the other half a corpse in decay. This duality reflects her domain between the living and the dead.

Though her realm is cold and cheerless compared to Valhalla, Hel is not evil—she is simply the keeper of those whose fate led them to her doors. She rules with grim fairness, neither cruel nor kind, accepting all who come to her regardless of their deeds in life.""",
    description_ko="""헬은 죽은 자의 여신이자 그녀의 이름을 딴 지하세계 영역의 지배자입니다. 로키와 거인 앙그르보다의 딸로, 오딘에 의해 심연으로 쫓겨나 노령, 질병, 또는 전투에서 영광 없이 죽은 자들에 대한 지배권을 받았습니다.

그녀의 외모는 인상적이고 무서습니다: 그녀의 몸 절반은 아름다운 여인의 것이고, 다른 절반은 부패 중인 시체입니다. 이 이중성은 산 자와 죽은 자 사이의 그녀의 영역을 반영합니다.

그녀의 영역은 발할라에 비해 춥고 우울하지만, 헬은 악하지 않습니다—그녀는 단순히 운명이 그녀의 문으로 이끈 자들의 관리인입니다. 그녀는 잔인하지도 친절하지도 않게 냉정한 공정함으로 다스리며, 삶에서의 행적과 관계없이 그녀에게 오는 모든 이를 받아들입니다.""",
    traits_en=["Impartial", "Inevitable", "Dual-natured", "Stern", "Accepting"],
    traits_ko=["공정한", "피할 수 없는", "이중적인", "엄격한", "받아들이는"],
    story_en="When the gods begged Hel to release Baldur from death, she agreed on one condition: every being in existence must weep for him. All creation wept except one giantess—actually Loki in disguise. Because of this, Baldur remains in Hel until Ragnarök.",
    story_ko="신들이 헬에게 발드르를 죽음에서 풀어달라고 간청했을 때, 그녀는 한 가지 조건으로 동의했습니다: 존재하는 모든 존재가 그를 위해 울어야 한다. 모든 창조물이 울었지만 한 거인 여성만 제외하고—실제로는 변장한 로키였습니다. 이 때문에 발드르는 라그나로크까지 헬에 남아 있습니다.",
    match_message_en="Your features carry the dual nature of Hel. There is a fascinating complexity to your appearance—beauty intertwined with depth and shadow. Your face speaks of one who accepts all aspects of existence without judgment.",
    match_message_ko="당신의 이목구비는 헬의 이중적 본성을 담고 있습니다. 당신의 외모에는 매혹적인 복잡성이 있습니다—깊이와 그림자와 얽힌 아름다움. 당신의 얼굴은 판단 없이 존재의 모든 측면을 받아들이는 사람을 말해줍니다.",
    image_prompt="Norse goddess with half her face beautiful and living, half skeletal or decayed, dark robes, crown of bones, seated on throne in misty underworld, the dead wandering in background, both terrible and majestic, cold blue light",
    visual_description="Striking contrasting features, one side beautiful one side shadowed or gaunt, penetrating eyes, expression of cold acceptance and inevitable fate",
    aliases=["Hela", "The Hidden One"],
    era="Viking Age",
    related_characters=["loki", "baldur", "odin", "fenrir", "jormungandr"]
)

HEIMDALL_DESC = CharacterDescription(
    id="heimdall",
    name_en="Heimdall",
    name_ko="헤임달",
    tagline_en="Guardian of Bifröst, Watchman of the Gods",
    tagline_ko="비프로스트의 수호자, 신들의 파수꾼",
    description_en="""Heimdall is the ever-vigilant guardian of Bifröst, the rainbow bridge connecting Asgard to the other realms. Born of nine mothers (the nine waves), he possesses senses so keen he can hear grass growing and see for hundreds of leagues in any direction.

He requires less sleep than a bird and can see equally well by night as by day. His golden teeth gleam, and he bears the Gjallarhorn, the great horn whose blast will signal the beginning of Ragnarök when the enemies of the gods finally march.

Heimdall stands eternal watch at the border of Asgard, the first line of defense against any threat. His vigilance never wavers, and his loyalty to the gods is absolute. At Ragnarök, he and Loki are destined to kill each other.""",
    description_ko="""헤임달은 아스가르드를 다른 영역들과 연결하는 무지개 다리 비프로스트의 영원한 수호자입니다. 아홉 어머니(아홉 파도)에게서 태어난 그는 너무 예리한 감각을 가져 풀이 자라는 소리를 들을 수 있고 어느 방향으로든 수백 리그를 볼 수 있습니다.

그는 새보다 적은 수면이 필요하고 밤과 낮을 똑같이 잘 볼 수 있습니다. 그의 금빛 이빨이 빛나고, 신들의 적이 마침내 행진할 때 라그나로크의 시작을 알릴 위대한 뿔 갈라르호른을 지닙니다.

헤임달은 아스가르드의 경계에서 영원한 감시를 서며, 어떤 위협에 대해서도 첫 번째 방어선입니다. 그의 경계는 결코 흔들리지 않으며, 신들에 대한 충성은 절대적입니다. 라그나로크에서, 그와 로키는 서로를 죽일 운명입니다.""",
    traits_en=["Vigilant", "Loyal", "All-seeing", "Steadfast", "Guardian"],
    traits_ko=["경계하는", "충성스러운", "모든 것을 보는", "확고한", "수호하는"],
    story_en="Heimdall once retrieved Freya's necklace Brísingamen when Loki stole it. Both gods transformed into seals to battle in the sea, and Heimdall proved victorious. This enmity between them will culminate at Ragnarök when they finally destroy each other.",
    story_ko="헤임달은 로키가 훔쳤을 때 프레이야의 목걸이 브리싱가멘을 되찾은 적이 있습니다. 두 신은 바다에서 싸우기 위해 물범으로 변신했고, 헤임달이 승리를 증명했습니다. 그들 사이의 이 적대감은 라그나로크에서 마침내 서로를 파멸시킬 때 절정에 이를 것입니다.",
    match_message_en="Your features reflect the eternal vigilance of Heimdall. There is an alert, watchful quality to your gaze—eyes that miss nothing. Your face speaks of unwavering dedication and the strength that comes from standing guard.",
    match_message_ko="당신의 이목구비는 헤임달의 영원한 경계를 반영합니다. 당신의 눈빛에는 민첩하고 경계하는 품질이 있습니다—아무것도 놓치지 않는 눈. 당신의 얼굴은 흔들림 없는 헌신과 경비를 서는 것에서 오는 힘을 말해줍니다.",
    image_prompt="Noble Norse god with golden teeth and keen piercing eyes, wearing gleaming armor, standing on Bifröst rainbow bridge, holding the great horn Gjallarhorn, looking out over all nine realms, alert guardian stance, golden light",
    visual_description="Sharp alert features, piercing all-seeing eyes, golden coloring, expression of eternal watchfulness and duty",
    aliases=["Heimdallr", "Hallinskiði", "Gullintanni"],
    era="Viking Age",
    related_characters=["odin", "loki", "thor", "freya"]
)

SKADI_DESC = CharacterDescription(
    id="skadi",
    name_en="Skadi",
    name_ko="스카디",
    tagline_en="Goddess of Winter, Hunting, and Mountains",
    tagline_ko="겨울, 사냥, 산의 여신",
    description_en="""Skadi is the giant goddess of winter, skiing, bowhunting, and mountains. After the gods killed her father Thiazi, she came to Asgard armed for war, demanding compensation. The gods offered her a husband chosen by looking only at the candidates' feet.

Hoping to choose Baldur by his beautiful feet, Skadi instead selected Njörðr, god of the sea. Their marriage was unhappy—she could not bear the sounds of the sea, and he could not endure the wolves' howling in her mountain home. They eventually separated.

Skadi represents the harsh beauty of the northern wilderness—dangerous yet magnificent. She is one of the few giants accepted among the gods, her fierce independence and hunting prowess earning her respect. She embodies survival in the coldest places.""",
    description_ko="""스카디는 겨울, 스키, 활 사냥, 산의 거인 여신입니다. 신들이 그녀의 아버지 티아지를 죽인 후, 그녀는 보상을 요구하며 전쟁 무장을 하고 아스가르드에 왔습니다. 신들은 그녀에게 후보자들의 발만 보고 선택한 남편을 제안했습니다.

아름다운 발로 발드르를 선택하기를 바랐지만, 스카디는 대신 바다의 신 뇨르드를 선택했습니다. 그들의 결혼은 불행했습니다—그녀는 바다 소리를 견딜 수 없었고, 그는 그녀의 산 집에서 늑대 울음소리를 견딜 수 없었습니다. 결국 그들은 헤어졌습니다.

스카디는 북부 황야의 가혹한 아름다움을 대표합니다—위험하지만 장엄한. 그녀는 신들 사이에서 받아들여진 몇 안 되는 거인 중 하나로, 맹렬한 독립심과 사냥 실력이 존경을 얻었습니다. 그녀는 가장 추운 곳에서의 생존을 구현합니다.""",
    traits_en=["Fierce", "Independent", "Hardy", "Wild", "Avenging"],
    traits_ko=["맹렬한", "독립적인", "강인한", "야생의", "복수하는"],
    story_en="When choosing her husband, Skadi saw the most beautiful feet and thought they belonged to Baldur. They were actually Njörðr's, roughened by saltwater but fair. This twist of fate led to a mismatched marriage between mountain and sea.",
    story_ko="남편을 선택할 때, 스카디는 가장 아름다운 발을 보고 발드르의 것이라고 생각했습니다. 실제로는 바닷물에 거칠어졌지만 아름다운 뇨르드의 것이었습니다. 이 운명의 반전은 산과 바다의 어울리지 않는 결혼으로 이어졌습니다.",
    match_message_en="Your features carry the fierce independence of Skadi. There is a wild, untamed quality to your appearance—the look of one who thrives in harsh conditions others cannot endure. Your face speaks of strength forged in the cold.",
    match_message_ko="당신의 이목구비는 스카디의 맹렬한 독립성을 담고 있습니다. 당신의 외모에는 야생적이고 길들여지지 않은 품질이 있습니다—다른 사람들이 견딜 수 없는 가혹한 조건에서 번성하는 사람의 모습. 당신의 얼굴은 추위 속에서 단련된 힘을 말해줍니다.",
    image_prompt="Fierce Norse giantess in winter furs, carrying bow and arrows, snowshoes or skis, standing on snowy mountain peak, wolves nearby, cold wind blowing, beautiful but harsh features, independent warrior huntress",
    visual_description="Strong sharp features, cold piercing eyes, wild beauty adapted to harsh conditions, fierce independent expression",
    aliases=["Skaði", "Öndurdís"],
    era="Viking Age",
    related_characters=["njord", "freya", "freyr", "odin", "loki"]
)

FREYR_DESC = CharacterDescription(
    id="freyr",
    name_en="Freyr",
    name_ko="프레이르",
    tagline_en="God of Fertility, Prosperity, and Peace",
    tagline_ko="다산, 번영, 평화의 신",
    description_en="""Freyr is the god of fertility, prosperity, sunshine, and peace—the male counterpart to his twin sister Freya. He rules over the realm of Alfheim and is the most beloved of the Vanir gods among humans for the blessings he brings to harvests and herds.

He possesses several magical treasures: the ship Skíðblaðnir that can sail anywhere and fold to fit in a pocket, and the golden boar Gullinbursti that pulls his chariot and shines like the sun.

Freyr's greatest flaw was giving away his magical sword for love of the giantess Gerðr. At Ragnarök, he will face the fire giant Surtr weaponless—a reminder that even the gods cannot escape the consequences of their passions.""",
    description_ko="""프레이르는 다산, 번영, 햇빛, 평화의 신으로—쌍둥이 여동생 프레이야의 남성 상대입니다. 그는 알프헤임의 영역을 다스리며, 수확과 가축에 가져다주는 축복으로 인간들 사이에서 바니르 신들 중 가장 사랑받습니다.

그는 여러 마법 보물을 소유합니다: 어디든 항해할 수 있고 주머니에 들어갈 만큼 접을 수 있는 배 스키드블라드니르, 그리고 태양처럼 빛나며 전차를 끄는 황금 멧돼지 굴린부르스티.

프레이르의 가장 큰 결점은 거인 게르드에 대한 사랑으로 마법의 검을 포기한 것이었습니다. 라그나로크에서 그는 무기 없이 불의 거인 수르트르에 맞설 것입니다—신들조차도 열정의 결과를 피할 수 없다는 것을 상기시켜 줍니다.""",
    traits_en=["Generous", "Peaceful", "Fertile", "Passionate", "Sacrificing"],
    traits_ko=["관대한", "평화로운", "다산의", "열정적인", "희생하는"],
    story_en="Freyr fell so deeply in love with the giantess Gerðr that he gave away his magical sword—the one weapon that could fight on its own—just for the chance to marry her. This sacrifice means he will face Ragnarök unarmed.",
    story_ko="프레이르는 거인 게르드와 너무 깊이 사랑에 빠져 그녀와 결혼할 기회를 위해 마법의 검—스스로 싸울 수 있는 유일한 무기—을 포기했습니다. 이 희생은 그가 라그나로크를 무장하지 않은 채로 맞이할 것을 의미합니다.",
    match_message_en="Your features reflect the generous warmth of Freyr. There is a life-giving quality to your appearance—the look of one who brings growth and prosperity wherever they go. Your face speaks of peace and the abundance of summer.",
    match_message_ko="당신의 이목구비는 프레이르의 관대한 온기를 반영합니다. 당신의 외모에는 생명을 주는 품질이 있습니다—가는 곳마다 성장과 번영을 가져다주는 사람의 모습. 당신의 얼굴은 평화와 여름의 풍요를 말해줍니다.",
    image_prompt="Handsome Norse god with golden hair, surrounded by wheat and abundance, riding golden boar Gullinbursti, peaceful expression, summer sunlight, wearing fine clothes of gold and green, symbols of fertility around him",
    visual_description="Handsome warm features, bright eyes full of life, golden coloring, expression of peaceful abundance and generosity",
    aliases=["Frey", "Yngvi", "Yngvi-Freyr"],
    era="Viking Age",
    related_characters=["freya", "njord", "gerdr", "odin", "skadi"]
)

NJORD_DESC = CharacterDescription(
    id="njord",
    name_en="Njörðr",
    name_ko="뇨르드",
    tagline_en="God of the Sea, Wealth, and Seafaring",
    tagline_ko="바다, 부, 항해의 신",
    description_en="""Njörðr is the Vanir god of the sea, wind, fishing, and wealth. Father of Freyr and Freya, he was sent to live among the Aesir as a hostage after the war between the two divine tribes, where he earned great respect for his wisdom and generosity.

Sailors pray to Njörðr for good winds and safe passage, and fishermen for bountiful catches. His hall Nóatún sits by the sea, and he is associated with the wealth that comes from maritime trade.

His ill-fated marriage to the mountain goddess Skadi taught that some differences cannot be reconciled—she could not live by the noisy sea, he could not bear the howling mountains. Yet both respected each other despite their incompatibility.""",
    description_ko="""뇨르드는 바다, 바람, 어업, 부의 바니르 신입니다. 프레이르와 프레이야의 아버지로, 두 신성한 부족 사이의 전쟁 후 인질로 아시르 사이에 살게 되었고, 지혜와 관대함으로 큰 존경을 얻었습니다.

선원들은 좋은 바람과 안전한 항해를 위해 뇨르드에게 기도하고, 어부들은 풍성한 어획을 위해 기도합니다. 그의 전당 노아툰은 바닷가에 있으며, 그는 해상 무역에서 오는 부와 연관됩니다.

산의 여신 스카디와의 불운한 결혼은 일부 차이점은 조정될 수 없다는 것을 가르쳐 주었습니다—그녀는 시끄러운 바닷가에서 살 수 없었고, 그는 울부짖는 산을 견딜 수 없었습니다. 그러나 둘 다 서로의 양립 불가능에도 불구하고 서로를 존경했습니다.""",
    traits_en=["Generous", "Wealthy", "Peaceful", "Sea-loving", "Wise"],
    traits_ko=["관대한", "부유한", "평화로운", "바다를 사랑하는", "지혜로운"],
    story_en="Njörðr and Skadi tried to compromise—nine nights in the mountains, nine nights by the sea. But neither could adjust: the seagulls kept Skadi awake, while the wolves' howling drove Njörðr to despair. They parted amicably.",
    story_ko="뇨르드와 스카디는 타협하려 했습니다—산에서 아홉 밤, 바닷가에서 아홉 밤. 그러나 둘 다 적응할 수 없었습니다: 갈매기 소리가 스카디를 깨웠고, 늑대 울음소리가 뇨르드를 절망에 빠뜨렸습니다. 그들은 우호적으로 헤어졌습니다.",
    match_message_en="Your features reflect the calm abundance of Njörðr. There is a maritime quality to your presence—vast, generous, and wealth-bringing. Your face speaks of one who finds peace near water and prosperity through patience.",
    match_message_ko="당신의 이목구비는 뇨르드의 평온한 풍요를 반영합니다. 당신의 존재에는 해양적 품질이 있습니다—광대하고, 관대하고, 부를 가져다주는. 당신의 얼굴은 물 근처에서 평화를 찾고 인내를 통해 번영하는 사람을 말해줍니다.",
    image_prompt="Noble Vanir god with sea-green eyes and grey-blue hair like waves, standing by the shore with ships in background, wealthy clothing, fishing nets and treasures from the sea, calm peaceful expression, ocean sunset",
    visual_description="Mature dignified features, calm sea-colored eyes, weathered but handsome, expression of peaceful wealth and maritime wisdom",
    aliases=["Njord", "Njörðr"],
    era="Viking Age",
    related_characters=["freya", "freyr", "skadi", "odin"]
)


# Master dictionary of all descriptions
DESCRIPTIONS_DATABASE: dict[str, CharacterDescription] = {
    # Greek (12 characters)
    "zeus": ZEUS_DESC,
    "hera": HERA_DESC,
    "athena": ATHENA_DESC,
    "apollo": APOLLO_DESC,
    "artemis": ARTEMIS_DESC,
    "ares": ARES_DESC,
    "aphrodite": APHRODITE_DESC,
    "poseidon": POSEIDON_DESC,
    "hades": HADES_DESC,
    "hermes": HERMES_DESC,
    "dionysus": DIONYSUS_DESC,
    "persephone": PERSEPHONE_DESC,

    # Norse (12 characters)
    "odin": ODIN_DESC,
    "thor": THOR_DESC,
    "freya": FREYA_DESC,
    "loki": LOKI_DESC,
    "frigg": FRIGG_DESC,
    "baldur": BALDUR_DESC,
    "tyr": TYR_DESC,
    "hel": HEL_DESC,
    "heimdall": HEIMDALL_DESC,
    "skadi": SKADI_DESC,
    "freyr": FREYR_DESC,
    "njord": NJORD_DESC,

    # Korean
    "admiral_yi": ADMIRAL_YI_DESC,
    "sejong_the_great": SEJONG_DESC,
    "gumiho": GUMIHO_DESC,

    # Chinese
    "confucius": CONFUCIUS_DESC,
    "guan_yu": GUAN_YU_DESC,

    # Egyptian (9 characters)
    "ra": RA_DESC,
    "isis": ISIS_DESC,
    "osiris": OSIRIS_DESC,
    "anubis": ANUBIS_DESC,
    "horus": HORUS_DESC,
    "bastet": BASTET_DESC,
    "sekhmet": SEKHMET_DESC,
    "thoth": THOTH_DESC,
    "set": SET_DESC,
}


def get_description(god_id: str) -> CharacterDescription | None:
    """Get description for a character by ID."""
    return DESCRIPTIONS_DATABASE.get(god_id)


def get_all_descriptions() -> list[CharacterDescription]:
    """Get all character descriptions."""
    return list(DESCRIPTIONS_DATABASE.values())
