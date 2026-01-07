"""
Norse Mythology - Additional Character Descriptions
Extends the base descriptions.py with more Norse figures to reach 20+
"""
from .descriptions import CharacterDescription


# Additional Norse Mythology Figures (to reach 20+)

VIDAR_DESC = CharacterDescription(
    id="vidar",
    name_en="Vidar",
    name_ko="비다르",
    tagline_en="God of Vengeance and Silence",
    tagline_ko="복수와 침묵의 신",
    description_en="""Vidar is the silent god, one of the strongest of all the Aesir, second only to Thor in might. He is destined to play a crucial role in Ragnarök, where he will avenge his father Odin by slaying the wolf Fenrir.

Known for his thick leather shoe, made from all the scraps of leather ever discarded by shoemakers, Vidar will use this magical footwear to hold open Fenrir's jaws while he delivers the killing blow.

As the god of silence, Vidar represents patient strength and the power of quiet determination. He speaks little but acts decisively when the time comes.""",
    description_ko="""비다르는 침묵의 신으로, 모든 아스신 중 가장 강한 신 중 하나이며, 힘으로는 토르에게만 뒤집니다. 그는 라그나로크에서 결정적인 역할을 할 운명으로, 늑대 펜리르를 죽여 아버지 오딘의 복수를 합니다.

구두장이들이 버린 모든 가죽 조각으로 만든 두꺼운 가죽 신발로 유명한 비다르는, 이 마법의 신발로 펜리르의 턱을 벌리고 치명타를 날립니다.

침묵의 신으로서 비다르는 인내하는 힘과 조용한 결단력의 힘을 대표합니다. 그는 말을 적게 하지만 때가 오면 단호하게 행동합니다.""",
    traits_en=["Silent", "Strong", "Patient", "Vengeful", "Determined"],
    traits_ko=["침묵하는", "강한", "인내하는", "복수심 있는", "결단력 있는"],
    story_en="At Ragnarök, Vidar will witness his father Odin being swallowed by Fenrir. Without hesitation, he will plant his legendary shoe on the wolf's lower jaw, grasp the upper jaw with his hands, and tear the beast apart, avenging the Allfather.",
    story_ko="라그나로크에서 비다르는 아버지 오딘이 펜리르에게 삼켜지는 것을 목격합니다. 주저 없이 그는 전설적인 신발을 늑대의 아래턱에 딛고, 손으로 위턱을 잡아, 짐승을 찢어 만물의 아버지의 복수를 합니다.",
    match_message_en="Your features carry the quiet strength of Vidar. There is a powerful stillness to your appearance—the look of one who waits patiently but acts with devastating force when needed.",
    match_message_ko="당신의 이목구비는 비다르의 조용한 힘을 담고 있습니다. 당신의 외모에는 강력한 고요함이 있습니다—인내심 있게 기다리지만 필요할 때 파괴적인 힘으로 행동하는 사람의 모습.",
    image_prompt="Powerful Norse god in leather armor with massive magical leather boot, standing silently in snowy forest, awaiting destiny, intense quiet determination in eyes, Norse runes glowing, twilight atmosphere",
    visual_description="Strong silent features, deep thoughtful eyes, powerful jaw, expression of patient determination and hidden strength",
    aliases=["Vidarr", "The Silent One"],
    era="Norse Mythology",
    related_characters=["odin", "fenrir", "thor", "vali"]
)

VALI_DESC = CharacterDescription(
    id="vali",
    name_en="Vali",
    name_ko="발리",
    tagline_en="God of Vengeance, Avenger of Baldur",
    tagline_ko="복수의 신, 발두르의 복수자",
    description_en="""Vali is the son of Odin, born specifically to avenge the death of Baldur. He grew to full adulthood in a single day, never washing his hands or combing his hair until he had slain Höðr, the blind god who killed Baldur.

His birth and rapid growth demonstrate the power of divine vengeance—purpose given form. Vali is one of the few gods destined to survive Ragnarök and help rebuild the world.

Vali represents righteous vengeance and the fulfillment of duty, no matter how painful the cost.""",
    description_ko="""발리는 오딘의 아들로, 발두르의 죽음을 복수하기 위해 특별히 태어났습니다. 그는 하루 만에 완전한 성인으로 자랐고, 발두르를 죽인 맹인 신 호드르를 죽일 때까지 손을 씻거나 머리를 빗지 않았습니다.

그의 탄생과 급속한 성장은 신성한 복수의 힘을 보여줍니다—목적이 형태를 갖춘 것입니다. 발리는 라그나로크에서 살아남아 세계 재건을 도울 운명인 몇 안 되는 신 중 하나입니다.

발리는 정당한 복수와 아무리 고통스러운 대가를 치르더라도 의무를 완수하는 것을 대표합니다.""",
    traits_en=["Vengeful", "Determined", "Rapid", "Purposeful", "Surviving"],
    traits_ko=["복수하는", "결단력 있는", "신속한", "목적 있는", "생존하는"],
    story_en="Born to avenge Baldur, Vali grew from infant to warrior in one day. He hunted down Höðr and slew him, fulfilling the prophecy. Vali is destined to survive Ragnarök and inherit the new world alongside his brother Vidar.",
    story_ko="발두르를 복수하기 위해 태어난 발리는 하루 만에 유아에서 전사로 자랐습니다. 그는 호드르를 추적하여 죽이고 예언을 이행했습니다. 발리는 라그나로크에서 살아남아 형제 비다르와 함께 새 세계를 물려받을 운명입니다.",
    match_message_en="Your features carry the focused determination of Vali. There is purpose in your appearance—the look of one born for a specific destiny and determined to fulfill it.",
    match_message_ko="당신의 이목구비는 발리의 집중된 결단력을 담고 있습니다. 당신의 외모에는 목적이 있습니다—특정 운명을 위해 태어나 그것을 이행하려는 결의를 가진 사람의 모습.",
    image_prompt="Young but fierce Norse warrior god with wild unkempt hair, bow and arrows, intense vengeful expression, standing over fallen enemy, Nordic winter landscape, divine golden aura",
    visual_description="Youthful but fierce features, intense focused eyes, wild determined expression, appearance of someone born with purpose",
    aliases=["Ali", "The Avenger"],
    era="Norse Mythology",
    related_characters=["odin", "baldur", "hodr", "vidar"]
)

BRAGI_DESC = CharacterDescription(
    id="bragi",
    name_en="Bragi",
    name_ko="브라기",
    tagline_en="God of Poetry and Eloquence",
    tagline_ko="시와 웅변의 신",
    description_en="""Bragi is the god of poetry, eloquence, and the spoken word. His tongue is said to have runes carved upon it, and his words flow like the finest mead. He welcomes fallen warriors to Valhalla with magnificent verses celebrating their heroic deeds.

Married to Idunn, keeper of the apples of immortality, Bragi represents the immortalizing power of poetry—how words can preserve heroic deeds forever. He is the patron of skalds, the Norse poets who kept history alive through verse.

His long beard and wise appearance embody the dignity of the learned, and his hall in Asgard rings with eternal song.""",
    description_ko="""브라기는 시, 웅변, 말의 신입니다. 그의 혀에는 룬이 새겨져 있다고 하며, 그의 말은 최상의 미드처럼 흐릅니다. 그는 전사한 영웅들을 그들의 영웅적 행위를 찬양하는 웅장한 시구로 발할라에 환영합니다.

불멸의 사과를 지키는 이둔과 결혼한 브라기는 시의 불멸화하는 힘을 대표합니다—말이 어떻게 영웅적 행위를 영원히 보존할 수 있는지. 그는 시를 통해 역사를 살아 있게 유지한 노르드 시인들인 스칼드들의 수호신입니다.

그의 긴 수염과 현명한 외모는 학자의 품위를 구현하며, 아스가르드에 있는 그의 전당은 영원한 노래로 울려 퍼집니다.""",
    traits_en=["Eloquent", "Wise", "Welcoming", "Artistic", "Dignified"],
    traits_ko=["웅변적인", "현명한", "환영하는", "예술적인", "품위 있는"],
    story_en="When Loki insulted all the gods at Aegir's feast, Bragi was the first to respond, warning Loki to leave. Loki called Bragi a coward, but Bragi calmly replied that if they were outside the hall, he would carry Loki's head as payment for his lies.",
    story_ko="로키가 에기르의 연회에서 모든 신들을 모욕했을 때, 브라기는 가장 먼저 대응하며 로키에게 떠나라고 경고했습니다. 로키는 브라기를 겁쟁이라고 불렀지만, 브라기는 침착하게 그들이 전당 밖에 있었다면 그의 거짓말에 대한 대가로 로키의 머리를 들고 갔을 것이라고 대답했습니다.",
    match_message_en="Your features carry the eloquent wisdom of Bragi. There is poetry in your appearance—the look of one who can capture truth in beautiful words and move hearts with speech.",
    match_message_ko="당신의 이목구비는 브라기의 웅변적인 지혜를 담고 있습니다. 당신의 외모에는 시가 있습니다—진실을 아름다운 말로 포착하고 말로 마음을 움직일 수 있는 사람의 모습.",
    image_prompt="Wise Norse god with long flowing beard, holding golden harp, runes glowing on tongue, seated in grand mead hall, surrounded by listening warriors, warm firelight, dignified artistic expression",
    visual_description="Wise gentle features, kind knowing eyes, long dignified beard, expression of one who speaks eternal truths",
    aliases=["The Long-Bearded One", "God of Skalds"],
    era="Norse Mythology",
    related_characters=["idunn", "odin", "loki", "thor"]
)

IDUNN_DESC = CharacterDescription(
    id="idunn",
    name_en="Idunn",
    name_ko="이둔",
    tagline_en="Goddess of Youth and Immortality",
    tagline_ko="젊음과 불멸의 여신",
    description_en="""Idunn is the keeper of the golden apples that grant the gods their immortality and eternal youth. Without her apples, the Aesir would age and wither like mortals—her role makes her one of the most crucial figures in Asgard.

Wife of Bragi, the god of poetry, Idunn embodies the preservation of life and vitality. Her orchard is the source of divine rejuvenation, and she carefully tends to each precious apple.

She represents the preciousness of youth and the vital forces that sustain life, as well as the vulnerability that comes from being so essential to others.""",
    description_ko="""이둔은 신들에게 불멸과 영원한 젊음을 부여하는 황금 사과의 수호자입니다. 그녀의 사과 없이는 아스신들도 필멸자처럼 늙고 시들 것입니다—그녀의 역할은 그녀를 아스가르드에서 가장 중요한 인물 중 하나로 만듭니다.

시의 신 브라기의 아내인 이둔은 생명과 활력의 보존을 구현합니다. 그녀의 과수원은 신성한 회춘의 원천이며, 그녀는 각각의 소중한 사과를 세심하게 돌봅니다.

그녀는 젊음의 소중함과 생명을 유지하는 핵심적인 힘을 대표하며, 다른 이들에게 너무 필수적인 존재가 됨으로써 오는 취약성도 대표합니다.""",
    traits_en=["Youthful", "Nurturing", "Essential", "Gentle", "Life-giving"],
    traits_ko=["젊은", "양육하는", "필수적인", "온화한", "생명을 주는"],
    story_en="The giant Thjazi kidnapped Idunn and her apples with Loki's unwitting help. Without her, the gods began to age rapidly. Loki was forced to rescue her by borrowing Freya's falcon cloak and transforming Idunn into a nut to carry her home, saving the gods from mortality.",
    story_ko="거인 티아치는 로키의 부주의한 도움으로 이둔과 그녀의 사과를 납치했습니다. 그녀 없이 신들은 급속히 늙기 시작했습니다. 로키는 프레야의 매 망토를 빌려 이둔을 견과류로 변신시켜 집으로 데려와 신들을 죽음에서 구해야 했습니다.",
    match_message_en="Your features carry the eternal youth of Idunn. There is a life-giving freshness to your appearance—the look of one who brings vitality and renewal wherever they go.",
    match_message_ko="당신의 이목구비는 이둔의 영원한 젊음을 담고 있습니다. 당신의 외모에는 생명을 주는 신선함이 있습니다—가는 곳마다 활력과 재생을 가져다주는 사람의 모습.",
    image_prompt="Beautiful Norse goddess with golden hair, holding basket of glowing golden apples, standing in magical orchard, eternal spring blooming around her, youthful radiant expression, soft divine light",
    visual_description="Youthful radiant features, bright clear eyes, fresh complexion, expression of eternal spring and life-giving energy",
    aliases=["Idun", "The Rejuvenating One"],
    era="Norse Mythology",
    related_characters=["bragi", "loki", "thjazi", "freya"]
)

FORSETI_DESC = CharacterDescription(
    id="forseti",
    name_en="Forseti",
    name_ko="포르세티",
    tagline_en="God of Justice and Reconciliation",
    tagline_ko="정의와 화해의 신",
    description_en="""Forseti is the god of justice, peace, and truth in Norse mythology. Son of Baldur and Nanna, he presides over disputes in his shining hall Glitnir, where gold pillars support a silver roof.

All who come to his hall with disputes leave reconciled—no case is too difficult for his wisdom. He represents the ideal of law as a means of creating peace rather than punishment, focusing on reconciliation rather than retribution.

Forseti embodies the belief that truth and fairness can resolve even the bitterest conflicts, and that justice serves the community by restoring harmony.""",
    description_ko="""포르세티는 노르드 신화에서 정의, 평화, 진실의 신입니다. 발두르와 난나의 아들로, 그는 금 기둥이 은 지붕을 받치는 빛나는 전당 글리트니르에서 분쟁을 주재합니다.

분쟁을 가지고 그의 전당에 오는 모든 이들은 화해하고 떠납니다—그의 지혜로 해결할 수 없는 사건은 없습니다. 그는 법을 처벌의 수단이 아닌 평화를 만드는 수단으로, 보복보다는 화해에 초점을 맞추는 이상을 대표합니다.

포르세티는 진실과 공정함이 가장 쓰라린 갈등도 해결할 수 있으며, 정의는 조화를 회복함으로써 공동체에 봉사한다는 믿음을 구현합니다.""",
    traits_en=["Just", "Peaceful", "Wise", "Reconciling", "Truthful"],
    traits_ko=["공정한", "평화로운", "현명한", "화해시키는", "진실한"],
    story_en="When the Frisians could not agree on their laws, Forseti appeared in their ship and taught them a code of justice. He struck a spring from the ground with his axe, and from then on they gathered at that spot to settle all disputes by his principles.",
    story_ko="프리지아인들이 그들의 법에 동의할 수 없었을 때, 포르세티가 그들의 배에 나타나 정의의 법전을 가르쳤습니다. 그는 도끼로 땅에서 샘을 쳤고, 그때부터 그들은 그의 원칙에 따라 모든 분쟁을 해결하기 위해 그 장소에 모였습니다.",
    match_message_en="Your features carry the balanced wisdom of Forseti. There is a natural fairness to your appearance—the look of one who can see all sides of a dispute and find the path to peace.",
    match_message_ko="당신의 이목구비는 포르세티의 균형 잡힌 지혜를 담고 있습니다. 당신의 외모에는 자연스러운 공정함이 있습니다—분쟁의 모든 면을 볼 수 있고 평화로 가는 길을 찾을 수 있는 사람의 모습.",
    image_prompt="Noble Norse god seated on golden throne in silver-roofed hall, holding scales and axe of justice, calm wise expression, parties in dispute before him, golden light streaming through columns",
    visual_description="Balanced noble features, clear truthful eyes, calm expression, appearance of perfect impartiality and wisdom",
    aliases=["The Presiding One", "God of Law"],
    era="Norse Mythology",
    related_characters=["baldur", "nanna", "odin", "tyr"]
)

MIMIR_DESC = CharacterDescription(
    id="mimir",
    name_en="Mimir",
    name_ko="미미르",
    tagline_en="Guardian of the Well of Wisdom",
    tagline_ko="지혜의 샘의 수호자",
    description_en="""Mimir is the wisest of all beings, guardian of the well of wisdom that lies beneath one of the roots of Yggdrasil. His knowledge encompasses all things that were, are, and will be, making him an invaluable counselor.

Odin sacrificed his eye to drink from Mimir's well and gain its wisdom. Even after Mimir was beheaded by the Vanir, Odin preserved his head with herbs and runes so that Mimir could continue to provide counsel.

Mimir represents the price of wisdom—that true knowledge often comes at great cost, and that the wise continue to teach even beyond death.""",
    description_ko="""미미르는 모든 존재 중 가장 현명하며, 위그드라실의 뿌리 중 하나 아래에 있는 지혜의 샘의 수호자입니다. 그의 지식은 과거, 현재, 미래의 모든 것을 포괄하여 그를 귀중한 조언자로 만듭니다.

오딘은 미미르의 샘에서 마시고 그 지혜를 얻기 위해 자신의 눈을 희생했습니다. 미미르가 바니르에게 참수당한 후에도, 오딘은 허브와 룬으로 그의 머리를 보존하여 미미르가 계속 조언을 제공할 수 있게 했습니다.

미미르는 지혜의 대가를 대표합니다—진정한 지식은 종종 큰 대가를 치르며, 현자는 죽음을 넘어서도 계속 가르친다는 것을.""",
    traits_en=["Wise", "Ancient", "Counseling", "Sacrificed", "Eternal"],
    traits_ko=["현명한", "고대의", "조언하는", "희생된", "영원한"],
    story_en="When the Vanir felt cheated in a hostage exchange, they beheaded Mimir and sent his head to Odin. But Odin would not lose such wisdom—he embalmed the head, sang charms over it, and gave it the power to speak. To this day, Mimir's head counsels the Allfather.",
    story_ko="바니르가 인질 교환에서 속았다고 느꼈을 때, 그들은 미미르를 참수하고 그의 머리를 오딘에게 보냈습니다. 하지만 오딘은 그런 지혜를 잃지 않을 것이었습니다—그는 머리를 방부 처리하고, 그 위에 주문을 불렀으며, 말할 수 있는 힘을 주었습니다. 오늘날까지 미미르의 머리는 만물의 아버지에게 조언합니다.",
    match_message_en="Your features carry the deep wisdom of Mimir. There is ancient knowledge in your gaze—the look of one who has seen much and understands the true cost of wisdom.",
    match_message_ko="당신의 이목구비는 미미르의 깊은 지혜를 담고 있습니다. 당신의 눈빛에는 고대의 지식이 있습니다—많은 것을 보고 지혜의 진정한 대가를 이해하는 사람의 모습.",
    image_prompt="Ancient wise head preserved in sacred well, surrounded by glowing runes, eyes full of infinite knowledge, Yggdrasil roots visible, mystical blue-green light, expression of timeless wisdom",
    visual_description="Ancient weathered features, infinitely deep knowing eyes, expression of accumulated wisdom beyond mortal understanding",
    aliases=["The Wise One", "The Rememberer"],
    era="Norse Mythology",
    related_characters=["odin", "yggdrasil", "vanir"]
)

NORNS_DESC = CharacterDescription(
    id="norns",
    name_en="The Norns",
    name_ko="노른",
    tagline_en="Weavers of Fate and Destiny",
    tagline_ko="운명의 직조자들",
    description_en="""The Norns are the three powerful beings who control the destiny of all living things. Urd (the past), Verdandi (the present), and Skuld (the future) sit at the Well of Fate beneath Yggdrasil, weaving the threads of all lives.

Not even the gods can escape the fate the Norns decree. They water the World Tree daily and carve the destinies of gods and mortals into its bark. Their power predates the gods themselves.

They represent the inescapable nature of fate, the connection between past, present, and future, and the fundamental truth that all things have their appointed time.""",
    description_ko="""노른은 모든 생명체의 운명을 통제하는 세 명의 강력한 존재입니다. 우르드(과거), 베르단디(현재), 스쿨드(미래)는 위그드라실 아래 운명의 샘에 앉아 모든 생명의 실을 짭니다.

신들조차도 노른이 정한 운명을 피할 수 없습니다. 그들은 매일 세계수에 물을 주고 신과 인간의 운명을 그 껍질에 새깁니다. 그들의 힘은 신들 자체보다 앞섭니다.

그들은 운명의 피할 수 없는 성질, 과거, 현재, 미래 사이의 연결, 그리고 모든 것에는 정해진 때가 있다는 근본적인 진실을 대표합니다.""",
    traits_en=["Fated", "Powerful", "Ancient", "Weaving", "Inescapable"],
    traits_ko=["운명적인", "강력한", "고대의", "직조하는", "피할 수 없는"],
    story_en="When a child is born, the Norns arrive to decree its fate. They spin the thread of life, measure it, and cut it when the time comes. Even Odin, who gained wisdom from Mimir's well, cannot change what the Norns have woven.",
    story_ko="아이가 태어나면 노른이 도착하여 그 운명을 정합니다. 그들은 생명의 실을 짜고, 측정하며, 때가 되면 자릅니다. 미미르의 샘에서 지혜를 얻은 오딘조차도 노른이 짠 것을 바꿀 수 없습니다.",
    match_message_en="Your features carry the timeless mystery of the Norns. There is a sense of fate about your appearance—the look of one connected to the deeper patterns that shape all existence.",
    match_message_ko="당신의 이목구비는 노른의 시간을 초월한 신비를 담고 있습니다. 당신의 외모에는 운명의 감각이 있습니다—모든 존재를 형성하는 더 깊은 패턴에 연결된 사람의 모습.",
    image_prompt="Three mystical women in flowing robes at sacred well, one old one young one ageless, weaving glowing threads of fate, Yggdrasil towering above, runes floating in air, ethereal starlight",
    visual_description="Ageless otherworldly features, eyes that see all time at once, expression of those who know all fates yet feel compassion",
    aliases=["The Fates", "The Weird Sisters"],
    era="Norse Mythology",
    related_characters=["odin", "yggdrasil", "mimir"]
)

JORMUNGANDR_DESC = CharacterDescription(
    id="jormungandr",
    name_en="Jörmungandr",
    name_ko="요르문간드",
    tagline_en="The World Serpent, Encircler of Midgard",
    tagline_ko="세계의 뱀, 미드가르드를 둘러싼 자",
    description_en="""Jörmungandr is the colossal World Serpent, child of Loki and the giantess Angrboda. Odin cast the serpent into the ocean surrounding Midgard, where it grew so large that it encircles the entire world, grasping its own tail.

Thor and Jörmungandr are fated enemies—they have encountered each other twice, and at Ragnarök they will meet for the final time. Their battle will end with both their deaths.

The World Serpent represents the chaos that surrounds order, the vastness of the unknown, and the apocalyptic forces that will one day be unleashed.""",
    description_ko="""요르문간드는 거대한 세계의 뱀으로, 로키와 거인 앙그르보다의 자식입니다. 오딘은 이 뱀을 미드가르드를 둘러싼 바다에 던졌고, 그곳에서 그것은 자신의 꼬리를 물고 전 세계를 둘러쌀 정도로 커졌습니다.

토르와 요르문간드는 운명적인 적입니다—그들은 두 번 만났고, 라그나로크에서 마지막으로 만날 것입니다. 그들의 전투는 둘 다의 죽음으로 끝날 것입니다.

세계의 뱀은 질서를 둘러싼 혼돈, 미지의 광대함, 그리고 언젠가 풀려날 종말론적 힘을 대표합니다.""",
    traits_en=["Vast", "Chaotic", "Apocalyptic", "Encircling", "Destined"],
    traits_ko=["광대한", "혼돈의", "종말론적인", "둘러싸는", "운명적인"],
    story_en="Thor once went fishing with the giant Hymir and used an ox head as bait. When Jörmungandr bit, Thor began hauling the World Serpent from the depths. They locked eyes, venom dripped—but Hymir cut the line in terror, and the serpent sank back, their final battle postponed.",
    story_ko="토르는 한때 거인 히미르와 낚시를 갔고 소 머리를 미끼로 사용했습니다. 요르문간드가 물었을 때, 토르는 세계의 뱀을 깊은 곳에서 끌어올리기 시작했습니다. 그들은 눈을 마주쳤고, 독이 떨어졌습니다—하지만 히미르가 공포에 질려 줄을 끊었고, 뱀은 다시 가라앉아 그들의 최종 전투는 연기되었습니다.",
    match_message_en="Your features carry the vast presence of Jörmungandr. There is something encompassing about your appearance—the look of one whose influence extends beyond what others can see.",
    match_message_ko="당신의 이목구비는 요르문간드의 광대한 존재감을 담고 있습니다. 당신의 외모에는 포괄적인 무언가가 있습니다—영향력이 다른 이들이 볼 수 있는 것 너머로 확장되는 사람의 모습.",
    image_prompt="Colossal sea serpent encircling the world, scales glittering like ocean waves, emerging from stormy seas, lightning reflected in serpentine eyes, apocalyptic grandeur, Norse mythological style",
    visual_description="Powerful ancient features, deep unfathomable eyes, presence that suggests vast hidden depths and primal power",
    aliases=["The Midgard Serpent", "The World Snake"],
    era="Norse Mythology",
    related_characters=["thor", "loki", "fenrir", "hel", "angrboda"]
)


# Dictionary of additional Norse descriptions
NORSE_ADDITIONAL_DESCRIPTIONS = {
    "vidar": VIDAR_DESC,
    "vali": VALI_DESC,
    "bragi": BRAGI_DESC,
    "idunn": IDUNN_DESC,
    "forseti": FORSETI_DESC,
    "mimir": MIMIR_DESC,
    "norns": NORNS_DESC,
    "jormungandr": JORMUNGANDR_DESC,
}
