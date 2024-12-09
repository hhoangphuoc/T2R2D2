from tqdm import tqdm
import argparse
import shutil
import glob
import os
import librosa
import soundfile as sf

parser = argparse.ArgumentParser()
parser.add_argument("--datasource", type=str, default='../../../data/r2d2/', help="data source of R2D2 dataset")
parser.add_argument("--outdir", type=str, default='../data_specs/', help="output directory storing the processed data")
args = parser.parse_args()
print(args)

# Gets the audio seperated wavs of a specific instrument from the URMP dataset
def get_r2d2_ins(ins):
    return glob.glob(args.datasource + '**'+ins+'*.wav', recursive = True)

# Saves wavs belonging to speaker from list of speaker files
def r2d2_prep_wavs(outdir, audio_files, audio_type, sample_rate = 16000):
    os.makedirs(outdir, exist_ok=True)
    for f in tqdm(audio_files, desc="extracting audio for  %s"%audio_type):
        # shutil.copy(f, outdir)
        # resample the audio to the target sample rate
        audio, sr = librosa.load(f, sr=sample_rate)

        if sr != sample_rate:
            audio = librosa.resample(audio, sr, sample_rate)
        sf.write(outdir + f.split('/')[-1], audio, sr)

# trumpet_files = get_audiosep_ins('tpt')

# Data preparation
r2d2_files = get_r2d2_ins('r2d2')
r2d2_prep_wavs(args.outdir+'r2d2', r2d2_files, 'r2d2')