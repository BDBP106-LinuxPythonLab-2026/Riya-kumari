#1
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO

# Given DNA sequence
plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")

# Create SeqRecord
record = SeqRecord(
    plasmid_seq,
    id="PLAB001",
    name="PLAB001",
    description="Cloning construct"
)

# Set molecule type
record.annotations["molecule_type"] = "DNA"

# Add BamHI feature (0-6)
bamhi = SeqFeature(
    FeatureLocation(0, 6),
    type="misc_feature",
    qualifiers={"note": "BamHI restriction site"}
)

# Add CDS feature (8-41)
cds = SeqFeature(
    FeatureLocation(8, 41),
    type="CDS",
    qualifiers={
        "gene": ["labA"],
        "translation": ["MASKGEELFT"]
    }
)

# Add EcoRI feature (41-47)
ecori = SeqFeature(
    FeatureLocation(41, 47),
    type="misc_feature",
    qualifiers={"note": "EcoRI restriction site"}
)

# Add features to record
record.features = [bamhi, cds, ecori]

# 2. Write to GenBank file
SeqIO.write(record, "lab construct.gb", "genbank")

print("GenBank file created successfully!")

