const startScreen = document.querySelector('#startScreen');
const briefingScreen = document.querySelector('#briefingScreen');
const startButton = document.querySelector('#startButton');
const enterButton = document.querySelector('#enterButton');
const boardScreen = document.querySelector('#boardScreen');
const evidenceNoteButton = document.querySelector('#evidenceNoteButton');
const evidenceNoteScreen = document.querySelector('#evidenceNoteScreen');
const closeEvidenceNoteButton = document.querySelector('#closeEvidenceNoteButton');
const caseMusic = document.querySelector('#caseMusic');

const evidenceFiles = {
  cassette: { name: '낡은 카세트테이프', clue: '23:49에 녹음된 의문의 음성이 남아 있다.', image: 'Evidence/스크린샷 2026-08-26 203030.png', accent: true },
  footprint: { name: '희미한 발자국', clue: '약 270mm. 보관실 안쪽을 향한다.', image: 'Evidence/스크린샷 2026-08-26 203034.png' },
  lock: { name: '낡은 잠금장치', clue: '안쪽에서도 잠글 수 있다. 최근 긁힌 흔적.', image: 'Evidence/스크린샷 2026-08-26 203037.png' },
  schedule: { name: '직원 근무표', clue: '서준호의 근무 종료 시간은 23:30.', image: 'Evidence/스크린샷 2026-08-26 203045.png' },
  torn_note: { name: '찢어진 메모', clue: '"...목격자가 되어서는 안 됐다."', image: 'Evidence/스크린샷 2026-08-26 203055.png', accent: true },
  cigarette: { name: '낯선 담배꽁초', clue: '외부인의 개입 가능성. 보조 단서.', image: 'Evidence/스크린샷 2026-08-26 203100.png', faded: true }
};
const noteGrid = document.querySelector('#noteGrid');
const noteCount = document.querySelector('#noteCount');
let collectedEvidence = JSON.parse(localStorage.getItem('collectedEvidence') || '[]');

function renderEvidenceNote() {
  noteGrid.innerHTML = '';
  if (!collectedEvidence.length) {
    noteGrid.innerHTML = '<p class="note-empty">아직 기록된 증거가 없습니다.<br><small>현장에서 증거 사진을 조사하면 이곳에 추가됩니다.</small></p>';
  } else {
    collectedEvidence.forEach((id, index) => {
      const evidence = evidenceFiles[id];
      if (!evidence) return;
      const item = document.createElement('article');
      item.className = `note-item${evidence.accent ? ' note-item--red' : ''}${evidence.faded ? ' note-item--faded' : ''}`;
      item.innerHTML = `<img src="${evidence.image}" alt="${evidence.name}"><span>단서 ${String(index + 1).padStart(2, '0')}</span><h3>${evidence.name}</h3><p>${evidence.clue}</p>`;
      noteGrid.appendChild(item);
    });
  }
  noteCount.textContent = `발견한 단서 ${collectedEvidence.length} / 6`;
}

// 조사 화면에서 window.collectEvidence('cassette')를 호출하면 노트에 추가됩니다.
window.collectEvidence = (evidenceId) => {
  if (!evidenceFiles[evidenceId] || collectedEvidence.includes(evidenceId)) return;
  collectedEvidence.push(evidenceId);
  localStorage.setItem('collectedEvidence', JSON.stringify(collectedEvidence));
  renderEvidenceNote();
};

renderEvidenceNote();

startButton.addEventListener('click', () => {
  caseMusic.volume = 0.42;
  caseMusic.play().catch(() => {});
  startScreen.classList.add('is-hidden');
  briefingScreen.classList.add('is-visible');
  briefingScreen.setAttribute('aria-hidden', 'false');
});

enterButton.addEventListener('click', () => {
  enterButton.textContent = '수사 기록을 여는 중...';
  enterButton.disabled = true;
  briefingScreen.classList.remove('is-visible');
  briefingScreen.classList.add('is-hidden');
  briefingScreen.setAttribute('aria-hidden', 'true');
  boardScreen.classList.add('is-visible');
  boardScreen.setAttribute('aria-hidden', 'false');
});

evidenceNoteButton.addEventListener('click', () => {
  boardScreen.classList.remove('is-visible');
  boardScreen.classList.add('is-hidden');
  boardScreen.setAttribute('aria-hidden', 'true');
  evidenceNoteScreen.classList.add('is-visible');
  evidenceNoteScreen.setAttribute('aria-hidden', 'false');
  closeEvidenceNoteButton.focus();
});

closeEvidenceNoteButton.addEventListener('click', () => {
  boardScreen.classList.remove('is-hidden');
  boardScreen.classList.add('is-visible');
  boardScreen.setAttribute('aria-hidden', 'false');
  evidenceNoteScreen.classList.remove('is-visible');
  evidenceNoteScreen.setAttribute('aria-hidden', 'true');
  evidenceNoteButton.focus();
});
