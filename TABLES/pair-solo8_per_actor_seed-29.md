# Per-actor measures — Batch 7

**Readings:** wide = source.N + source_input + input.N (A3/A4); narrow = source.N + source_input only (Batch 7). Shared columns, including kept, are identical under both readings. New zero bins show where only the other reading has observations.

Use IDs uN are zero-based occurrences in Batch 3's unchanged record sequence,
scoped to the History column. The use trace below links each to its committed
transaction, exact operation revision, and block completion boundary. Empty
ID lists mean zero observed uses, not missing histories. Inactive means zero
completed paid uses; such actors remain in population denominators.

**Batch 7 conditioning index:** received uses at dim <= 2 divided by ALL
uses at dim <= 2, per actor. The numerator IDs are listed; denominator IDs
are every row for that actor with Dim <= 2 in the use trace below.
Hold is kept received / received, across all seats. N/A denotes a zero denominator.
World and self are not received; they contribute to the weak-use denominator,
use profile/trace and all-use DCNH. No zero-denominator ratio is presented as zero.

## Actor indices

| History | Actor | TIM | Status | Conditioning wide | Hold wide | Conditioning numerator IDs wide | Received IDs wide | Kept received IDs wide | Conditioning narrow | Hold narrow | Conditioning numerator IDs narrow | Received IDs narrow | Kept received IDs narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-solo8-seed-29 | workshop:alice | iee | active | 134/196 = 67/98 | 162/164 = 81/82 | u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u68, u69, u70, u71, u72, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u135, u136, u137, u138, u139, u140, u141, u142, u181, u182, u183, u184, u185, u186, u187, u188, u189, u205, u208, u209, u210, u211, u212, u213, u214, u215, u216, u230, u234, u235, u236, u237, u238, u239, u240, u241, u256, u260, u261, u262, u263, u264, u265, u266, u267, u268, u283, u288, u289, u290, u291, u292, u293, u294, u295, u303, u304, u309, u310, u311, u312, u313, u314, u315, u316, u317, u318, u319, u320, u328, u329, u337, u338, u342, u343, u344, u345, u346, u347, u348, u349, u357, u358, u363, u364, u365, u366, u367, u368, u369, u370, u371, u372, u380, u381, u387, u388 | u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u68, u69, u70, u71, u72, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u135, u136, u137, u138, u139, u140, u141, u142, u180, u181, u182, u183, u184, u185, u186, u187, u188, u189, u199, u200, u205, u206, u207, u208, u209, u210, u211, u212, u213, u214, u215, u216, u224, u225, u230, u231, u232, u233, u234, u235, u236, u237, u238, u239, u240, u241, u249, u250, u255, u256, u257, u258, u259, u260, u261, u262, u263, u264, u265, u266, u267, u268, u276, u277, u282, u283, u284, u285, u286, u287, u288, u289, u290, u291, u292, u293, u294, u295, u303, u304, u309, u310, u311, u312, u313, u314, u315, u316, u317, u318, u319, u320, u328, u329, u334, u335, u336, u337, u338, u339, u340, u341, u342, u343, u344, u345, u346, u347, u348, u349, u357, u358, u363, u364, u365, u366, u367, u368, u369, u370, u371, u372, u380, u381, u386, u387, u388 | u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u68, u69, u70, u71, u72, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u135, u136, u137, u138, u139, u140, u141, u142, u180, u181, u182, u183, u184, u185, u186, u187, u188, u189, u199, u200, u205, u206, u207, u208, u209, u210, u211, u212, u213, u214, u215, u216, u224, u225, u230, u231, u232, u233, u234, u235, u236, u237, u238, u239, u240, u241, u249, u250, u255, u256, u257, u258, u259, u260, u261, u262, u263, u264, u265, u266, u267, u268, u276, u282, u283, u284, u285, u286, u287, u288, u289, u290, u291, u292, u293, u294, u295, u303, u304, u309, u310, u311, u312, u313, u314, u315, u316, u317, u318, u319, u320, u328, u329, u334, u335, u336, u337, u338, u339, u340, u341, u342, u343, u344, u345, u346, u347, u348, u349, u357, u358, u363, u364, u365, u366, u367, u368, u369, u370, u371, u372, u380, u386, u387, u388 | 12/196 = 3/49 | 28/28 = 1 | u205, u230, u256, u283, u309, u310, u311, u337, u338, u363, u387, u388 | u205, u206, u207, u230, u231, u232, u255, u256, u257, u258, u259, u282, u283, u284, u285, u286, u309, u310, u311, u334, u335, u336, u337, u338, u363, u386, u387, u388 | u205, u206, u207, u230, u231, u232, u255, u256, u257, u258, u259, u282, u283, u284, u285, u286, u309, u310, u311, u334, u335, u336, u337, u338, u363, u386, u387, u388 |
| pair-solo8-seed-29 | workshop:bob | sli | active | 45/45 = 1 | 138/142 = 69/71 | u47, u52, u73, u78, u100, u105, u109, u114, u118, u123, u127, u132, u191, u196, u202, u203, u204, u221, u227, u228, u229, u246, u252, u253, u254, u273, u279, u280, u281, u300, u306, u307, u308, u325, u331, u332, u333, u354, u360, u361, u362, u377, u383, u384, u385 | u46, u47, u48, u49, u50, u51, u52, u53, u54, u73, u74, u75, u76, u77, u78, u79, u80, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u190, u191, u192, u193, u194, u195, u196, u197, u198, u201, u202, u203, u204, u217, u218, u219, u220, u221, u222, u223, u226, u227, u228, u229, u242, u243, u244, u245, u246, u247, u248, u251, u252, u253, u254, u269, u270, u271, u272, u273, u274, u275, u278, u279, u280, u281, u296, u297, u298, u299, u300, u301, u302, u305, u306, u307, u308, u321, u322, u323, u324, u325, u326, u327, u330, u331, u332, u333, u350, u351, u352, u353, u354, u355, u356, u359, u360, u361, u362, u373, u374, u375, u376, u377, u378, u379, u382, u383, u384, u385 | u46, u47, u48, u49, u50, u51, u52, u53, u54, u73, u74, u75, u76, u77, u78, u79, u80, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u190, u191, u192, u193, u194, u195, u196, u197, u198, u201, u202, u203, u204, u217, u218, u219, u220, u221, u222, u223, u226, u227, u228, u229, u242, u243, u244, u245, u246, u247, u248, u251, u252, u253, u254, u269, u270, u271, u272, u273, u274, u275, u278, u279, u280, u281, u296, u297, u298, u299, u300, u301, u302, u305, u306, u307, u308, u321, u322, u323, u324, u325, u326, u327, u330, u331, u332, u333, u350, u351, u352, u353, u354, u355, u356, u359, u360, u361, u362, u373, u374, u375, u376, u377, u378, u384 | 24/45 = 8/15 | 29/32 = 29/32 | u202, u203, u204, u227, u228, u229, u252, u253, u254, u279, u280, u281, u306, u307, u308, u331, u332, u333, u360, u361, u362, u383, u384, u385 | u201, u202, u203, u204, u226, u227, u228, u229, u251, u252, u253, u254, u278, u279, u280, u281, u305, u306, u307, u308, u330, u331, u332, u333, u359, u360, u361, u362, u382, u383, u384, u385 | u201, u202, u203, u204, u226, u227, u228, u229, u251, u252, u253, u254, u278, u279, u280, u281, u305, u306, u307, u308, u330, u331, u332, u333, u359, u360, u361, u362, u384 |
| pair-solo8-seed-29 | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) | none | none | none | 0/0 (N/A) | 0/0 (N/A) | none | none | none |

## Use profile

Bins present in either reading are printed; omitted (seat, source, kept) bins are zero in both.

| History | Actor | Seat | Source class | Kept (both) | Count wide | Use IDs wide | Count narrow | Use IDs narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-solo8-seed-29 | workshop:alice | 1 | other | True | 4 | u255, u257, u282, u386 | 4 | u255, u257, u282, u386 |
| pair-solo8-seed-29 | workshop:alice | 1 | self | False | 1 | u397 | 0 | none |
| pair-solo8-seed-29 | workshop:alice | 1 | self | True | 7 | u145, u146, u159, u160, u178, u179, u396 | 2 | u178, u179 |
| pair-solo8-seed-29 | workshop:alice | 2 | other | False | 1 | u277 | 0 | none |
| pair-solo8-seed-29 | workshop:alice | 2 | other | True | 12 | u180, u199, u200, u206, u207, u224, u225, u249, u250, u258, u259, u276 | 4 | u206, u207, u258, u259 |
| pair-solo8-seed-29 | workshop:alice | 2 | self | True | 2 | u144, u147 | 0 | none |
| pair-solo8-seed-29 | workshop:alice | 2 | world | True | 1 | u0 | 11 | u0, u144, u147, u180, u199, u200, u224, u225, u249, u250, u276 |
| pair-solo8-seed-29 | workshop:alice | 3 | other | True | 5 | u283, u337, u338, u387, u388 | 5 | u283, u337, u338, u387, u388 |
| pair-solo8-seed-29 | workshop:alice | 3 | self | False | 1 | u398 | 0 | none |
| pair-solo8-seed-29 | workshop:alice | 3 | self | True | 3 | u161, u177, u395 | 1 | u177 |
| pair-solo8-seed-29 | workshop:alice | 4 | self | False | 1 | u409 | 1 | u409 |
| pair-solo8-seed-29 | workshop:alice | 4 | self | True | 7 | u150, u151, u164, u165, u173, u174, u408 | 3 | u173, u174, u408 |
| pair-solo8-seed-29 | workshop:alice | 5 | other | False | 1 | u381 | 0 | none |
| pair-solo8-seed-29 | workshop:alice | 5 | other | True | 66 | u55, u56, u59, u62, u63, u65, u66, u69, u70, u81, u82, u85, u88, u89, u91, u92, u95, u98, u99, u137, u138, u141, u142, u182, u183, u186, u187, u209, u210, u213, u214, u234, u235, u238, u239, u256, u261, u262, u265, u266, u288, u289, u292, u293, u303, u304, u310, u311, u313, u314, u317, u318, u328, u329, u342, u343, u346, u347, u357, u358, u363, u365, u366, u369, u370, u380 | 4 | u256, u310, u311, u363 |
| pair-solo8-seed-29 | workshop:alice | 5 | self | True | 20 | u8, u9, u12, u13, u16, u17, u20, u21, u24, u25, u28, u31, u32, u35, u36, u38, u39, u42, u43, u158 | 7 | u303, u304, u328, u329, u357, u358, u380 |
| pair-solo8-seed-29 | workshop:alice | 6 | other | True | 62 | u57, u58, u60, u61, u64, u67, u68, u71, u72, u83, u84, u86, u87, u90, u93, u94, u96, u97, u135, u136, u139, u140, u181, u184, u185, u188, u189, u205, u208, u211, u212, u215, u216, u230, u236, u237, u240, u241, u260, u263, u264, u267, u268, u290, u291, u294, u295, u309, u312, u315, u316, u319, u320, u344, u345, u348, u349, u364, u367, u368, u371, u372 | 3 | u205, u230, u309 |
| pair-solo8-seed-29 | workshop:alice | 6 | self | False | 1 | u403 | 1 | u403 |
| pair-solo8-seed-29 | workshop:alice | 6 | self | True | 26 | u10, u11, u14, u15, u18, u19, u22, u23, u26, u27, u29, u30, u33, u34, u37, u40, u41, u44, u45, u143, u148, u156, u157, u167, u168, u402 | 3 | u167, u168, u402 |
| pair-solo8-seed-29 | workshop:alice | 6 | world | True | 3 | u1, u6, u7 | 85 | u1, u6, u7, u10, u11, u14, u15, u18, u19, u22, u23, u26, u27, u29, u30, u33, u34, u37, u40, u41, u44, u45, u57, u58, u60, u61, u64, u67, u68, u71, u72, u83, u84, u86, u87, u90, u93, u94, u96, u97, u135, u136, u139, u140, u143, u148, u156, u157, u181, u184, u185, u188, u189, u208, u211, u212, u215, u216, u236, u237, u240, u241, u260, u263, u264, u267, u268, u290, u291, u294, u295, u312, u315, u316, u319, u320, u344, u345, u348, u349, u364, u367, u368, u371, u372 |
| pair-solo8-seed-29 | workshop:alice | 7 | other | True | 7 | u233, u284, u287, u334, u336, u339, u341 | 3 | u284, u334, u336 |
| pair-solo8-seed-29 | workshop:alice | 7 | self | False | 1 | u406 | 0 | none |
| pair-solo8-seed-29 | workshop:alice | 7 | self | True | 13 | u153, u154, u162, u170, u171, u176, u389, u391, u392, u394, u399, u400, u405 | 3 | u170, u171, u176 |
| pair-solo8-seed-29 | workshop:alice | 7 | world | True | 2 | u3, u4 | 16 | u3, u4, u153, u154, u162, u233, u287, u339, u341, u389, u391, u392, u394, u399, u400, u405 |
| pair-solo8-seed-29 | workshop:alice | 8 | other | True | 6 | u231, u232, u285, u286, u335, u340 | 5 | u231, u232, u285, u286, u335 |
| pair-solo8-seed-29 | workshop:alice | 8 | self | False | 1 | u407 | 1 | u407 |
| pair-solo8-seed-29 | workshop:alice | 8 | self | True | 12 | u149, u152, u155, u163, u166, u169, u172, u175, u390, u393, u401, u404 | 5 | u166, u169, u172, u175, u401 |
| pair-solo8-seed-29 | workshop:alice | 8 | world | True | 2 | u2, u5 | 10 | u2, u5, u149, u152, u155, u163, u340, u390, u393, u404 |
| pair-solo8-seed-29 | workshop:bob | 1 | other | False | 1 | u382 | 1 | u382 |
| pair-solo8-seed-29 | workshop:bob | 1 | other | True | 41 | u49, u50, u75, u76, u102, u103, u108, u110, u113, u115, u116, u120, u121, u126, u128, u131, u133, u134, u193, u194, u201, u218, u219, u226, u243, u244, u251, u270, u271, u278, u297, u298, u305, u322, u323, u330, u351, u352, u359, u374, u375 | 7 | u201, u226, u251, u278, u305, u330, u359 |
| pair-solo8-seed-29 | workshop:bob | 2 | other | False | 1 | u379 | 0 | none |
| pair-solo8-seed-29 | workshop:bob | 2 | other | True | 54 | u46, u48, u51, u53, u54, u74, u77, u79, u80, u101, u104, u106, u107, u111, u112, u117, u119, u122, u124, u125, u129, u130, u190, u192, u195, u197, u198, u217, u220, u222, u223, u242, u245, u247, u248, u269, u272, u274, u275, u296, u299, u301, u302, u321, u324, u326, u327, u350, u353, u355, u356, u373, u376, u378 | 0 | none |
| pair-solo8-seed-29 | workshop:bob | 5 | other | False | 1 | u383 | 1 | u383 |
| pair-solo8-seed-29 | workshop:bob | 5 | other | True | 11 | u109, u114, u127, u132, u202, u227, u252, u279, u306, u331, u360 | 7 | u202, u227, u252, u279, u306, u331, u360 |
| pair-solo8-seed-29 | workshop:bob | 6 | other | False | 1 | u385 | 1 | u385 |
| pair-solo8-seed-29 | workshop:bob | 6 | other | True | 32 | u47, u52, u73, u78, u100, u105, u118, u123, u191, u196, u203, u204, u221, u228, u229, u246, u253, u254, u273, u280, u281, u300, u307, u308, u325, u332, u333, u354, u361, u362, u377, u384 | 15 | u203, u204, u228, u229, u253, u254, u280, u281, u307, u308, u332, u333, u361, u362, u384 |
| pair-solo8-seed-29 | workshop:alice | 1 | world | False | 0 | none | 1 | u397 |
| pair-solo8-seed-29 | workshop:alice | 1 | world | True | 0 | none | 5 | u145, u146, u159, u160, u396 |
| pair-solo8-seed-29 | workshop:alice | 2 | world | False | 0 | none | 1 | u277 |
| pair-solo8-seed-29 | workshop:alice | 3 | world | False | 0 | none | 1 | u398 |
| pair-solo8-seed-29 | workshop:alice | 3 | world | True | 0 | none | 2 | u161, u395 |
| pair-solo8-seed-29 | workshop:alice | 4 | world | True | 0 | none | 4 | u150, u151, u164, u165 |
| pair-solo8-seed-29 | workshop:alice | 5 | self | False | 0 | none | 1 | u381 |
| pair-solo8-seed-29 | workshop:alice | 5 | world | True | 0 | none | 75 | u8, u9, u12, u13, u16, u17, u20, u21, u24, u25, u28, u31, u32, u35, u36, u38, u39, u42, u43, u55, u56, u59, u62, u63, u65, u66, u69, u70, u81, u82, u85, u88, u89, u91, u92, u95, u98, u99, u137, u138, u141, u142, u158, u182, u183, u186, u187, u209, u210, u213, u214, u234, u235, u238, u239, u261, u262, u265, u266, u288, u289, u292, u293, u313, u314, u317, u318, u342, u343, u346, u347, u365, u366, u369, u370 |
| pair-solo8-seed-29 | workshop:alice | 7 | world | False | 0 | none | 1 | u406 |
| pair-solo8-seed-29 | workshop:bob | 1 | world | True | 0 | none | 34 | u49, u50, u75, u76, u102, u103, u108, u110, u113, u115, u116, u120, u121, u126, u128, u131, u133, u134, u193, u194, u218, u219, u243, u244, u270, u271, u297, u298, u322, u323, u351, u352, u374, u375 |
| pair-solo8-seed-29 | workshop:bob | 2 | world | False | 0 | none | 1 | u379 |
| pair-solo8-seed-29 | workshop:bob | 2 | world | True | 0 | none | 54 | u46, u48, u51, u53, u54, u74, u77, u79, u80, u101, u104, u106, u107, u111, u112, u117, u119, u122, u124, u125, u129, u130, u190, u192, u195, u197, u198, u217, u220, u222, u223, u242, u245, u247, u248, u269, u272, u274, u275, u296, u299, u301, u302, u321, u324, u326, u327, u350, u353, u355, u356, u373, u376, u378 |
| pair-solo8-seed-29 | workshop:bob | 5 | world | True | 0 | none | 4 | u109, u114, u127, u132 |
| pair-solo8-seed-29 | workshop:bob | 6 | world | True | 0 | none | 17 | u47, u52, u73, u78, u100, u105, u118, u123, u191, u196, u221, u246, u273, u300, u325, u354, u377 |

## Weak-seat supplier map

Each dim <= 2 seat is listed, including empty supplier sets.

| History | Receiver | Seat | Supplier | Count wide | Use IDs wide | Count narrow | Use IDs narrow |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pair-solo8-seed-29 | workshop:alice | 3 | workshop:bob | 5 | u283, u337, u338, u387, u388 | 5 | u283, u337, u338, u387, u388 |
| pair-solo8-seed-29 | workshop:alice | 4 | none | 0 | none | 0 | none |
| pair-solo8-seed-29 | workshop:alice | 5 | workshop:bob | 67 | u55, u56, u59, u62, u63, u65, u66, u69, u70, u81, u82, u85, u88, u89, u91, u92, u95, u98, u99, u137, u138, u141, u142, u182, u183, u186, u187, u209, u210, u213, u214, u234, u235, u238, u239, u256, u261, u262, u265, u266, u288, u289, u292, u293, u303, u304, u310, u311, u313, u314, u317, u318, u328, u329, u342, u343, u346, u347, u357, u358, u363, u365, u366, u369, u370, u380, u381 | 4 | u256, u310, u311, u363 |
| pair-solo8-seed-29 | workshop:alice | 6 | workshop:bob | 62 | u57, u58, u60, u61, u64, u67, u68, u71, u72, u83, u84, u86, u87, u90, u93, u94, u96, u97, u135, u136, u139, u140, u181, u184, u185, u188, u189, u205, u208, u211, u212, u215, u216, u230, u236, u237, u240, u241, u260, u263, u264, u267, u268, u290, u291, u294, u295, u309, u312, u315, u316, u319, u320, u344, u345, u348, u349, u364, u367, u368, u371, u372 | 3 | u205, u230, u309 |
| pair-solo8-seed-29 | workshop:bob | 3 | none | 0 | none | 0 | none |
| pair-solo8-seed-29 | workshop:bob | 4 | none | 0 | none | 0 | none |
| pair-solo8-seed-29 | workshop:bob | 5 | workshop:alice | 12 | u109, u114, u127, u132, u202, u227, u252, u279, u306, u331, u360, u383 | 8 | u202, u227, u252, u279, u306, u331, u360, u383 |
| pair-solo8-seed-29 | workshop:bob | 6 | workshop:alice | 33 | u47, u52, u73, u78, u100, u105, u118, u123, u191, u196, u203, u204, u221, u228, u229, u246, u253, u254, u273, u280, u281, u300, u307, u308, u325, u332, u333, u354, u361, u362, u377, u384, u385 | 16 | u203, u204, u228, u229, u253, u254, u280, u281, u307, u308, u332, u333, u361, u362, u384, u385 |
| pair-solo8-seed-29 | workshop:eve | 3 | none | 0 | none | 0 | none |
| pair-solo8-seed-29 | workshop:eve | 4 | none | 0 | none | 0 | none |
| pair-solo8-seed-29 | workshop:eve | 5 | none | 0 | none | 0 | none |
| pair-solo8-seed-29 | workshop:eve | 6 | none | 0 | none | 0 | none |

## Use trace

Transaction and episode indices are zero-based.

| History | Use ID | Transaction | Operation revision | Block end | Actor | Element | Seat | Dim | Source wide | Source narrow | Kept (both) | Episode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-solo8-seed-29 | u0 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 24 | workshop:alice | fi | 2 | 3 | world | world | True | 0 |
| pair-solo8-seed-29 | u1 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 27 | workshop:alice | te | 6 | 2 | world | world | True | 0 |
| pair-solo8-seed-29 | u2 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 28 | workshop:alice | fe | 8 | 4 | world | world | True | 0 |
| pair-solo8-seed-29 | u3 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 30 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| pair-solo8-seed-29 | u4 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 32 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| pair-solo8-seed-29 | u5 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 33 | workshop:alice | fe | 8 | 4 | world | world | True | 0 |
| pair-solo8-seed-29 | u6 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 36 | workshop:alice | te | 6 | 2 | world | world | True | 0 |
| pair-solo8-seed-29 | u7 | 310 | u4.operation:2ce6d4eba8bf840af397058663a0aa5d28737042849e2b385177eaabf077c9fe@2 | 39 | workshop:alice | te | 6 | 2 | world | world | True | 0 |
| pair-solo8-seed-29 | u8 | 322 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 327 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u9 | 322 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 331 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u10 | 322 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 334 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u11 | 322 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 337 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u12 | 328 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 339 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u13 | 328 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 343 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u14 | 328 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 346 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u15 | 328 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 349 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u16 | 334 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 326 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u17 | 334 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 330 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u18 | 334 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 333 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u19 | 334 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 336 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u20 | 340 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 327 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u21 | 340 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 331 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u22 | 340 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 334 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u23 | 340 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 337 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u24 | 343 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 327 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u25 | 343 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 331 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u26 | 343 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 334 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u27 | 343 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 337 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u28 | 356 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 343 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u29 | 356 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 346 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u30 | 356 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 349 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u31 | 356 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 353 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u32 | 356 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 357 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u33 | 362 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 343 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u34 | 362 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 346 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u35 | 362 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 350 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u36 | 362 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 354 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u37 | 381 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 376 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u38 | 381 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 380 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u39 | 381 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 384 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u40 | 381 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 387 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u41 | 381 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 390 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u42 | 387 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 375 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u43 | 387 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 379 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u44 | 387 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 382 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u45 | 387 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 385 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u46 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 295 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u47 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 298 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u48 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 300 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u49 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 301 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u50 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 302 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u51 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 304 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u52 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 307 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u53 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 309 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u54 | 393 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 311 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u55 | 402 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 410 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u56 | 402 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 414 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u57 | 402 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 417 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u58 | 402 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 420 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u59 | 405 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 377 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u60 | 405 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 380 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u61 | 405 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 383 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u62 | 405 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 387 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u63 | 405 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 391 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u64 | 411 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 377 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u65 | 411 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 381 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u66 | 411 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 385 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u67 | 411 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 388 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u68 | 411 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 391 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u69 | 417 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 379 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u70 | 417 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 383 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u71 | 417 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 386 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u72 | 417 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 389 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u73 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 297 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u74 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 299 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u75 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 300 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u76 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 301 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u77 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 303 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u78 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 306 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u79 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 308 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u80 | 423 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 310 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u81 | 432 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 391 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u82 | 432 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 395 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u83 | 432 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 398 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u84 | 432 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 401 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u85 | 445 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 407 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u86 | 445 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 410 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u87 | 445 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 413 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u88 | 445 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 417 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u89 | 445 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 421 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u90 | 454 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 413 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u91 | 454 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 417 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u92 | 454 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 421 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u93 | 454 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 424 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u94 | 454 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 427 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u95 | 467 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 427 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u96 | 467 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 430 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u97 | 467 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 433 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u98 | 467 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 437 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u99 | 467 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 441 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u100 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 304 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u101 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 306 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u102 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 307 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u103 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 308 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u104 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 310 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u105 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 313 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u106 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 315 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u107 | 476 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 317 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u108 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 315 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u109 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 319 | workshop:bob | ne | 5 | 1 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u110 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 320 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u111 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 322 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u112 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 324 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u113 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 325 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u114 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 329 | workshop:bob | ne | 5 | 1 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u115 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 330 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u116 | 493 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 331 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u117 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 329 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u118 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 332 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u119 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 334 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u120 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 335 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u121 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 336 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u122 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 338 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u123 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 341 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u124 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 343 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u125 | 505 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 345 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u126 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 344 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u127 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 348 | workshop:bob | ne | 5 | 1 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u128 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 349 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u129 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 351 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u130 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 353 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u131 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 354 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u132 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 358 | workshop:bob | ne | 5 | 1 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u133 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 359 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u134 | 522 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 360 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u135 | 528 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 454 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u136 | 528 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 457 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u137 | 528 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 461 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u138 | 528 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 465 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u139 | 531 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 454 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u140 | 531 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 457 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u141 | 531 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 461 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u142 | 531 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 465 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u143 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 25 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u144 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 27 | workshop:alice | fi | 2 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u145 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 28 | workshop:alice | ne | 1 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u146 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 29 | workshop:alice | ne | 1 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u147 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 31 | workshop:alice | fi | 2 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u148 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 34 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u149 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 35 | workshop:alice | fe | 8 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u150 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 39 | workshop:alice | ti | 4 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u151 | 554 | u4.operation:e0a8aaf08ccbba14179c4a5ada6887f4c644d04142a11d7a417997d0e5badeb1@2 | 43 | workshop:alice | ti | 4 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u152 | 577 | u4.operation:14e74e99d6fb53fb0fde5d2d812938ab444f436a66c7d4a196860b089b355c16@2 | 17 | workshop:alice | fe | 8 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u153 | 577 | u4.operation:14e74e99d6fb53fb0fde5d2d812938ab444f436a66c7d4a196860b089b355c16@2 | 19 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u154 | 577 | u4.operation:14e74e99d6fb53fb0fde5d2d812938ab444f436a66c7d4a196860b089b355c16@2 | 21 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u155 | 577 | u4.operation:14e74e99d6fb53fb0fde5d2d812938ab444f436a66c7d4a196860b089b355c16@2 | 22 | workshop:alice | fe | 8 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u156 | 577 | u4.operation:14e74e99d6fb53fb0fde5d2d812938ab444f436a66c7d4a196860b089b355c16@2 | 25 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u157 | 577 | u4.operation:14e74e99d6fb53fb0fde5d2d812938ab444f436a66c7d4a196860b089b355c16@2 | 28 | workshop:alice | te | 6 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u158 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 19 | workshop:alice | si | 5 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u159 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 20 | workshop:alice | ne | 1 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u160 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 21 | workshop:alice | ne | 1 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u161 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 24 | workshop:alice | se | 3 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u162 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 26 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u163 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 27 | workshop:alice | fe | 8 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u164 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 31 | workshop:alice | ti | 4 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u165 | 584 | u4.operation:eedcecc2e6fb2ac4cf61aa282c5be379e778d2ee9a38439cb3287aa017360cbf@2 | 35 | workshop:alice | ti | 4 | 1 | self | world | True | 0 |
| pair-solo8-seed-29 | u166 | 594 | u4.operation:c7c377e494ce00a4a5422a8fd2fc2f9f235fe56a81e656d91360a5cf04fe48ef@2 | 41 | workshop:alice | fe | 8 | 4 | self | self | True | 0 |
| pair-solo8-seed-29 | u167 | 594 | u4.operation:c7c377e494ce00a4a5422a8fd2fc2f9f235fe56a81e656d91360a5cf04fe48ef@2 | 44 | workshop:alice | te | 6 | 2 | self | self | True | 0 |
| pair-solo8-seed-29 | u168 | 594 | u4.operation:c7c377e494ce00a4a5422a8fd2fc2f9f235fe56a81e656d91360a5cf04fe48ef@2 | 47 | workshop:alice | te | 6 | 2 | self | self | True | 0 |
| pair-solo8-seed-29 | u169 | 594 | u4.operation:c7c377e494ce00a4a5422a8fd2fc2f9f235fe56a81e656d91360a5cf04fe48ef@2 | 48 | workshop:alice | fe | 8 | 4 | self | self | True | 0 |
| pair-solo8-seed-29 | u170 | 594 | u4.operation:c7c377e494ce00a4a5422a8fd2fc2f9f235fe56a81e656d91360a5cf04fe48ef@2 | 50 | workshop:alice | ni | 7 | 3 | self | self | True | 0 |
| pair-solo8-seed-29 | u171 | 594 | u4.operation:c7c377e494ce00a4a5422a8fd2fc2f9f235fe56a81e656d91360a5cf04fe48ef@2 | 52 | workshop:alice | ni | 7 | 3 | self | self | True | 0 |
| pair-solo8-seed-29 | u172 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 41 | workshop:alice | fe | 8 | 4 | self | self | True | 0 |
| pair-solo8-seed-29 | u173 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 45 | workshop:alice | ti | 4 | 1 | self | self | True | 0 |
| pair-solo8-seed-29 | u174 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 49 | workshop:alice | ti | 4 | 1 | self | self | True | 0 |
| pair-solo8-seed-29 | u175 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 50 | workshop:alice | fe | 8 | 4 | self | self | True | 0 |
| pair-solo8-seed-29 | u176 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 52 | workshop:alice | ni | 7 | 3 | self | self | True | 0 |
| pair-solo8-seed-29 | u177 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 55 | workshop:alice | se | 3 | 2 | self | self | True | 0 |
| pair-solo8-seed-29 | u178 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 56 | workshop:alice | ne | 1 | 4 | self | self | True | 0 |
| pair-solo8-seed-29 | u179 | 604 | u4.operation:a9a31f78e3661e8a2c2b85af1069f66b63251dcccae065138d854c9fa3e7d46d@2 | 57 | workshop:alice | ne | 1 | 4 | self | self | True | 0 |
| pair-solo8-seed-29 | u180 | 611 | u4.operation:752dc996135b68fb370633d835ff3035e977e4e8e5a6f914f13d0921fcb54052@2 | 537 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u181 | 611 | u4.operation:752dc996135b68fb370633d835ff3035e977e4e8e5a6f914f13d0921fcb54052@2 | 540 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u182 | 611 | u4.operation:752dc996135b68fb370633d835ff3035e977e4e8e5a6f914f13d0921fcb54052@2 | 544 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u183 | 611 | u4.operation:752dc996135b68fb370633d835ff3035e977e4e8e5a6f914f13d0921fcb54052@2 | 548 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u184 | 611 | u4.operation:752dc996135b68fb370633d835ff3035e977e4e8e5a6f914f13d0921fcb54052@2 | 551 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u185 | 611 | u4.operation:752dc996135b68fb370633d835ff3035e977e4e8e5a6f914f13d0921fcb54052@2 | 554 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u186 | 617 | u4.operation:bfdff29eb04709644010a8cf813982be6fd5c2565dc4cdcd4f8fa3a49eba5f64@2 | 540 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u187 | 617 | u4.operation:bfdff29eb04709644010a8cf813982be6fd5c2565dc4cdcd4f8fa3a49eba5f64@2 | 544 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u188 | 617 | u4.operation:bfdff29eb04709644010a8cf813982be6fd5c2565dc4cdcd4f8fa3a49eba5f64@2 | 547 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u189 | 617 | u4.operation:bfdff29eb04709644010a8cf813982be6fd5c2565dc4cdcd4f8fa3a49eba5f64@2 | 550 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u190 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 346 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u191 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 349 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u192 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 351 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u193 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 352 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u194 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 353 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u195 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 355 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u196 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 358 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u197 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 360 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u198 | 623 | u4.operation:2d9ab27bb5f04914cb357ed9c1a747b29791acfef31d2f0761f65cd456a25aed@2 | 362 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u199 | 636 | u4.operation:fc4076bf9c9ca1d249c90b52a2894eb5574810268ded9a2f7078f09bec116e34@2 | 27 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u200 | 636 | u4.operation:fc4076bf9c9ca1d249c90b52a2894eb5574810268ded9a2f7078f09bec116e34@2 | 29 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u201 | 649 | u4.operation:39af288da072deaf202f6936fc211629b640dd5b4f3ab2fc4b9b80cbb166dff0@2 | 45 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u202 | 649 | u4.operation:39af288da072deaf202f6936fc211629b640dd5b4f3ab2fc4b9b80cbb166dff0@2 | 49 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u203 | 649 | u4.operation:39af288da072deaf202f6936fc211629b640dd5b4f3ab2fc4b9b80cbb166dff0@2 | 52 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u204 | 649 | u4.operation:39af288da072deaf202f6936fc211629b640dd5b4f3ab2fc4b9b80cbb166dff0@2 | 55 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u205 | 655 | u4.operation:f97ccbcec5bc89c639395222723f4df04e1b2bc829f677203e79695b1099d6c3@2 | 83 | workshop:alice | te | 6 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u206 | 655 | u4.operation:f97ccbcec5bc89c639395222723f4df04e1b2bc829f677203e79695b1099d6c3@2 | 85 | workshop:alice | fi | 2 | 3 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u207 | 655 | u4.operation:f97ccbcec5bc89c639395222723f4df04e1b2bc829f677203e79695b1099d6c3@2 | 87 | workshop:alice | fi | 2 | 3 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u208 | 662 | u4.operation:431c7bbfdc26fccbe1f45f5f036aabe4842ca80ad7e59e20119b33f3c96f0d0d@2 | 542 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u209 | 662 | u4.operation:431c7bbfdc26fccbe1f45f5f036aabe4842ca80ad7e59e20119b33f3c96f0d0d@2 | 546 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u210 | 662 | u4.operation:431c7bbfdc26fccbe1f45f5f036aabe4842ca80ad7e59e20119b33f3c96f0d0d@2 | 550 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u211 | 662 | u4.operation:431c7bbfdc26fccbe1f45f5f036aabe4842ca80ad7e59e20119b33f3c96f0d0d@2 | 553 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u212 | 662 | u4.operation:431c7bbfdc26fccbe1f45f5f036aabe4842ca80ad7e59e20119b33f3c96f0d0d@2 | 556 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u213 | 668 | u4.operation:220701be14c25544d07f31b225d9fb356547b0575382c440b8e747409d443fd2@2 | 544 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u214 | 668 | u4.operation:220701be14c25544d07f31b225d9fb356547b0575382c440b8e747409d443fd2@2 | 548 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u215 | 668 | u4.operation:220701be14c25544d07f31b225d9fb356547b0575382c440b8e747409d443fd2@2 | 551 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u216 | 668 | u4.operation:220701be14c25544d07f31b225d9fb356547b0575382c440b8e747409d443fd2@2 | 554 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u217 | 674 | u4.operation:1f8640ca5b9aceb56aa35b093bc5544520b2a211da12a63b2ab3f757e11a80fe@2 | 349 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u218 | 674 | u4.operation:1f8640ca5b9aceb56aa35b093bc5544520b2a211da12a63b2ab3f757e11a80fe@2 | 350 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u219 | 674 | u4.operation:1f8640ca5b9aceb56aa35b093bc5544520b2a211da12a63b2ab3f757e11a80fe@2 | 351 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u220 | 674 | u4.operation:1f8640ca5b9aceb56aa35b093bc5544520b2a211da12a63b2ab3f757e11a80fe@2 | 353 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u221 | 674 | u4.operation:1f8640ca5b9aceb56aa35b093bc5544520b2a211da12a63b2ab3f757e11a80fe@2 | 356 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u222 | 674 | u4.operation:1f8640ca5b9aceb56aa35b093bc5544520b2a211da12a63b2ab3f757e11a80fe@2 | 358 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u223 | 674 | u4.operation:1f8640ca5b9aceb56aa35b093bc5544520b2a211da12a63b2ab3f757e11a80fe@2 | 360 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u224 | 687 | u4.operation:483e8ca2aff5c90f4e612fc8f8c1b8131314c31aa7b13864241d39f609a28ab8@2 | 27 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u225 | 687 | u4.operation:483e8ca2aff5c90f4e612fc8f8c1b8131314c31aa7b13864241d39f609a28ab8@2 | 29 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u226 | 700 | u4.operation:49f7cddf76d2c780bdaeb2635589e43204a87aeeda9763af550370ed28db1cec@2 | 45 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u227 | 700 | u4.operation:49f7cddf76d2c780bdaeb2635589e43204a87aeeda9763af550370ed28db1cec@2 | 49 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u228 | 700 | u4.operation:49f7cddf76d2c780bdaeb2635589e43204a87aeeda9763af550370ed28db1cec@2 | 52 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u229 | 700 | u4.operation:49f7cddf76d2c780bdaeb2635589e43204a87aeeda9763af550370ed28db1cec@2 | 55 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u230 | 706 | u4.operation:a8e8dcc2037a7b43060467e81a48022ae89f4a7611017bb65fbf41c0c45517a9@2 | 83 | workshop:alice | te | 6 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u231 | 706 | u4.operation:a8e8dcc2037a7b43060467e81a48022ae89f4a7611017bb65fbf41c0c45517a9@2 | 84 | workshop:alice | fe | 8 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u232 | 706 | u4.operation:a8e8dcc2037a7b43060467e81a48022ae89f4a7611017bb65fbf41c0c45517a9@2 | 85 | workshop:alice | fe | 8 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u233 | 713 | u4.operation:a3e60d56b9f01a9836e13160844428b66048a26c67b9bf37e0bccf337d152da0@2 | 545 | workshop:alice | ni | 7 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u234 | 713 | u4.operation:a3e60d56b9f01a9836e13160844428b66048a26c67b9bf37e0bccf337d152da0@2 | 549 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u235 | 713 | u4.operation:a3e60d56b9f01a9836e13160844428b66048a26c67b9bf37e0bccf337d152da0@2 | 553 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u236 | 713 | u4.operation:a3e60d56b9f01a9836e13160844428b66048a26c67b9bf37e0bccf337d152da0@2 | 556 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u237 | 713 | u4.operation:a3e60d56b9f01a9836e13160844428b66048a26c67b9bf37e0bccf337d152da0@2 | 559 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u238 | 719 | u4.operation:834a72c8c5e13d903302e8278b32af1250faa97e3bbe007f73e4e48d0bb2bd98@2 | 548 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u239 | 719 | u4.operation:834a72c8c5e13d903302e8278b32af1250faa97e3bbe007f73e4e48d0bb2bd98@2 | 552 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u240 | 719 | u4.operation:834a72c8c5e13d903302e8278b32af1250faa97e3bbe007f73e4e48d0bb2bd98@2 | 555 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u241 | 719 | u4.operation:834a72c8c5e13d903302e8278b32af1250faa97e3bbe007f73e4e48d0bb2bd98@2 | 558 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u242 | 725 | u4.operation:b82ea43a946639a708adf8df82f8864a1b32c31e926c537c8b15467da6f5a30b@2 | 352 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u243 | 725 | u4.operation:b82ea43a946639a708adf8df82f8864a1b32c31e926c537c8b15467da6f5a30b@2 | 353 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u244 | 725 | u4.operation:b82ea43a946639a708adf8df82f8864a1b32c31e926c537c8b15467da6f5a30b@2 | 354 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u245 | 725 | u4.operation:b82ea43a946639a708adf8df82f8864a1b32c31e926c537c8b15467da6f5a30b@2 | 356 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u246 | 725 | u4.operation:b82ea43a946639a708adf8df82f8864a1b32c31e926c537c8b15467da6f5a30b@2 | 359 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u247 | 725 | u4.operation:b82ea43a946639a708adf8df82f8864a1b32c31e926c537c8b15467da6f5a30b@2 | 361 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u248 | 725 | u4.operation:b82ea43a946639a708adf8df82f8864a1b32c31e926c537c8b15467da6f5a30b@2 | 363 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u249 | 738 | u4.operation:8a6a9cc488d0073ea4f827564f761e8466801259ea6454b97b36e56d55ab28fd@2 | 27 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u250 | 738 | u4.operation:8a6a9cc488d0073ea4f827564f761e8466801259ea6454b97b36e56d55ab28fd@2 | 29 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u251 | 751 | u4.operation:63bc4fd2524adcfff4353cd00109c5ba79089e727988636b3b203dc8757cd285@2 | 45 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u252 | 751 | u4.operation:63bc4fd2524adcfff4353cd00109c5ba79089e727988636b3b203dc8757cd285@2 | 49 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u253 | 751 | u4.operation:63bc4fd2524adcfff4353cd00109c5ba79089e727988636b3b203dc8757cd285@2 | 52 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u254 | 751 | u4.operation:63bc4fd2524adcfff4353cd00109c5ba79089e727988636b3b203dc8757cd285@2 | 55 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u255 | 757 | u4.operation:4b7ef3d07c52d0670e615d918ad99b16e0894cd9dc3986a532f13d7e2bdee983@2 | 81 | workshop:alice | ne | 1 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u256 | 757 | u4.operation:4b7ef3d07c52d0670e615d918ad99b16e0894cd9dc3986a532f13d7e2bdee983@2 | 85 | workshop:alice | si | 5 | 1 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u257 | 757 | u4.operation:4b7ef3d07c52d0670e615d918ad99b16e0894cd9dc3986a532f13d7e2bdee983@2 | 86 | workshop:alice | ne | 1 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u258 | 757 | u4.operation:4b7ef3d07c52d0670e615d918ad99b16e0894cd9dc3986a532f13d7e2bdee983@2 | 88 | workshop:alice | fi | 2 | 3 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u259 | 757 | u4.operation:4b7ef3d07c52d0670e615d918ad99b16e0894cd9dc3986a532f13d7e2bdee983@2 | 90 | workshop:alice | fi | 2 | 3 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u260 | 764 | u4.operation:7761107d33c0150f25d0845906fad18039749c4afd228376232222182a1d37d5@2 | 550 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u261 | 764 | u4.operation:7761107d33c0150f25d0845906fad18039749c4afd228376232222182a1d37d5@2 | 554 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u262 | 764 | u4.operation:7761107d33c0150f25d0845906fad18039749c4afd228376232222182a1d37d5@2 | 558 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u263 | 764 | u4.operation:7761107d33c0150f25d0845906fad18039749c4afd228376232222182a1d37d5@2 | 561 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u264 | 764 | u4.operation:7761107d33c0150f25d0845906fad18039749c4afd228376232222182a1d37d5@2 | 564 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u265 | 770 | u4.operation:57334350d3688d5375f5b7100daee512e5e01e9dfe6f87bc3eab36e655e3abd1@2 | 552 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u266 | 770 | u4.operation:57334350d3688d5375f5b7100daee512e5e01e9dfe6f87bc3eab36e655e3abd1@2 | 556 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u267 | 770 | u4.operation:57334350d3688d5375f5b7100daee512e5e01e9dfe6f87bc3eab36e655e3abd1@2 | 559 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u268 | 770 | u4.operation:57334350d3688d5375f5b7100daee512e5e01e9dfe6f87bc3eab36e655e3abd1@2 | 562 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u269 | 776 | u4.operation:f7df360183f0c9bb4d227abdf0aa0ccc33dca2d12db4ff1236eca9a562aaaf2f@2 | 355 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u270 | 776 | u4.operation:f7df360183f0c9bb4d227abdf0aa0ccc33dca2d12db4ff1236eca9a562aaaf2f@2 | 356 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u271 | 776 | u4.operation:f7df360183f0c9bb4d227abdf0aa0ccc33dca2d12db4ff1236eca9a562aaaf2f@2 | 357 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u272 | 776 | u4.operation:f7df360183f0c9bb4d227abdf0aa0ccc33dca2d12db4ff1236eca9a562aaaf2f@2 | 359 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u273 | 776 | u4.operation:f7df360183f0c9bb4d227abdf0aa0ccc33dca2d12db4ff1236eca9a562aaaf2f@2 | 362 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u274 | 776 | u4.operation:f7df360183f0c9bb4d227abdf0aa0ccc33dca2d12db4ff1236eca9a562aaaf2f@2 | 364 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u275 | 776 | u4.operation:f7df360183f0c9bb4d227abdf0aa0ccc33dca2d12db4ff1236eca9a562aaaf2f@2 | 366 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u276 | 789 | u4.operation:8c5426eb7cb8377929e96d59f6d2316972b1d7cd0c663d6088f055edca94f4ad@2 | 27 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u277 | 789 | u4.operation:8c5426eb7cb8377929e96d59f6d2316972b1d7cd0c663d6088f055edca94f4ad@2 | 29 | workshop:alice | fi | 2 | 3 | (workshop:bob) | world | False | 0 |
| pair-solo8-seed-29 | u278 | 802 | u4.operation:f29c934e113a90dcc2e759b71c609f88db4871c5033837cebc8428679e57d79d@2 | 45 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u279 | 802 | u4.operation:f29c934e113a90dcc2e759b71c609f88db4871c5033837cebc8428679e57d79d@2 | 49 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u280 | 802 | u4.operation:f29c934e113a90dcc2e759b71c609f88db4871c5033837cebc8428679e57d79d@2 | 52 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u281 | 802 | u4.operation:f29c934e113a90dcc2e759b71c609f88db4871c5033837cebc8428679e57d79d@2 | 55 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u282 | 808 | u4.operation:3623a20e489bf45025dbde3be535227516d290fea4ac41c3f18275b7013a608d@2 | 81 | workshop:alice | ne | 1 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u283 | 808 | u4.operation:3623a20e489bf45025dbde3be535227516d290fea4ac41c3f18275b7013a608d@2 | 84 | workshop:alice | se | 3 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u284 | 808 | u4.operation:3623a20e489bf45025dbde3be535227516d290fea4ac41c3f18275b7013a608d@2 | 86 | workshop:alice | ni | 7 | 3 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u285 | 808 | u4.operation:3623a20e489bf45025dbde3be535227516d290fea4ac41c3f18275b7013a608d@2 | 87 | workshop:alice | fe | 8 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u286 | 808 | u4.operation:3623a20e489bf45025dbde3be535227516d290fea4ac41c3f18275b7013a608d@2 | 88 | workshop:alice | fe | 8 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u287 | 818 | u4.operation:285c4afb5434e95d53016f65a308eeb71c824078bfcce0d46db590a507504294@2 | 565 | workshop:alice | ni | 7 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u288 | 818 | u4.operation:285c4afb5434e95d53016f65a308eeb71c824078bfcce0d46db590a507504294@2 | 569 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u289 | 818 | u4.operation:285c4afb5434e95d53016f65a308eeb71c824078bfcce0d46db590a507504294@2 | 573 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u290 | 818 | u4.operation:285c4afb5434e95d53016f65a308eeb71c824078bfcce0d46db590a507504294@2 | 576 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u291 | 818 | u4.operation:285c4afb5434e95d53016f65a308eeb71c824078bfcce0d46db590a507504294@2 | 579 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u292 | 824 | u4.operation:b3e23093d4e78c8d24f923ddd44d143cc3fef10650c0bd55869c8bb54c340866@2 | 568 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u293 | 824 | u4.operation:b3e23093d4e78c8d24f923ddd44d143cc3fef10650c0bd55869c8bb54c340866@2 | 572 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u294 | 824 | u4.operation:b3e23093d4e78c8d24f923ddd44d143cc3fef10650c0bd55869c8bb54c340866@2 | 575 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u295 | 824 | u4.operation:b3e23093d4e78c8d24f923ddd44d143cc3fef10650c0bd55869c8bb54c340866@2 | 578 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u296 | 830 | u4.operation:c4a0f936b198d3e11a0a4dc6257539fb2bcc300d4e8563054200a9440b2d8ffb@2 | 358 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u297 | 830 | u4.operation:c4a0f936b198d3e11a0a4dc6257539fb2bcc300d4e8563054200a9440b2d8ffb@2 | 359 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u298 | 830 | u4.operation:c4a0f936b198d3e11a0a4dc6257539fb2bcc300d4e8563054200a9440b2d8ffb@2 | 360 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u299 | 830 | u4.operation:c4a0f936b198d3e11a0a4dc6257539fb2bcc300d4e8563054200a9440b2d8ffb@2 | 362 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u300 | 830 | u4.operation:c4a0f936b198d3e11a0a4dc6257539fb2bcc300d4e8563054200a9440b2d8ffb@2 | 365 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u301 | 830 | u4.operation:c4a0f936b198d3e11a0a4dc6257539fb2bcc300d4e8563054200a9440b2d8ffb@2 | 367 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u302 | 830 | u4.operation:c4a0f936b198d3e11a0a4dc6257539fb2bcc300d4e8563054200a9440b2d8ffb@2 | 369 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u303 | 843 | u4.operation:0a24de95eeeb7ab91c6bfb42f436bbbfbb92839dc17ee268bc090f0d104a2e2a@2 | 53 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | True | 0 |
| pair-solo8-seed-29 | u304 | 843 | u4.operation:0a24de95eeeb7ab91c6bfb42f436bbbfbb92839dc17ee268bc090f0d104a2e2a@2 | 57 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | True | 0 |
| pair-solo8-seed-29 | u305 | 856 | u4.operation:28553e8a35bc2e01090ef12a14496099ba8da4059837690e5d2e73c1d1b273f0@2 | 46 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u306 | 856 | u4.operation:28553e8a35bc2e01090ef12a14496099ba8da4059837690e5d2e73c1d1b273f0@2 | 50 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u307 | 856 | u4.operation:28553e8a35bc2e01090ef12a14496099ba8da4059837690e5d2e73c1d1b273f0@2 | 53 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u308 | 856 | u4.operation:28553e8a35bc2e01090ef12a14496099ba8da4059837690e5d2e73c1d1b273f0@2 | 56 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u309 | 862 | u4.operation:051f1111849e965f07423edcb70cd4ef5cbf6062f6b45c7d6df25a1f17ee3603@2 | 108 | workshop:alice | te | 6 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u310 | 862 | u4.operation:051f1111849e965f07423edcb70cd4ef5cbf6062f6b45c7d6df25a1f17ee3603@2 | 112 | workshop:alice | si | 5 | 1 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u311 | 862 | u4.operation:051f1111849e965f07423edcb70cd4ef5cbf6062f6b45c7d6df25a1f17ee3603@2 | 116 | workshop:alice | si | 5 | 1 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u312 | 872 | u4.operation:51070b3244dd07d3bd2b4edfccc408f923f9957e05210df0f2c077c15f5d007b@2 | 582 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u313 | 872 | u4.operation:51070b3244dd07d3bd2b4edfccc408f923f9957e05210df0f2c077c15f5d007b@2 | 586 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u314 | 872 | u4.operation:51070b3244dd07d3bd2b4edfccc408f923f9957e05210df0f2c077c15f5d007b@2 | 590 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u315 | 872 | u4.operation:51070b3244dd07d3bd2b4edfccc408f923f9957e05210df0f2c077c15f5d007b@2 | 593 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u316 | 872 | u4.operation:51070b3244dd07d3bd2b4edfccc408f923f9957e05210df0f2c077c15f5d007b@2 | 596 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u317 | 878 | u4.operation:9cb930546b77fa152afae8291ac3df1bd8d4bd5895b270e1476127fa2236e55b@2 | 584 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u318 | 878 | u4.operation:9cb930546b77fa152afae8291ac3df1bd8d4bd5895b270e1476127fa2236e55b@2 | 588 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u319 | 878 | u4.operation:9cb930546b77fa152afae8291ac3df1bd8d4bd5895b270e1476127fa2236e55b@2 | 591 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u320 | 878 | u4.operation:9cb930546b77fa152afae8291ac3df1bd8d4bd5895b270e1476127fa2236e55b@2 | 594 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u321 | 884 | u4.operation:a4cfc0a088bf9b08679c96da17c16ef919470e030db97bc9c788568046726544@2 | 361 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u322 | 884 | u4.operation:a4cfc0a088bf9b08679c96da17c16ef919470e030db97bc9c788568046726544@2 | 362 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u323 | 884 | u4.operation:a4cfc0a088bf9b08679c96da17c16ef919470e030db97bc9c788568046726544@2 | 363 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u324 | 884 | u4.operation:a4cfc0a088bf9b08679c96da17c16ef919470e030db97bc9c788568046726544@2 | 365 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u325 | 884 | u4.operation:a4cfc0a088bf9b08679c96da17c16ef919470e030db97bc9c788568046726544@2 | 368 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u326 | 884 | u4.operation:a4cfc0a088bf9b08679c96da17c16ef919470e030db97bc9c788568046726544@2 | 370 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u327 | 884 | u4.operation:a4cfc0a088bf9b08679c96da17c16ef919470e030db97bc9c788568046726544@2 | 372 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u328 | 897 | u4.operation:302c782f4d5a8e0ca1e002c48381f9880bdce78839ea9e32e1ecc392bf04acd9@2 | 53 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | True | 0 |
| pair-solo8-seed-29 | u329 | 897 | u4.operation:302c782f4d5a8e0ca1e002c48381f9880bdce78839ea9e32e1ecc392bf04acd9@2 | 57 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | True | 0 |
| pair-solo8-seed-29 | u330 | 910 | u4.operation:101a7c5857935f4666e7d753b3369c7d670a9e8b94a3df4d8845d64cd19db2c9@2 | 46 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u331 | 910 | u4.operation:101a7c5857935f4666e7d753b3369c7d670a9e8b94a3df4d8845d64cd19db2c9@2 | 50 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u332 | 910 | u4.operation:101a7c5857935f4666e7d753b3369c7d670a9e8b94a3df4d8845d64cd19db2c9@2 | 53 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u333 | 910 | u4.operation:101a7c5857935f4666e7d753b3369c7d670a9e8b94a3df4d8845d64cd19db2c9@2 | 56 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u334 | 916 | u4.operation:3c49bcd3801e3b3c00a0cbe4449a35aadc2a989aadd623bee6b5e0e87fea036e@2 | 107 | workshop:alice | ni | 7 | 3 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u335 | 916 | u4.operation:3c49bcd3801e3b3c00a0cbe4449a35aadc2a989aadd623bee6b5e0e87fea036e@2 | 108 | workshop:alice | fe | 8 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u336 | 916 | u4.operation:3c49bcd3801e3b3c00a0cbe4449a35aadc2a989aadd623bee6b5e0e87fea036e@2 | 110 | workshop:alice | ni | 7 | 3 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u337 | 916 | u4.operation:3c49bcd3801e3b3c00a0cbe4449a35aadc2a989aadd623bee6b5e0e87fea036e@2 | 113 | workshop:alice | se | 3 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u338 | 916 | u4.operation:3c49bcd3801e3b3c00a0cbe4449a35aadc2a989aadd623bee6b5e0e87fea036e@2 | 116 | workshop:alice | se | 3 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u339 | 926 | u4.operation:52240cda21628aff89032656fa871bbc072a2acad9f696548b7027f4b3b7e4dc@2 | 597 | workshop:alice | ni | 7 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u340 | 926 | u4.operation:52240cda21628aff89032656fa871bbc072a2acad9f696548b7027f4b3b7e4dc@2 | 598 | workshop:alice | fe | 8 | 4 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u341 | 926 | u4.operation:52240cda21628aff89032656fa871bbc072a2acad9f696548b7027f4b3b7e4dc@2 | 600 | workshop:alice | ni | 7 | 3 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u342 | 926 | u4.operation:52240cda21628aff89032656fa871bbc072a2acad9f696548b7027f4b3b7e4dc@2 | 604 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u343 | 926 | u4.operation:52240cda21628aff89032656fa871bbc072a2acad9f696548b7027f4b3b7e4dc@2 | 608 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u344 | 926 | u4.operation:52240cda21628aff89032656fa871bbc072a2acad9f696548b7027f4b3b7e4dc@2 | 611 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u345 | 926 | u4.operation:52240cda21628aff89032656fa871bbc072a2acad9f696548b7027f4b3b7e4dc@2 | 614 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u346 | 932 | u4.operation:2a659f9ad38f178c5ecd7632a45d5b9be5752f994160facdad84cdf80c4ade41@2 | 600 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u347 | 932 | u4.operation:2a659f9ad38f178c5ecd7632a45d5b9be5752f994160facdad84cdf80c4ade41@2 | 604 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u348 | 932 | u4.operation:2a659f9ad38f178c5ecd7632a45d5b9be5752f994160facdad84cdf80c4ade41@2 | 607 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u349 | 932 | u4.operation:2a659f9ad38f178c5ecd7632a45d5b9be5752f994160facdad84cdf80c4ade41@2 | 610 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u350 | 938 | u4.operation:54ea583c2ebd10466d8424f6d4f9e9589d6d509ffbef19c14f245150accee834@2 | 364 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u351 | 938 | u4.operation:54ea583c2ebd10466d8424f6d4f9e9589d6d509ffbef19c14f245150accee834@2 | 365 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u352 | 938 | u4.operation:54ea583c2ebd10466d8424f6d4f9e9589d6d509ffbef19c14f245150accee834@2 | 366 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u353 | 938 | u4.operation:54ea583c2ebd10466d8424f6d4f9e9589d6d509ffbef19c14f245150accee834@2 | 368 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u354 | 938 | u4.operation:54ea583c2ebd10466d8424f6d4f9e9589d6d509ffbef19c14f245150accee834@2 | 371 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u355 | 938 | u4.operation:54ea583c2ebd10466d8424f6d4f9e9589d6d509ffbef19c14f245150accee834@2 | 373 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u356 | 938 | u4.operation:54ea583c2ebd10466d8424f6d4f9e9589d6d509ffbef19c14f245150accee834@2 | 375 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u357 | 951 | u4.operation:a62c70fde80f86bc5bb05a3e0f1474002cb9286ba8b4abe01501fb608825840a@2 | 53 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | True | 0 |
| pair-solo8-seed-29 | u358 | 951 | u4.operation:a62c70fde80f86bc5bb05a3e0f1474002cb9286ba8b4abe01501fb608825840a@2 | 57 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | True | 0 |
| pair-solo8-seed-29 | u359 | 964 | u4.operation:80392dd682c2220b3962cfd086264dd730d9c897de8810d7f8eb7b2548a32b5b@2 | 46 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u360 | 964 | u4.operation:80392dd682c2220b3962cfd086264dd730d9c897de8810d7f8eb7b2548a32b5b@2 | 50 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u361 | 964 | u4.operation:80392dd682c2220b3962cfd086264dd730d9c897de8810d7f8eb7b2548a32b5b@2 | 53 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u362 | 964 | u4.operation:80392dd682c2220b3962cfd086264dd730d9c897de8810d7f8eb7b2548a32b5b@2 | 56 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u363 | 970 | u4.operation:16de824d1962de6a434d54c6ba6b7bd08d3fea5fece6ee4e21fcadf8e005ef7f@2 | 109 | workshop:alice | si | 5 | 1 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u364 | 980 | u4.operation:be3f73ec0acf3e282b4a8084b243bc386d5533f3eea3328772a4ba9bbc172ce2@2 | 614 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u365 | 980 | u4.operation:be3f73ec0acf3e282b4a8084b243bc386d5533f3eea3328772a4ba9bbc172ce2@2 | 618 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u366 | 980 | u4.operation:be3f73ec0acf3e282b4a8084b243bc386d5533f3eea3328772a4ba9bbc172ce2@2 | 622 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u367 | 980 | u4.operation:be3f73ec0acf3e282b4a8084b243bc386d5533f3eea3328772a4ba9bbc172ce2@2 | 625 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u368 | 980 | u4.operation:be3f73ec0acf3e282b4a8084b243bc386d5533f3eea3328772a4ba9bbc172ce2@2 | 628 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u369 | 986 | u4.operation:918e5d827b265435e0da6aea131773f3394f916da1a8831ffa5cfadc7a08b9b7@2 | 616 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u370 | 986 | u4.operation:918e5d827b265435e0da6aea131773f3394f916da1a8831ffa5cfadc7a08b9b7@2 | 620 | workshop:alice | si | 5 | 1 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u371 | 986 | u4.operation:918e5d827b265435e0da6aea131773f3394f916da1a8831ffa5cfadc7a08b9b7@2 | 623 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u372 | 986 | u4.operation:918e5d827b265435e0da6aea131773f3394f916da1a8831ffa5cfadc7a08b9b7@2 | 626 | workshop:alice | te | 6 | 2 | (workshop:bob) | world | True | 0 |
| pair-solo8-seed-29 | u373 | 992 | u4.operation:b61d7b7e4f2f0377bcb8844ec9a38af1e38e10a61b96422205ce9282034c1bcc@2 | 367 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u374 | 992 | u4.operation:b61d7b7e4f2f0377bcb8844ec9a38af1e38e10a61b96422205ce9282034c1bcc@2 | 368 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u375 | 992 | u4.operation:b61d7b7e4f2f0377bcb8844ec9a38af1e38e10a61b96422205ce9282034c1bcc@2 | 369 | workshop:bob | si | 1 | 4 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u376 | 992 | u4.operation:b61d7b7e4f2f0377bcb8844ec9a38af1e38e10a61b96422205ce9282034c1bcc@2 | 371 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u377 | 992 | u4.operation:b61d7b7e4f2f0377bcb8844ec9a38af1e38e10a61b96422205ce9282034c1bcc@2 | 374 | workshop:bob | fi | 6 | 2 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u378 | 992 | u4.operation:b61d7b7e4f2f0377bcb8844ec9a38af1e38e10a61b96422205ce9282034c1bcc@2 | 376 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | True | 0 |
| pair-solo8-seed-29 | u379 | 992 | u4.operation:b61d7b7e4f2f0377bcb8844ec9a38af1e38e10a61b96422205ce9282034c1bcc@2 | 378 | workshop:bob | te | 2 | 3 | (workshop:alice) | world | False | 0 |
| pair-solo8-seed-29 | u380 | 1005 | u4.operation:fac40ac05d295c4770d5386706f27c6b16042d9c6f752327227f8d0a7d9b7e61@2 | 53 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | True | 0 |
| pair-solo8-seed-29 | u381 | 1005 | u4.operation:fac40ac05d295c4770d5386706f27c6b16042d9c6f752327227f8d0a7d9b7e61@2 | 57 | workshop:alice | si | 5 | 1 | (workshop:bob) | self | False | 0 |
| pair-solo8-seed-29 | u382 | 1018 | u4.operation:f3f0bf5c24c314641d97f27ecd9e886876ce1ef45e6f6ed1db211e1aea281a8e@2 | 46 | workshop:bob | si | 1 | 4 | (workshop:alice) | (workshop:alice) | False | 0 |
| pair-solo8-seed-29 | u383 | 1018 | u4.operation:f3f0bf5c24c314641d97f27ecd9e886876ce1ef45e6f6ed1db211e1aea281a8e@2 | 50 | workshop:bob | ne | 5 | 1 | (workshop:alice) | (workshop:alice) | False | 0 |
| pair-solo8-seed-29 | u384 | 1018 | u4.operation:f3f0bf5c24c314641d97f27ecd9e886876ce1ef45e6f6ed1db211e1aea281a8e@2 | 53 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | True | 0 |
| pair-solo8-seed-29 | u385 | 1018 | u4.operation:f3f0bf5c24c314641d97f27ecd9e886876ce1ef45e6f6ed1db211e1aea281a8e@2 | 56 | workshop:bob | fi | 6 | 2 | (workshop:alice) | (workshop:alice) | False | 0 |
| pair-solo8-seed-29 | u386 | 1024 | u4.operation:1b5a8554470d796e9f48be283f8eba7dc65047f1138bd7182dece217900e4fa9@2 | 106 | workshop:alice | ne | 1 | 4 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u387 | 1024 | u4.operation:1b5a8554470d796e9f48be283f8eba7dc65047f1138bd7182dece217900e4fa9@2 | 109 | workshop:alice | se | 3 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u388 | 1024 | u4.operation:1b5a8554470d796e9f48be283f8eba7dc65047f1138bd7182dece217900e4fa9@2 | 112 | workshop:alice | se | 3 | 2 | (workshop:bob) | (workshop:bob) | True | 0 |
| pair-solo8-seed-29 | u389 | 1031 | u4.operation:2e51bb637596b09633a67d837a43a4d129ddf15e0cd03cfdc42f8478d9b9506d@2 | 18 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u390 | 1031 | u4.operation:2e51bb637596b09633a67d837a43a4d129ddf15e0cd03cfdc42f8478d9b9506d@2 | 19 | workshop:alice | fe | 8 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u391 | 1031 | u4.operation:2e51bb637596b09633a67d837a43a4d129ddf15e0cd03cfdc42f8478d9b9506d@2 | 21 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u392 | 1031 | u4.operation:2e51bb637596b09633a67d837a43a4d129ddf15e0cd03cfdc42f8478d9b9506d@2 | 23 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u393 | 1038 | u4.operation:a31f7e5d6a81356175d20815060b42ccf03d1ec6c887cb065bb4d86c3585c92c@2 | 17 | workshop:alice | fe | 8 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u394 | 1038 | u4.operation:a31f7e5d6a81356175d20815060b42ccf03d1ec6c887cb065bb4d86c3585c92c@2 | 19 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u395 | 1038 | u4.operation:a31f7e5d6a81356175d20815060b42ccf03d1ec6c887cb065bb4d86c3585c92c@2 | 22 | workshop:alice | se | 3 | 2 | self | world | True | 0 |
| pair-solo8-seed-29 | u396 | 1038 | u4.operation:a31f7e5d6a81356175d20815060b42ccf03d1ec6c887cb065bb4d86c3585c92c@2 | 23 | workshop:alice | ne | 1 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u397 | 1038 | u4.operation:a31f7e5d6a81356175d20815060b42ccf03d1ec6c887cb065bb4d86c3585c92c@2 | 24 | workshop:alice | ne | 1 | 4 | self | world | False | 0 |
| pair-solo8-seed-29 | u398 | 1045 | u4.operation:4dd840d13513ebf9f6f5d632723c361ce82d23bfad23cc57f7c59e125ac672aa@2 | 19 | workshop:alice | se | 3 | 2 | self | world | False | 0 |
| pair-solo8-seed-29 | u399 | 1045 | u4.operation:4dd840d13513ebf9f6f5d632723c361ce82d23bfad23cc57f7c59e125ac672aa@2 | 21 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u400 | 1045 | u4.operation:4dd840d13513ebf9f6f5d632723c361ce82d23bfad23cc57f7c59e125ac672aa@2 | 23 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u401 | 1048 | u4.operation:ff5ca0a19f2e4448f8a31eb9db7f6e48e2c2b627eaf61962070c36647e326ef3@2 | 44 | workshop:alice | fe | 8 | 4 | self | self | True | 0 |
| pair-solo8-seed-29 | u402 | 1048 | u4.operation:ff5ca0a19f2e4448f8a31eb9db7f6e48e2c2b627eaf61962070c36647e326ef3@2 | 47 | workshop:alice | te | 6 | 2 | self | self | True | 0 |
| pair-solo8-seed-29 | u403 | 1048 | u4.operation:ff5ca0a19f2e4448f8a31eb9db7f6e48e2c2b627eaf61962070c36647e326ef3@2 | 50 | workshop:alice | te | 6 | 2 | self | self | False | 0 |
| pair-solo8-seed-29 | u404 | 1055 | u4.operation:e0e4d113fdcfac2199ce120fe1a276c58d43dd4d153206b74cc4bb33bccc4a6d@2 | 17 | workshop:alice | fe | 8 | 4 | self | world | True | 0 |
| pair-solo8-seed-29 | u405 | 1055 | u4.operation:e0e4d113fdcfac2199ce120fe1a276c58d43dd4d153206b74cc4bb33bccc4a6d@2 | 19 | workshop:alice | ni | 7 | 3 | self | world | True | 0 |
| pair-solo8-seed-29 | u406 | 1055 | u4.operation:e0e4d113fdcfac2199ce120fe1a276c58d43dd4d153206b74cc4bb33bccc4a6d@2 | 21 | workshop:alice | ni | 7 | 3 | self | world | False | 0 |
| pair-solo8-seed-29 | u407 | 1058 | u4.operation:d24f52f2460a0f521cf2a5d8d4647617d9408e0f33147bcda6781e79b1734c43@2 | 44 | workshop:alice | fe | 8 | 4 | self | self | False | 0 |
| pair-solo8-seed-29 | u408 | 1058 | u4.operation:d24f52f2460a0f521cf2a5d8d4647617d9408e0f33147bcda6781e79b1734c43@2 | 48 | workshop:alice | ti | 4 | 1 | self | self | True | 0 |
| pair-solo8-seed-29 | u409 | 1058 | u4.operation:d24f52f2460a0f521cf2a5d8d4647617d9408e0f33147bcda6781e79b1734c43@2 | 52 | workshop:alice | ti | 4 | 1 | self | self | False | 0 |

Wide (A3/A4): any exact operation input counts, including collective evidence. A use counts once in its receiver profile and once per listed supplier in supplier/pair counts.
