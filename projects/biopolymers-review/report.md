# Biopolymers: Structure, Properties, and the Limits of the "Green" Label

*CM3254 Project Report · [Author 1, Matric No.] · [Author 2, Matric No.] · [Date]*

> **AI Tool Declaration** — *(final wording to be added on the first page before submission)*

<!-- STATUS: §1–§2 first draft. Citation numbers are placeholders in order of first
     appearance and will be renumbered once the full reference list is fixed.
     Every <!-- VERIFY --> marker must be resolved against the primary source before submission. -->

---

## 1. Introduction and Definitions

### 1.1 Why biopolymers, and why the discussion is louder than the tonnage

Global production of plastics reached 435 million tonnes (Mt) in 2020 and, in the absence of
additional policy intervention, is projected to grow by roughly 70 % by 2040, while only about 9 %
of plastic waste is recycled worldwide [1]. Against this background, polymers derived from
renewable biological feedstocks are routinely presented as the structural answer to the plastics
problem. The production statistics do not yet support that framing. Global bioplastics capacity
stood at 2.31 Mt in 2025 — of which 1.67 Mt was actually produced, at an average utilisation rate
of 72 % — and is forecast to reach 4.69 Mt by 2030 [2]. Even the 2030 figure represents
approximately 1 % of current global plastics output.

This mismatch defines the perspective taken in this review. Biopolymers are not, on any credible
projection, a volumetric substitute for fossil-derived commodity plastics within the next decade.
The case for them must therefore be made where it is actually strong: in applications where
end-of-life leakage into the environment is unavoidable, where biological function or
biocompatibility is required, or where the molecular architecture delivers properties that
synthetic chemistry reproduces only with difficulty. The remainder of this report examines the
structures that generate those properties, the limitations that follow from the same structures,
and the evidence behind the sustainability claims attached to this class of materials.

### 1.2 Three independent questions that the prefix "bio-" conflates

Much of the confusion in both the popular and the technical literature arises because a single
prefix is made to answer three logically independent questions [3]:

**(i) Where does the carbon come from?** A *bio-based* polymer contains carbon fixed from
contemporary biomass rather than from fossil sources. This is a measurable quantity, not a
qualitative claim: the bio-based carbon content is determined by the ¹⁴C radiocarbon method
specified in ASTM D6866 and ISO 16620 [4,5]. It says nothing whatsoever about how the material
behaves at end of life.

**(ii) How is the polymer made?** *Biopolymers* in the strict IUPAC sense are macromolecules
synthesised by living organisms — polysaccharides, proteins, nucleic acids, polyisoprene and
lignin [3]. A second group is produced by chemical polymerisation of monomers obtained from
biomass; poly(lactic acid) (PLA) is the leading example and is, strictly speaking, a synthetic
polymer made from a biological monomer. A third group, exemplified by polyhydroxyalkanoates
(PHAs), is polymerised inside microbial cells and is biological in both senses.
<!-- VERIFY: exact IUPAC wording of "biopolymer" and "bio-based polymer" in Vert et al. 2012;
     the IUPAC document (PAC 84:377-410) could not be retrieved in this environment. -->

**(iii) What happens to it at end of life?** *Biodegradation* is the conversion of a material to
CO₂, water and biomass by micro-organisms; crucially, it is a property of the material **and its
environment together**, never of the material alone [3]. *Compostable* is the narrowest and the
only operationally defined term of the three: certification under EN 13432, ASTM D6400 or ISO
17088 requires ≥ 90 % mineralisation within 180 days and disintegration to ≤ 10 % residue on a
2 mm sieve within 12 weeks under controlled thermophilic composting, together with ecotoxicity
and heavy-metal limits [6–8]. Compostability is thus a strict subset of biodegradability, itself
qualified by environment; neither is implied by a bio-based origin.

Four materials make the independence of these axes concrete, and they are used as reference
points throughout this report. Bio-based polyethylene (bio-PE), polymerised from sugarcane
ethanol, is fully bio-based and not biodegradable — chemically it is polyethylene. Poly(butylene
adipate-*co*-terephthalate) (PBAT) is fossil-derived and certified compostable. PLA is bio-based
and compostable only under industrial thermophilic conditions, degrading negligibly in seawater or
ambient soil [9]. PHAs are bio-based and biodegrade in a broad range of environments including
marine water [10]. Figure 1 places these and related materials on the three axes.

*[Figure 1 — Venn diagram: bio-based / biodegradable / compostable, with materials placed]*

### 1.3 Scope

This review covers the principal families of biopolymers, organised by backbone chemistry;
their molecular weight characteristics and the difficulty of measuring them; processing; a
critical comparison with synthetic commodity polymers; applications; and the current state of
the art. Selected results from computational chemistry are used where they explain
structure–property relationships that experiment alone leaves ambiguous.

---

## 2. Classification

Biopolymers are commonly classified by origin, and that classification is useful for
understanding supply chains, but it is a poor predictor of material behaviour. This review
therefore uses origin as the secondary axis and backbone chemistry as the primary one.

### 2.1 By origin

- **Extracted directly from biomass** — cellulose, starch, chitin, alginate, pectin, collagen,
  zein, lignin, natural rubber. Available at very large tonnage; structurally heterogeneous
  because the source organism, harvest and extraction route all vary.
- **Synthesised by micro-organisms** — PHAs, bacterial cellulose, xanthan, poly(γ-glutamic acid).
  Structurally the most controllable of the three groups, since copolymer composition can be set
  by the feed; also the most expensive, because fermentation and downstream recovery dominate
  cost.
- **Chemically polymerised from bio-based monomers** — PLA, poly(butylene succinate) (PBS),
  poly(ethylene furanoate) (PEF), bio-PE, bio-PET. Conventional polymer chemistry applies, so
  molecular weight and dispersity are controllable, and the resulting materials are drop-in
  compatible with existing processing equipment.

### 2.2 By backbone chemistry — the axis used in this review

The linkage that repeats along the chain governs the two behaviours that matter most in practice:
whether the polymer can be melt-processed, and by what mechanism it degrades.

| Backbone class | Repeating linkage | Representative materials | Consequence |
|---|---|---|---|
| Polysaccharide | glycosidic (acetal) | cellulose, starch, chitin/chitosan, alginate | dense hydrogen bonding; decomposition before melting; enzymatic, not simple hydrolytic, breakdown |
| Polyester | ester | PHB, PHBV, PLA, PBS | melt-processable; hydrolysis is the dominant degradation route, and it is autocatalytic |
| Polypeptide | amide | silk fibroin, collagen/gelatin, zein | sequence-defined, monodisperse; proteolytic degradation |
| Polynucleotide | phosphodiester | DNA, RNA | information-carrying; niche materials applications |
| Polyphenolic | ether (β-O-4) and C–C | lignin | amorphous, irregular, cross-linked; recalcitrant |
| Polyisoprene | C–C | natural rubber | elastomeric; strain-induced crystallisation |

*[Figure 2 — Classification tree: origin × backbone chemistry]*

Section 3 follows this classification, and the same colour coding is used in all figures.

---

## References *(working list — grows as sections are drafted)*

1. OECD. *Global Plastics Outlook: Economic Drivers, Environmental Impacts and Policy Options*.
   OECD Publishing, Paris, 2022. <!-- VERIFY page/figure for the 435 Mt and 9 % values -->
2. European Bioplastics / nova-Institute. *Bioplastics Market Development Update 2025*. Berlin,
   2025. <!-- VERIFY: 2.31 Mt capacity, 1.67 Mt produced, 72 % utilisation, 4.69 Mt by 2030 -->
3. Vert, M.; Doi, Y.; Hellwich, K.-H.; Hess, M.; Hodge, P.; Kubisa, P.; Rinaudo, M.; Schué, F.
   Terminology for biorelated polymers and applications (IUPAC Recommendations 2012).
   *Pure Appl. Chem.* **2012**, *84*, 377–410. DOI: 10.1351/PAC-REC-10-12-04.
4. ASTM D6866. *Standard Test Methods for Determining the Biobased Content of Solid, Liquid, and
   Gaseous Samples Using Radiocarbon Analysis.*
5. ISO 16620. *Plastics — Biobased content.*
6. EN 13432:2000. *Packaging — Requirements for packaging recoverable through composting and
   biodegradation.*
7. ASTM D6400-19. *Standard Specification for Labeling of Plastics Designed to be Aerobically
   Composted in Municipal or Industrial Facilities.*
8. ISO 17088. *Plastics — Organic recycling — Specifications for compostable plastics.*
9. *[to add: primary study on PLA degradation in seawater / ambient soil]*
10. *[to add: primary study on PHA marine biodegradation]*
