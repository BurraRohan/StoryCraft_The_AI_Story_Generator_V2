document.addEventListener('DOMContentLoaded', () => {
    // --- State ---
    let currentStoryText = '';
    let isStoryGenerated = false;
    const availableGenres = ['Fantasy', 'Sci-Fi', 'Mystery', 'Adventure', 'Comedy', 'Horror', 'Thriller', 'Romance', 'Historical','Period-film','psychological','Action'];
    let selectedGenres = [];

    // --- DOM Element References ---
    const topicInput = document.getElementById('topic');
    const certificationBoardSelect = document.getElementById('certificationBoard');
    const generateBtn = document.getElementById('generateBtn');
    const clearBtn = document.getElementById('clearBtn');
    const btnText = document.getElementById('btn-text');
    const loader = document.getElementById('loader');
    const loaderText = document.getElementById('loader-text');
    const errorContainer = document.getElementById('errorContainer');
    const storySection = document.getElementById('storySection');
    const placeholderSection = document.getElementById('placeholderSection');
    const storyOutput = document.getElementById('storyOutput');
    const certificationOutput = document.getElementById('certificationOutput');
    const genreMultiselect = document.getElementById('genre-multiselect');
    const genreSelectTrigger = document.getElementById('genre-select-trigger');
    const genreSelectText = document.getElementById('genre-select-text');
    const genreOptionsContainer = document.getElementById('genre-options');
    const selectedGenresContainer = document.getElementById('selected-genres-container');

    // --- Genre Multiselect Logic ---
    function toggleGenre(genre) {
        const index = selectedGenres.indexOf(genre);
        if (index > -1) selectedGenres.splice(index, 1);
        else selectedGenres.push(genre);
        updateSelectedGenresUI();
    }

    function updateSelectedGenresUI() {
        selectedGenresContainer.innerHTML = '';
        selectedGenres.forEach(genre => {
            const tag = document.createElement('div');
            tag.className = 'genre-tag';
            tag.innerHTML = `<span>${genre}</span><span class="genre-tag-close" data-genre="${genre}"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></span>`;
            selectedGenresContainer.appendChild(tag);
        });
        genreSelectText.textContent = selectedGenres.length === 0 ? 'Select one or more genres...' : `${selectedGenres.length} genre(s) selected`;
        genreSelectText.style.color = selectedGenres.length === 0 ? '#9ca3af' : 'white';
        document.querySelectorAll('#genre-options .multiselect-option input').forEach(checkbox => {
            checkbox.checked = selectedGenres.includes(checkbox.parentElement.dataset.genre);
        });
    }

    function initializeGenreDropdown() {
        availableGenres.forEach(genre => {
            const option = document.createElement('div');
            option.className = 'multiselect-option';
            option.dataset.genre = genre;
            option.innerHTML = `<input type="checkbox"><span class="ml-3">${genre}</span>`;
            option.addEventListener('click', (e) => {
                e.stopPropagation();
                toggleGenre(genre);
            });
            genreOptionsContainer.appendChild(option);
        });
    }

    // --- UI Update Functions ---
    const displayError = (message) => {
        errorContainer.innerHTML = `<strong>Oops! </strong><span>${message}</span>`;
        errorContainer.classList.remove('hidden');
    };

    const updateGenerateButtonUI = () => {
        if (isStoryGenerated) {
            btnText.textContent = 'Regenerate';
            generateBtn.classList.remove('btn-primary');
            generateBtn.classList.add('btn-secondary');
        } else {
            btnText.textContent = 'Generate Story';
            generateBtn.classList.remove('btn-secondary');
            generateBtn.classList.add('btn-primary');
        }
    };

    const setLoadingState = (isLoading) => {
        generateBtn.disabled = isLoading;
        clearBtn.disabled = isLoading;
        loader.style.display = isLoading ? 'flex' : 'none';
        btnText.style.display = isLoading ? 'none' : 'inline';
        loaderText.textContent = isStoryGenerated ? 'Regenerating...' : 'Weaving...';
    };

    // --- Main Logic Functions ---
    const handleGenerateStory = async () => {
        const topic = topicInput.value;
        if (!topic.trim()) return displayError('Please enter a topic for the story.');
        if (selectedGenres.length === 0) return displayError('Please select at least one genre.');

        setLoadingState(true);
        errorContainer.classList.add('hidden');
        placeholderSection.classList.add('hidden');
        storySection.classList.remove('hidden');
        storyOutput.innerHTML = '<p>The magic is happening...</p>';
        certificationOutput.innerHTML = '<p>Analyzing for rating...</p>';

        try {
            const response = await fetch('http://127.0.0.1:5000/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    topic: topic,
                    genres: selectedGenres,
                    board: certificationBoardSelect.value
                })
            });

            if (!response.ok) throw new Error(`Server responded with status: ${response.status}`);
            
            const data = await response.json();
            if (data.error) throw new Error(data.error);

            currentStoryText = data.story;
            storyOutput.innerHTML = `<p>${data.story}</p>`;
            certificationOutput.innerHTML = `<p>${data.certification.replace(/\n/g, '<br>')}</p>`;
            isStoryGenerated = true;

        } catch (err) {
            console.error("Error during generation:", err);
            displayError(err.message);
            isStoryGenerated = false;
        } finally {
            setLoadingState(false);
            updateGenerateButtonUI();
        }
    };

    const handleCertification = async () => {
        if (!currentStoryText) return;
        certificationOutput.innerHTML = '<p>Analyzing for rating...</p>';
        try {
            const response = await fetch('http://127.0.0.1:5000/certify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    story: currentStoryText,
                    board: certificationBoardSelect.value
                })
            });
            if (!response.ok) throw new Error(`Server responded with status: ${response.status}`);
            const data = await response.json();
            if (data.error) throw new Error(data.error);
            certificationOutput.innerHTML = `<p>${data.certification.replace(/\n/g, '<br>')}</p>`;
        } catch (err) {
            console.error("Error during certification:", err);
            certificationOutput.innerHTML = `<p style="color: #f87171;">Could not get rating: ${err.message}</p>`;
        }
    };

    const handleClear = () => {
        topicInput.value = '';
        currentStoryText = '';
        selectedGenres = [];
        isStoryGenerated = false;
        updateSelectedGenresUI();
        updateGenerateButtonUI();
        storySection.classList.add('hidden');
        placeholderSection.classList.remove('hidden');
        errorContainer.classList.add('hidden');
    };

    // --- Initial Setup & Event Listeners ---
    initializeGenreDropdown();
    generateBtn.addEventListener('click', handleGenerateStory);
    clearBtn.addEventListener('click', handleClear);
    certificationBoardSelect.addEventListener('change', handleCertification);

    genreSelectTrigger.addEventListener('click', () => genreOptionsContainer.classList.toggle('show'));
    document.addEventListener('click', (e) => {
        if (!genreMultiselect.contains(e.target)) genreOptionsContainer.classList.remove('show');
    });
    selectedGenresContainer.addEventListener('click', (e) => {
        if (e.target.closest('.genre-tag-close')) {
            toggleGenre(e.target.closest('.genre-tag-close').dataset.genre);
        }
    });
});
