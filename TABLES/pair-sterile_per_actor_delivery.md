# Per-actor measures — Batch 6

Use IDs uN are zero-based occurrences in Batch 3's unchanged record sequence,
scoped to the History column. The use trace below links each to its committed
transaction, exact operation revision, and block completion boundary. Empty
ID lists mean zero observed uses, not missing histories. Inactive means zero
completed paid uses; such actors remain in population denominators.

**A1 source scope:** only non-empty actor tuples enter received-use measures.
Applied literally to both counts, the conditioning index is received weak-seat
uses / actor-sourced weak-seat uses: 1 whenever defined, N/A when empty.
This degeneracy follows A1; the original all-source denominator is not silently
substituted. A source-scope ruling is needed if that original ratio is intended.
Hold is kept received / received, across all seats. N/A denotes a zero denominator.
World and self are not received. World appears only in the use profile/trace
and all-use DCNH. No zero-denominator ratio is presented as zero.

## Actor indices

| History | Actor | TIM | Status | Conditioning (A1 literal) | Hold | Conditioning numerator and denominator IDs | Received IDs | Kept received IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | workshop:alice | eie | active | 40/40 = 1 | 71/75 = 71/75 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u196 |
| pair-sterile-seed-17 | workshop:bob | sli | active | 12/12 = 1 | 48/52 = 12/13 | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u171, u172, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-17 | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) | none | none | none |
| pair-sterile-seed-29 | workshop:alice | eie | active | 40/40 = 1 | 71/75 = 71/75 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u196 |
| pair-sterile-seed-29 | workshop:bob | sli | active | 12/12 = 1 | 48/52 = 12/13 | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u171, u172, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-29 | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) | none | none | none |
| pair-sterile-seed-43 | workshop:alice | eie | active | 40/40 = 1 | 71/75 = 71/75 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u196 |
| pair-sterile-seed-43 | workshop:bob | sli | active | 12/12 = 1 | 48/52 = 12/13 | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u171, u172, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-43 | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) | none | none | none |
| pair-sterile-seed-61 | workshop:alice | eie | active | 40/40 = 1 | 71/75 = 71/75 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u196 |
| pair-sterile-seed-61 | workshop:bob | sli | active | 12/12 = 1 | 48/52 = 12/13 | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u171, u172, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-61 | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) | none | none | none |

## Use profile

Only nonzero bins are printed; omitted (seat, source, kept) bins are zero.

| History | Actor | Seat | Source class | Kept | Count | Use IDs |
| --- | --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | workshop:alice | 2 | self | False | 1 | u0 |
| pair-sterile-seed-17 | workshop:alice | 3 | other | False | 1 | u193 |
| pair-sterile-seed-17 | workshop:alice | 3 | other | True | 19 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192 |
| pair-sterile-seed-17 | workshop:alice | 3 | self | True | 18 | u7, u8, u15, u16, u23, u24, u31, u32, u39, u40, u42, u43, u50, u51, u61, u62, u69, u70 |
| pair-sterile-seed-17 | workshop:alice | 4 | other | False | 1 | u197 |
| pair-sterile-seed-17 | workshop:alice | 4 | other | True | 19 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196 |
| pair-sterile-seed-17 | workshop:alice | 4 | self | True | 18 | u3, u4, u11, u12, u19, u20, u27, u28, u35, u36, u46, u47, u54, u55, u57, u58, u65, u66 |
| pair-sterile-seed-17 | workshop:alice | 6 | self | False | 1 | u1 |
| pair-sterile-seed-17 | workshop:alice | 7 | other | False | 1 | u194 |
| pair-sterile-seed-17 | workshop:alice | 7 | other | True | 17 | u80, u85, u88, u91, u99, u102, u107, u118, u123, u126, u129, u137, u140, u143, u183, u186, u191 |
| pair-sterile-seed-17 | workshop:alice | 7 | self | True | 16 | u6, u9, u14, u17, u22, u25, u30, u33, u38, u41, u44, u49, u52, u60, u63, u68 |
| pair-sterile-seed-17 | workshop:alice | 8 | other | False | 1 | u195 |
| pair-sterile-seed-17 | workshop:alice | 8 | other | True | 16 | u81, u84, u92, u95, u98, u103, u106, u119, u122, u130, u133, u136, u144, u182, u187, u190 |
| pair-sterile-seed-17 | workshop:alice | 8 | self | True | 17 | u2, u5, u10, u13, u18, u21, u26, u29, u34, u37, u45, u48, u53, u56, u59, u64, u67 |
| pair-sterile-seed-17 | workshop:bob | 1 | other | False | 1 | u181 |
| pair-sterile-seed-17 | workshop:bob | 1 | other | True | 17 | u74, u75, u112, u113, u149, u150, u155, u157, u160, u162, u163, u167, u168, u173, u175, u178, u180 |
| pair-sterile-seed-17 | workshop:bob | 2 | other | False | 1 | u177 |
| pair-sterile-seed-17 | workshop:bob | 2 | other | True | 21 | u71, u73, u76, u78, u79, u111, u114, u116, u117, u148, u151, u153, u154, u158, u159, u164, u166, u169, u171, u172, u176 |
| pair-sterile-seed-17 | workshop:bob | 5 | other | False | 1 | u179 |
| pair-sterile-seed-17 | workshop:bob | 5 | other | True | 3 | u156, u161, u174 |
| pair-sterile-seed-17 | workshop:bob | 6 | other | False | 1 | u170 |
| pair-sterile-seed-17 | workshop:bob | 6 | other | True | 7 | u72, u77, u110, u115, u147, u152, u165 |
| pair-sterile-seed-29 | workshop:alice | 2 | self | False | 1 | u0 |
| pair-sterile-seed-29 | workshop:alice | 3 | other | False | 1 | u193 |
| pair-sterile-seed-29 | workshop:alice | 3 | other | True | 19 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192 |
| pair-sterile-seed-29 | workshop:alice | 3 | self | True | 18 | u7, u8, u15, u16, u23, u24, u31, u32, u39, u40, u42, u43, u50, u51, u61, u62, u69, u70 |
| pair-sterile-seed-29 | workshop:alice | 4 | other | False | 1 | u197 |
| pair-sterile-seed-29 | workshop:alice | 4 | other | True | 19 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196 |
| pair-sterile-seed-29 | workshop:alice | 4 | self | True | 18 | u3, u4, u11, u12, u19, u20, u27, u28, u35, u36, u46, u47, u54, u55, u57, u58, u65, u66 |
| pair-sterile-seed-29 | workshop:alice | 6 | self | False | 1 | u1 |
| pair-sterile-seed-29 | workshop:alice | 7 | other | False | 1 | u194 |
| pair-sterile-seed-29 | workshop:alice | 7 | other | True | 17 | u80, u85, u88, u91, u99, u102, u107, u118, u123, u126, u129, u137, u140, u143, u183, u186, u191 |
| pair-sterile-seed-29 | workshop:alice | 7 | self | True | 16 | u6, u9, u14, u17, u22, u25, u30, u33, u38, u41, u44, u49, u52, u60, u63, u68 |
| pair-sterile-seed-29 | workshop:alice | 8 | other | False | 1 | u195 |
| pair-sterile-seed-29 | workshop:alice | 8 | other | True | 16 | u81, u84, u92, u95, u98, u103, u106, u119, u122, u130, u133, u136, u144, u182, u187, u190 |
| pair-sterile-seed-29 | workshop:alice | 8 | self | True | 17 | u2, u5, u10, u13, u18, u21, u26, u29, u34, u37, u45, u48, u53, u56, u59, u64, u67 |
| pair-sterile-seed-29 | workshop:bob | 1 | other | False | 1 | u181 |
| pair-sterile-seed-29 | workshop:bob | 1 | other | True | 17 | u74, u75, u112, u113, u149, u150, u155, u157, u160, u162, u163, u167, u168, u173, u175, u178, u180 |
| pair-sterile-seed-29 | workshop:bob | 2 | other | False | 1 | u177 |
| pair-sterile-seed-29 | workshop:bob | 2 | other | True | 21 | u71, u73, u76, u78, u79, u111, u114, u116, u117, u148, u151, u153, u154, u158, u159, u164, u166, u169, u171, u172, u176 |
| pair-sterile-seed-29 | workshop:bob | 5 | other | False | 1 | u179 |
| pair-sterile-seed-29 | workshop:bob | 5 | other | True | 3 | u156, u161, u174 |
| pair-sterile-seed-29 | workshop:bob | 6 | other | False | 1 | u170 |
| pair-sterile-seed-29 | workshop:bob | 6 | other | True | 7 | u72, u77, u110, u115, u147, u152, u165 |
| pair-sterile-seed-43 | workshop:alice | 2 | self | False | 1 | u0 |
| pair-sterile-seed-43 | workshop:alice | 3 | other | False | 1 | u193 |
| pair-sterile-seed-43 | workshop:alice | 3 | other | True | 19 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192 |
| pair-sterile-seed-43 | workshop:alice | 3 | self | True | 18 | u7, u8, u15, u16, u23, u24, u31, u32, u39, u40, u42, u43, u50, u51, u61, u62, u69, u70 |
| pair-sterile-seed-43 | workshop:alice | 4 | other | False | 1 | u197 |
| pair-sterile-seed-43 | workshop:alice | 4 | other | True | 19 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196 |
| pair-sterile-seed-43 | workshop:alice | 4 | self | True | 18 | u3, u4, u11, u12, u19, u20, u27, u28, u35, u36, u46, u47, u54, u55, u57, u58, u65, u66 |
| pair-sterile-seed-43 | workshop:alice | 6 | self | False | 1 | u1 |
| pair-sterile-seed-43 | workshop:alice | 7 | other | False | 1 | u194 |
| pair-sterile-seed-43 | workshop:alice | 7 | other | True | 17 | u80, u85, u88, u91, u99, u102, u107, u118, u123, u126, u129, u137, u140, u143, u183, u186, u191 |
| pair-sterile-seed-43 | workshop:alice | 7 | self | True | 16 | u6, u9, u14, u17, u22, u25, u30, u33, u38, u41, u44, u49, u52, u60, u63, u68 |
| pair-sterile-seed-43 | workshop:alice | 8 | other | False | 1 | u195 |
| pair-sterile-seed-43 | workshop:alice | 8 | other | True | 16 | u81, u84, u92, u95, u98, u103, u106, u119, u122, u130, u133, u136, u144, u182, u187, u190 |
| pair-sterile-seed-43 | workshop:alice | 8 | self | True | 17 | u2, u5, u10, u13, u18, u21, u26, u29, u34, u37, u45, u48, u53, u56, u59, u64, u67 |
| pair-sterile-seed-43 | workshop:bob | 1 | other | False | 1 | u181 |
| pair-sterile-seed-43 | workshop:bob | 1 | other | True | 17 | u74, u75, u112, u113, u149, u150, u155, u157, u160, u162, u163, u167, u168, u173, u175, u178, u180 |
| pair-sterile-seed-43 | workshop:bob | 2 | other | False | 1 | u177 |
| pair-sterile-seed-43 | workshop:bob | 2 | other | True | 21 | u71, u73, u76, u78, u79, u111, u114, u116, u117, u148, u151, u153, u154, u158, u159, u164, u166, u169, u171, u172, u176 |
| pair-sterile-seed-43 | workshop:bob | 5 | other | False | 1 | u179 |
| pair-sterile-seed-43 | workshop:bob | 5 | other | True | 3 | u156, u161, u174 |
| pair-sterile-seed-43 | workshop:bob | 6 | other | False | 1 | u170 |
| pair-sterile-seed-43 | workshop:bob | 6 | other | True | 7 | u72, u77, u110, u115, u147, u152, u165 |
| pair-sterile-seed-61 | workshop:alice | 2 | self | False | 1 | u0 |
| pair-sterile-seed-61 | workshop:alice | 3 | other | False | 1 | u193 |
| pair-sterile-seed-61 | workshop:alice | 3 | other | True | 19 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192 |
| pair-sterile-seed-61 | workshop:alice | 3 | self | True | 18 | u7, u8, u15, u16, u23, u24, u31, u32, u39, u40, u42, u43, u50, u51, u61, u62, u69, u70 |
| pair-sterile-seed-61 | workshop:alice | 4 | other | False | 1 | u197 |
| pair-sterile-seed-61 | workshop:alice | 4 | other | True | 19 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196 |
| pair-sterile-seed-61 | workshop:alice | 4 | self | True | 18 | u3, u4, u11, u12, u19, u20, u27, u28, u35, u36, u46, u47, u54, u55, u57, u58, u65, u66 |
| pair-sterile-seed-61 | workshop:alice | 6 | self | False | 1 | u1 |
| pair-sterile-seed-61 | workshop:alice | 7 | other | False | 1 | u194 |
| pair-sterile-seed-61 | workshop:alice | 7 | other | True | 17 | u80, u85, u88, u91, u99, u102, u107, u118, u123, u126, u129, u137, u140, u143, u183, u186, u191 |
| pair-sterile-seed-61 | workshop:alice | 7 | self | True | 16 | u6, u9, u14, u17, u22, u25, u30, u33, u38, u41, u44, u49, u52, u60, u63, u68 |
| pair-sterile-seed-61 | workshop:alice | 8 | other | False | 1 | u195 |
| pair-sterile-seed-61 | workshop:alice | 8 | other | True | 16 | u81, u84, u92, u95, u98, u103, u106, u119, u122, u130, u133, u136, u144, u182, u187, u190 |
| pair-sterile-seed-61 | workshop:alice | 8 | self | True | 17 | u2, u5, u10, u13, u18, u21, u26, u29, u34, u37, u45, u48, u53, u56, u59, u64, u67 |
| pair-sterile-seed-61 | workshop:bob | 1 | other | False | 1 | u181 |
| pair-sterile-seed-61 | workshop:bob | 1 | other | True | 17 | u74, u75, u112, u113, u149, u150, u155, u157, u160, u162, u163, u167, u168, u173, u175, u178, u180 |
| pair-sterile-seed-61 | workshop:bob | 2 | other | False | 1 | u177 |
| pair-sterile-seed-61 | workshop:bob | 2 | other | True | 21 | u71, u73, u76, u78, u79, u111, u114, u116, u117, u148, u151, u153, u154, u158, u159, u164, u166, u169, u171, u172, u176 |
| pair-sterile-seed-61 | workshop:bob | 5 | other | False | 1 | u179 |
| pair-sterile-seed-61 | workshop:bob | 5 | other | True | 3 | u156, u161, u174 |
| pair-sterile-seed-61 | workshop:bob | 6 | other | False | 1 | u170 |
| pair-sterile-seed-61 | workshop:bob | 6 | other | True | 7 | u72, u77, u110, u115, u147, u152, u165 |

## Weak-seat supplier map

Each dim <= 2 seat is listed, including empty supplier sets.

| History | Receiver | Seat | Supplier | Count | Use IDs |
| --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | workshop:alice | 3 | workshop:bob | 20 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192, u193 |
| pair-sterile-seed-17 | workshop:alice | 4 | workshop:bob | 20 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196, u197 |
| pair-sterile-seed-17 | workshop:alice | 5 | none | 0 | none |
| pair-sterile-seed-17 | workshop:alice | 6 | none | 0 | none |
| pair-sterile-seed-17 | workshop:bob | 3 | none | 0 | none |
| pair-sterile-seed-17 | workshop:bob | 4 | none | 0 | none |
| pair-sterile-seed-17 | workshop:bob | 5 | workshop:alice | 4 | u156, u161, u174, u179 |
| pair-sterile-seed-17 | workshop:bob | 6 | workshop:alice | 8 | u72, u77, u110, u115, u147, u152, u165, u170 |
| pair-sterile-seed-17 | workshop:eve | 3 | none | 0 | none |
| pair-sterile-seed-17 | workshop:eve | 4 | none | 0 | none |
| pair-sterile-seed-17 | workshop:eve | 5 | none | 0 | none |
| pair-sterile-seed-17 | workshop:eve | 6 | none | 0 | none |
| pair-sterile-seed-29 | workshop:alice | 3 | workshop:bob | 20 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192, u193 |
| pair-sterile-seed-29 | workshop:alice | 4 | workshop:bob | 20 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196, u197 |
| pair-sterile-seed-29 | workshop:alice | 5 | none | 0 | none |
| pair-sterile-seed-29 | workshop:alice | 6 | none | 0 | none |
| pair-sterile-seed-29 | workshop:bob | 3 | none | 0 | none |
| pair-sterile-seed-29 | workshop:bob | 4 | none | 0 | none |
| pair-sterile-seed-29 | workshop:bob | 5 | workshop:alice | 4 | u156, u161, u174, u179 |
| pair-sterile-seed-29 | workshop:bob | 6 | workshop:alice | 8 | u72, u77, u110, u115, u147, u152, u165, u170 |
| pair-sterile-seed-29 | workshop:eve | 3 | none | 0 | none |
| pair-sterile-seed-29 | workshop:eve | 4 | none | 0 | none |
| pair-sterile-seed-29 | workshop:eve | 5 | none | 0 | none |
| pair-sterile-seed-29 | workshop:eve | 6 | none | 0 | none |
| pair-sterile-seed-43 | workshop:alice | 3 | workshop:bob | 20 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192, u193 |
| pair-sterile-seed-43 | workshop:alice | 4 | workshop:bob | 20 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196, u197 |
| pair-sterile-seed-43 | workshop:alice | 5 | none | 0 | none |
| pair-sterile-seed-43 | workshop:alice | 6 | none | 0 | none |
| pair-sterile-seed-43 | workshop:bob | 3 | none | 0 | none |
| pair-sterile-seed-43 | workshop:bob | 4 | none | 0 | none |
| pair-sterile-seed-43 | workshop:bob | 5 | workshop:alice | 4 | u156, u161, u174, u179 |
| pair-sterile-seed-43 | workshop:bob | 6 | workshop:alice | 8 | u72, u77, u110, u115, u147, u152, u165, u170 |
| pair-sterile-seed-43 | workshop:eve | 3 | none | 0 | none |
| pair-sterile-seed-43 | workshop:eve | 4 | none | 0 | none |
| pair-sterile-seed-43 | workshop:eve | 5 | none | 0 | none |
| pair-sterile-seed-43 | workshop:eve | 6 | none | 0 | none |
| pair-sterile-seed-61 | workshop:alice | 3 | workshop:bob | 20 | u86, u87, u89, u90, u100, u101, u108, u109, u124, u125, u127, u128, u138, u139, u141, u142, u184, u185, u192, u193 |
| pair-sterile-seed-61 | workshop:alice | 4 | workshop:bob | 20 | u82, u83, u93, u94, u96, u97, u104, u105, u120, u121, u131, u132, u134, u135, u145, u146, u188, u189, u196, u197 |
| pair-sterile-seed-61 | workshop:alice | 5 | none | 0 | none |
| pair-sterile-seed-61 | workshop:alice | 6 | none | 0 | none |
| pair-sterile-seed-61 | workshop:bob | 3 | none | 0 | none |
| pair-sterile-seed-61 | workshop:bob | 4 | none | 0 | none |
| pair-sterile-seed-61 | workshop:bob | 5 | workshop:alice | 4 | u156, u161, u174, u179 |
| pair-sterile-seed-61 | workshop:bob | 6 | workshop:alice | 8 | u72, u77, u110, u115, u147, u152, u165, u170 |
| pair-sterile-seed-61 | workshop:eve | 3 | none | 0 | none |
| pair-sterile-seed-61 | workshop:eve | 4 | none | 0 | none |
| pair-sterile-seed-61 | workshop:eve | 5 | none | 0 | none |
| pair-sterile-seed-61 | workshop:eve | 6 | none | 0 | none |

## Use trace

Transaction and episode indices are zero-based.

| History | Use ID | Transaction | Operation revision | Block end | Actor | Element | Seat | Dim | Source | Kept | Episode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | u0 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 273 | workshop:alice | ni | 2 | 3 | self | False | 0 |
| pair-sterile-seed-17 | u1 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 276 | workshop:alice | se | 6 | 2 | self | False | 0 |
| pair-sterile-seed-17 | u2 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 277 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u3 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u4 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 285 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u5 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u6 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u7 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u8 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u9 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u10 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u11 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 290 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u12 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 294 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u13 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 295 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u14 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 297 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u15 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 300 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u16 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 303 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u17 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 272 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u18 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 273 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u19 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 277 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u20 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u21 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 282 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u22 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 284 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u23 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 287 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u24 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 290 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u25 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u26 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u27 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u28 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u29 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u30 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u31 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u32 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u33 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u34 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u35 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u36 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u37 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u38 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u39 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u40 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u41 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u42 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u43 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u44 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 296 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u45 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 297 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u46 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 301 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u47 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 305 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u48 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 288 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u49 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 290 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u50 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 293 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u51 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 296 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u52 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 298 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u53 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 299 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u54 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 303 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u55 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 307 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u56 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u57 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u58 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u59 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u60 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u61 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u62 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u63 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 319 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u64 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u65 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u66 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-17 | u67 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-17 | u68 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-17 | u69 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u70 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-17 | u71 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 253 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u72 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 256 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u73 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 258 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u74 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u75 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 260 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u76 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 262 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u77 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 265 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u78 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 267 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u79 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 269 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u80 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 354 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u81 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 355 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u82 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 359 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u83 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u84 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 364 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u85 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 366 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u86 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 369 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u87 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u88 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 321 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u89 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 324 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u90 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 327 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u91 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 329 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u92 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u93 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 334 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u94 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 338 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u95 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 321 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u96 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 325 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u97 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 329 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u98 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u99 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 332 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u100 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 335 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u101 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u102 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 323 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u103 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 324 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u104 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 328 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u105 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 332 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u106 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 333 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u107 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u108 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u109 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 341 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u110 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 255 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u111 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 257 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u112 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 258 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u113 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u114 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 261 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u115 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 264 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u116 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 266 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u117 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u118 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u119 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 336 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u120 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 340 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u121 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 344 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u122 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 345 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u123 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 347 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u124 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 350 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u125 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u126 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 350 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u127 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u128 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 356 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u129 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 358 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u130 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 359 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u131 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u132 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 367 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u133 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 356 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u134 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 360 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u135 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 364 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u136 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 365 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u137 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 367 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u138 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 370 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u139 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 373 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u140 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 369 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u141 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u142 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 375 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u143 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 377 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u144 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 378 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u145 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 382 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u146 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 386 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u147 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 262 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u148 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 264 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u149 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 265 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u150 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 266 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u151 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u152 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 271 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u153 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 273 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u154 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 275 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u155 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 272 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u156 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 276 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u157 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 277 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u158 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 279 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u159 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 281 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u160 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 282 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u161 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 286 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u162 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 287 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u163 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 288 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u164 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 286 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u165 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 289 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u166 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 291 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u167 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 292 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u168 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 293 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u169 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 295 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u170 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 298 | workshop:bob | fi | 6 | 2 | (workshop:alice) | False | 0 |
| pair-sterile-seed-17 | u171 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 300 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u172 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 302 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u173 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 300 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u174 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 304 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u175 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 305 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u176 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 307 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u177 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 309 | workshop:bob | te | 2 | 3 | (workshop:alice) | False | 0 |
| pair-sterile-seed-17 | u178 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 310 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u179 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 314 | workshop:bob | ne | 5 | 1 | (workshop:alice) | False | 0 |
| pair-sterile-seed-17 | u180 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 315 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-17 | u181 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 316 | workshop:bob | si | 1 | 4 | (workshop:alice) | False | 0 |
| pair-sterile-seed-17 | u182 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u183 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u184 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u185 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u186 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u187 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u188 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u189 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u190 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u191 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u192 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u193 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | False | 0 |
| pair-sterile-seed-17 | u194 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | False | 0 |
| pair-sterile-seed-17 | u195 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | False | 0 |
| pair-sterile-seed-17 | u196 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-17 | u197 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | False | 0 |
| pair-sterile-seed-29 | u0 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 273 | workshop:alice | ni | 2 | 3 | self | False | 0 |
| pair-sterile-seed-29 | u1 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 276 | workshop:alice | se | 6 | 2 | self | False | 0 |
| pair-sterile-seed-29 | u2 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 277 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u3 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u4 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 285 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u5 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u6 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u7 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u8 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u9 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u10 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u11 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 290 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u12 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 294 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u13 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 295 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u14 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 297 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u15 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 300 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u16 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 303 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u17 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 272 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u18 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 273 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u19 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 277 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u20 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u21 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 282 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u22 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 284 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u23 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 287 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u24 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 290 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u25 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u26 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u27 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u28 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u29 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u30 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u31 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u32 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u33 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u34 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u35 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u36 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u37 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u38 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u39 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u40 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u41 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u42 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u43 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u44 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 296 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u45 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 297 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u46 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 301 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u47 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 305 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u48 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 288 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u49 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 290 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u50 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 293 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u51 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 296 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u52 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 298 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u53 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 299 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u54 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 303 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u55 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 307 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u56 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u57 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u58 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u59 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u60 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u61 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u62 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u63 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 319 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u64 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u65 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u66 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-29 | u67 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-29 | u68 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-29 | u69 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u70 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-29 | u71 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 253 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u72 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 256 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u73 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 258 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u74 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u75 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 260 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u76 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 262 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u77 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 265 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u78 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 267 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u79 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 269 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u80 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 354 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u81 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 355 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u82 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 359 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u83 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u84 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 364 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u85 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 366 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u86 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 369 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u87 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u88 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 321 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u89 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 324 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u90 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 327 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u91 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 329 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u92 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u93 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 334 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u94 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 338 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u95 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 321 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u96 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 325 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u97 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 329 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u98 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u99 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 332 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u100 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 335 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u101 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u102 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 323 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u103 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 324 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u104 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 328 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u105 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 332 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u106 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 333 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u107 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u108 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u109 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 341 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u110 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 255 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u111 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 257 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u112 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 258 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u113 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u114 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 261 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u115 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 264 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u116 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 266 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u117 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u118 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u119 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 336 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u120 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 340 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u121 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 344 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u122 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 345 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u123 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 347 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u124 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 350 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u125 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u126 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 350 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u127 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u128 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 356 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u129 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 358 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u130 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 359 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u131 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u132 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 367 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u133 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 356 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u134 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 360 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u135 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 364 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u136 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 365 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u137 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 367 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u138 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 370 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u139 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 373 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u140 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 369 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u141 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u142 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 375 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u143 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 377 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u144 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 378 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u145 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 382 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u146 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 386 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u147 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 262 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u148 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 264 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u149 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 265 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u150 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 266 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u151 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u152 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 271 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u153 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 273 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u154 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 275 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u155 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 272 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u156 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 276 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u157 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 277 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u158 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 279 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u159 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 281 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u160 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 282 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u161 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 286 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u162 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 287 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u163 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 288 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u164 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 286 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u165 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 289 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u166 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 291 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u167 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 292 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u168 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 293 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u169 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 295 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u170 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 298 | workshop:bob | fi | 6 | 2 | (workshop:alice) | False | 0 |
| pair-sterile-seed-29 | u171 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 300 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u172 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 302 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u173 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 300 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u174 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 304 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u175 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 305 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u176 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 307 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u177 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 309 | workshop:bob | te | 2 | 3 | (workshop:alice) | False | 0 |
| pair-sterile-seed-29 | u178 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 310 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u179 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 314 | workshop:bob | ne | 5 | 1 | (workshop:alice) | False | 0 |
| pair-sterile-seed-29 | u180 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 315 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-29 | u181 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 316 | workshop:bob | si | 1 | 4 | (workshop:alice) | False | 0 |
| pair-sterile-seed-29 | u182 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u183 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u184 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u185 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u186 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u187 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u188 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u189 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u190 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u191 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u192 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u193 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | False | 0 |
| pair-sterile-seed-29 | u194 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | False | 0 |
| pair-sterile-seed-29 | u195 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | False | 0 |
| pair-sterile-seed-29 | u196 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-29 | u197 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | False | 0 |
| pair-sterile-seed-43 | u0 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 273 | workshop:alice | ni | 2 | 3 | self | False | 0 |
| pair-sterile-seed-43 | u1 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 276 | workshop:alice | se | 6 | 2 | self | False | 0 |
| pair-sterile-seed-43 | u2 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 277 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u3 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u4 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 285 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u5 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u6 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u7 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u8 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u9 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u10 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u11 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 290 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u12 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 294 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u13 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 295 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u14 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 297 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u15 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 300 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u16 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 303 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u17 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 272 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u18 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 273 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u19 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 277 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u20 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u21 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 282 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u22 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 284 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u23 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 287 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u24 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 290 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u25 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u26 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u27 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u28 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u29 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u30 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u31 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u32 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u33 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u34 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u35 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u36 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u37 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u38 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u39 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u40 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u41 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u42 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u43 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u44 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 296 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u45 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 297 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u46 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 301 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u47 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 305 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u48 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 288 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u49 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 290 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u50 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 293 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u51 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 296 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u52 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 298 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u53 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 299 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u54 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 303 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u55 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 307 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u56 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u57 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u58 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u59 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u60 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u61 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u62 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u63 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 319 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u64 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u65 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u66 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-43 | u67 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-43 | u68 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-43 | u69 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u70 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-43 | u71 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 253 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u72 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 256 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u73 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 258 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u74 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u75 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 260 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u76 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 262 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u77 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 265 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u78 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 267 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u79 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 269 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u80 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 354 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u81 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 355 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u82 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 359 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u83 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u84 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 364 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u85 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 366 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u86 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 369 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u87 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u88 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 321 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u89 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 324 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u90 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 327 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u91 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 329 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u92 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u93 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 334 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u94 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 338 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u95 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 321 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u96 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 325 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u97 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 329 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u98 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u99 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 332 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u100 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 335 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u101 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u102 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 323 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u103 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 324 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u104 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 328 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u105 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 332 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u106 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 333 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u107 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u108 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u109 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 341 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u110 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 255 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u111 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 257 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u112 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 258 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u113 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u114 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 261 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u115 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 264 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u116 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 266 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u117 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u118 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u119 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 336 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u120 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 340 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u121 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 344 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u122 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 345 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u123 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 347 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u124 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 350 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u125 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u126 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 350 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u127 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u128 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 356 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u129 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 358 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u130 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 359 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u131 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u132 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 367 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u133 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 356 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u134 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 360 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u135 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 364 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u136 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 365 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u137 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 367 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u138 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 370 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u139 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 373 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u140 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 369 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u141 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u142 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 375 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u143 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 377 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u144 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 378 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u145 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 382 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u146 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 386 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u147 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 262 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u148 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 264 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u149 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 265 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u150 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 266 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u151 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u152 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 271 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u153 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 273 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u154 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 275 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u155 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 272 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u156 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 276 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u157 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 277 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u158 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 279 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u159 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 281 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u160 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 282 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u161 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 286 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u162 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 287 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u163 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 288 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u164 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 286 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u165 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 289 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u166 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 291 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u167 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 292 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u168 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 293 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u169 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 295 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u170 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 298 | workshop:bob | fi | 6 | 2 | (workshop:alice) | False | 0 |
| pair-sterile-seed-43 | u171 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 300 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u172 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 302 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u173 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 300 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u174 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 304 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u175 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 305 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u176 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 307 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u177 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 309 | workshop:bob | te | 2 | 3 | (workshop:alice) | False | 0 |
| pair-sterile-seed-43 | u178 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 310 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u179 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 314 | workshop:bob | ne | 5 | 1 | (workshop:alice) | False | 0 |
| pair-sterile-seed-43 | u180 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 315 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-43 | u181 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 316 | workshop:bob | si | 1 | 4 | (workshop:alice) | False | 0 |
| pair-sterile-seed-43 | u182 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u183 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u184 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u185 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u186 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u187 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u188 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u189 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u190 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u191 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u192 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u193 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | False | 0 |
| pair-sterile-seed-43 | u194 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | False | 0 |
| pair-sterile-seed-43 | u195 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | False | 0 |
| pair-sterile-seed-43 | u196 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-43 | u197 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | False | 0 |
| pair-sterile-seed-61 | u0 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 273 | workshop:alice | ni | 2 | 3 | self | False | 0 |
| pair-sterile-seed-61 | u1 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 276 | workshop:alice | se | 6 | 2 | self | False | 0 |
| pair-sterile-seed-61 | u2 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 277 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u3 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u4 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 285 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u5 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u6 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u7 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u8 | 236 | u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u9 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u10 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 286 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u11 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 290 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u12 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 294 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u13 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 295 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u14 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 297 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u15 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 300 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u16 | 242 | u4.operation:3564a2d7519ad8c72dd7f45b6adbd0367319b5efedee8f164e7f7b99f0310da7@2 | 303 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u17 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 272 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u18 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 273 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u19 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 277 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u20 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 281 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u21 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 282 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u22 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 284 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u23 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 287 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u24 | 248 | u4.operation:a0d69968eb3d320fb5bc33d4575ae1a49b85ec799d73fc17d549d91cb9b37908@2 | 290 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u25 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u26 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u27 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u28 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u29 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u30 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u31 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u32 | 254 | u4.operation:b985c1abc59df94e5e7063c926337c6ea86b8c5b656c5b35dcaf3462ae52980d@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u33 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 273 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u34 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 274 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u35 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 278 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u36 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 282 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u37 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 283 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u38 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 285 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u39 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 288 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u40 | 257 | u4.operation:8986b61478200f3c497a5d73265a493e37856db709d3617e5b5fd2c55a008717@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u41 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 288 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u42 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 291 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u43 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 294 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u44 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 296 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u45 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 297 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u46 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 301 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u47 | 270 | u4.operation:730887a72377859c31a6321959a61cc8b56b096c247126925d5a702ed648a282@2 | 305 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u48 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 288 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u49 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 290 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u50 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 293 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u51 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 296 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u52 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 298 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u53 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 299 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u54 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 303 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u55 | 276 | u4.operation:6181c4504a384ddfabd6ac49984afc80e1318fa2ac6a5f411964238b6326b9d8@2 | 307 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u56 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u57 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u58 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u59 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u60 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u61 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u62 | 295 | u4.operation:3df139bb00af3adc2a71c65e7d2bc6bfdaa86ae58f9c1b781497bf00705f9df8@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u63 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 319 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u64 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 320 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u65 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 324 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u66 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 328 | workshop:alice | si | 4 | 1 | self | True | 0 |
| pair-sterile-seed-61 | u67 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 329 | workshop:alice | ne | 8 | 4 | self | True | 0 |
| pair-sterile-seed-61 | u68 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 331 | workshop:alice | fi | 7 | 3 | self | True | 0 |
| pair-sterile-seed-61 | u69 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 334 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u70 | 301 | u4.operation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@2 | 337 | workshop:alice | te | 3 | 2 | self | True | 0 |
| pair-sterile-seed-61 | u71 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 253 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u72 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 256 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u73 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 258 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u74 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u75 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 260 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u76 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 262 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u77 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 265 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u78 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 267 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u79 | 307 | u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a@2 | 269 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u80 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 354 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u81 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 355 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u82 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 359 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u83 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u84 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 364 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u85 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 366 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u86 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 369 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u87 | 316 | u4.operation:38e1f6b7fe6c80ff9951e8d7003b4a7ecad20614cb103f5e47bcc3f28f8f7e40@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u88 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 321 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u89 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 324 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u90 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 327 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u91 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 329 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u92 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u93 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 334 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u94 | 319 | u4.operation:03250f7ed3ec0dafbe2818ea76ae1810d8cd3daf1ef081bf2a5b8f17f6bd3c3d@2 | 338 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u95 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 321 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u96 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 325 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u97 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 329 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u98 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 330 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u99 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 332 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u100 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 335 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u101 | 325 | u4.operation:0891157b75b9355fc41d14c8e45ecdb21271feda7b0267f0c728facd5514ef5a@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u102 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 323 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u103 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 324 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u104 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 328 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u105 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 332 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u106 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 333 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u107 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u108 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 338 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u109 | 331 | u4.operation:ca6ae2f30656f682f479736a5f8d60c2b785bb6102ffc6dd182a2827f217250d@2 | 341 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u110 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 255 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u111 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 257 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u112 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 258 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u113 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 259 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u114 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 261 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u115 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 264 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u116 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 266 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u117 | 337 | u4.operation:29bba6db1a9fc6ccb2a84a2d5026d65f328bb1d33d6db432d4130a44992e1add@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u118 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 335 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u119 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 336 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u120 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 340 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u121 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 344 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u122 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 345 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u123 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 347 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u124 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 350 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u125 | 346 | u4.operation:5e6839c2a71456c4e6972e213cfab1be68a6121750d013a4275ce45e8972dec1@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u126 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 350 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u127 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 353 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u128 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 356 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u129 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 358 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u130 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 359 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u131 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 363 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u132 | 359 | u4.operation:89172c7307b8637912743c5da22f5ac078701d467ec531fa7d811aeb1aec1466@2 | 367 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u133 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 356 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u134 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 360 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u135 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 364 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u136 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 365 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u137 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 367 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u138 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 370 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u139 | 368 | u4.operation:5b0c4924e181795378aaa7da523ef14cfd9b11677500bbe401fa49e47f7c8b0b@2 | 373 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u140 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 369 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u141 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 372 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u142 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 375 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u143 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 377 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u144 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 378 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u145 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 382 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u146 | 381 | u4.operation:6ff31b7bb8527e35b63a70b236cd42d6f289d1a218a014a27c830d07b1ce3981@2 | 386 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u147 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 262 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u148 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 264 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u149 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 265 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u150 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 266 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u151 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 268 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u152 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 271 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u153 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 273 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u154 | 390 | u4.operation:63361e7c8c851448e8d469f99c6cd884ee1eff722b2c2fff4bd682bdbf02c4b1@2 | 275 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u155 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 272 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u156 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 276 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u157 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 277 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u158 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 279 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u159 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 281 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u160 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 282 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u161 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 286 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u162 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 287 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u163 | 407 | u4.operation:5a2fa789fa2474240da6f503913affe9bbb4f6555536485bbeb8d992e549de72@2 | 288 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u164 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 286 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u165 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 289 | workshop:bob | fi | 6 | 2 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u166 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 291 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u167 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 292 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u168 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 293 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u169 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 295 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u170 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 298 | workshop:bob | fi | 6 | 2 | (workshop:alice) | False | 0 |
| pair-sterile-seed-61 | u171 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 300 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u172 | 419 | u4.operation:2763434b2cbb6ad61f6cda8d3d78befd4bdb922ea0c214dcc3e98d279856f35f@2 | 302 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u173 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 300 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u174 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 304 | workshop:bob | ne | 5 | 1 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u175 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 305 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u176 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 307 | workshop:bob | te | 2 | 3 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u177 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 309 | workshop:bob | te | 2 | 3 | (workshop:alice) | False | 0 |
| pair-sterile-seed-61 | u178 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 310 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u179 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 314 | workshop:bob | ne | 5 | 1 | (workshop:alice) | False | 0 |
| pair-sterile-seed-61 | u180 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 315 | workshop:bob | si | 1 | 4 | (workshop:alice) | True | 0 |
| pair-sterile-seed-61 | u181 | 436 | u4.operation:ab839f9544022a19a7f701253817cc93fee412a83b69dafee697771e673d6e54@2 | 316 | workshop:bob | si | 1 | 4 | (workshop:alice) | False | 0 |
| pair-sterile-seed-61 | u182 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u183 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u184 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u185 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u186 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u187 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u188 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u189 | 442 | u4.operation:493dee748610e0d17c2be1a15c80a7c0993ce3f7e95d80557dbf07b06b0fa205@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u190 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 394 | workshop:alice | ne | 8 | 4 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u191 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 396 | workshop:alice | fi | 7 | 3 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u192 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 399 | workshop:alice | te | 3 | 2 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u193 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 402 | workshop:alice | te | 3 | 2 | (workshop:bob) | False | 0 |
| pair-sterile-seed-61 | u194 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 404 | workshop:alice | fi | 7 | 3 | (workshop:bob) | False | 0 |
| pair-sterile-seed-61 | u195 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 405 | workshop:alice | ne | 8 | 4 | (workshop:bob) | False | 0 |
| pair-sterile-seed-61 | u196 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 409 | workshop:alice | si | 4 | 1 | (workshop:bob) | True | 0 |
| pair-sterile-seed-61 | u197 | 445 | u4.operation:0847e534019d02c974375ebdff6f36ae683216cc16ad1ba47a3486a8a7ce4f3d@2 | 413 | workshop:alice | si | 4 | 1 | (workshop:bob) | False | 0 |

A3/A4: any exact operation input counts, including collective evidence. A use counts once in its receiver profile and once per listed supplier in supplier/pair counts.
