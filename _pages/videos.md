---
title: "Videos"
permalink: /videos/
layout: single
classes: wide
header:
  overlay_image: /assets/images/HERB-pose.jpg
---

<p>
  Visit the <a href="https://www.youtube.com/@PRL_HERB" target="_blank">YouTube channel</a> for more content.
</p>

<div class="video-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5em; margin-top: 2em;">

{% for video in site.data.videos %}
<div class="video-card" style="cursor: pointer; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s, box-shadow 0.2s;" 
     data-video-id="{{ video.id }}"
     data-video-title="{{ video.title | escape }}"
     data-video-description="{{ video.description | escape }}"
     data-video-channel="{{ video.channel_title | escape }}"
     data-video-date="{{ video.published_at | date: "%B %d, %Y" }}"
     onclick="openVideoModalFromCard(this)"
     onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 8px rgba(0,0,0,0.15)'"
     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.1)'">

  <div class="video-thumbnail" style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; background-color: #f0f0f0;">
    {% if video.thumbnail_url and video.thumbnail_url != "" %}
      <img src="{{ video.thumbnail_url | escape }}" alt="{{ video.title | escape }}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;" loading="lazy">
    {% else %}
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: #ddd; display: flex; align-items: center; justify-content: center; color: #666; font-size: 14px; text-align: center; padding: 1em;">
        <div>
          <div style="font-size: 24px; margin-bottom: 0.5em;">📹</div>
          <div>{{ video.title | truncate: 50 }}</div>
        </div>
      </div>
    {% endif %}
    <div class="play-button" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background-color: rgba(0,0,0,0.8); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px;">
      ▶
    </div>
  </div>

  <div class="video-info" style="padding: 1em;">
    <h3 class="video-title" style="margin: 0 0 0.5em 0; font-size: 1.1em; line-height: 1.3; color: #333; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
      {{ video.title }}
    </h3>
    
    <div class="video-meta" style="font-size: 0.85em; color: #666;">
      {% if video.channel_title %}
        <strong>{{ video.channel_title }}</strong> • 
      {% endif %}
      {{ video.published_at | date: "%b %d, %Y" }}
    </div>
  </div>

</div>
{% endfor %}

</div>

<!-- Video Modal -->
<div id="videoModal" style="display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.8);">
  <div class="modal-content" style="position: relative; background-color: #fff; margin: 2% auto; padding: 0; width: 90%; max-width: 900px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
    
    <div class="modal-header" style="padding: 1.5em; border-bottom: 1px solid #eee;">
      <h2 id="modalTitle" style="margin: 0; color: #333; font-size: 1.3em; line-height: 1.3;"></h2>
      <div id="modalMeta" style="font-size: 0.9em; color: #666; margin-top: 0.5em;"></div>
      <span class="close" onclick="closeVideoModal()" style="position: absolute; top: 1em; right: 1.5em; font-size: 28px; font-weight: bold; color: #aaa; cursor: pointer; line-height: 1;">&times;</span>
    </div>
    
    <div class="modal-body" style="padding: 0;">
      <div id="modalPlayer" style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
        <!-- YouTube iframe will be inserted here -->
      </div>
    </div>
    
    <div class="modal-footer" style="padding: 1.5em; border-top: 1px solid #eee;">
      <div id="modalDescription" style="color: #555; line-height: 1.5; font-size: 0.95em;"></div>
      <div style="margin-top: 1em; text-align: right;">
        <a id="modalYouTubeLink" href="#" target="_blank" class="btn btn--primary btn--small">Watch on YouTube</a>
      </div>
    </div>
    
  </div>
</div>

<script>
function openVideoModalFromCard(card) {
  const videoId = card.getAttribute('data-video-id');
  const title = card.getAttribute('data-video-title');
  const description = card.getAttribute('data-video-description');
  const channelTitle = card.getAttribute('data-video-channel');
  const publishedAt = card.getAttribute('data-video-date');
  
  openVideoModal(videoId, title, description, channelTitle, publishedAt);
}

function openVideoModal(videoId, title, description, channelTitle, publishedAt) {
  const modal = document.getElementById('videoModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalMeta = document.getElementById('modalMeta');
  const modalPlayer = document.getElementById('modalPlayer');
  const modalDescription = document.getElementById('modalDescription');
  const modalYouTubeLink = document.getElementById('modalYouTubeLink');
  
  // Set content
  modalTitle.textContent = title;
  modalMeta.innerHTML = `<strong>${channelTitle}</strong> • ${publishedAt}`;
  modalDescription.textContent = description;
  modalYouTubeLink.href = `https://www.youtube.com/watch?v=${videoId}`;
  
  // Create YouTube iframe
  modalPlayer.innerHTML = `
    <iframe 
      src="https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0" 
      style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
      allowfullscreen>
    </iframe>
  `;
  
  // Show modal
  modal.style.display = 'block';
  document.body.style.overflow = 'hidden';
}

function closeVideoModal() {
  const modal = document.getElementById('videoModal');
  const modalPlayer = document.getElementById('modalPlayer');
  
  // Clear iframe to stop video
  modalPlayer.innerHTML = '';
  
  // Hide modal
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}

// Close modal when clicking outside
window.onclick = function(event) {
  const modal = document.getElementById('videoModal');
  if (event.target === modal) {
    closeVideoModal();
  }
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeVideoModal();
  }
});
</script>

{% if site.data.videos.size == 0 %}
<div style="text-align: center; padding: 2em; color: #666;">
  <p>No videos found. Please check your YouTube API configuration.</p>
</div>
{% endif %}
