'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"version.json": "c3baed92020ab261923cd49f6cbfee92",
"index.html": "8a6931f2ce8054065a870e06f670b779",
"/": "8a6931f2ce8054065a870e06f670b779",
"main.dart.js": "34564963f1956f21beecb4db8519fb8d",
"flutter.js": "6fef97aeca90b426343ba6c5c9dc5d4a",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"manifest.json": "e442f00180b1df916f51cb1580706951",
"assets/AssetManifest.json": "05395969e262a2ad2251f79a5d609c24",
"assets/NOTICES": "926ac0a045b58703eafc4673bdc29ab2",
"assets/FontManifest.json": "13de329719c18fcdd1dce1a66f7e5763",
"assets/packages/font_awesome_flutter/lib/fonts/fa-solid-900.ttf": "d8e9b6203ce2657c991f0b339ccb3a6d",
"assets/packages/font_awesome_flutter/lib/fonts/fa-regular-400.ttf": "48ce1bb8a42776caa951cb782d277730",
"assets/packages/font_awesome_flutter/lib/fonts/fa-brands-400.ttf": "99f29024aee8f4672a47cc3a81b9b84a",
"assets/shaders/ink_sparkle.frag": "f8b80e740d33eb157090be4e995febdf",
"assets/AssetManifest.bin": "cb62db4d3ec4e067d52d09205db34d47",
"assets/fonts/circular-std-medium-500.ttf": "9475d6a0b79c164f9f605673714e75d9",
"assets/fonts/MaterialIcons-Regular.otf": "9bfd0ac394b038eacdf48d271a690c9b",
"assets/assets/ic_pump_off.png": "6fcd233709c0a08cc3ba78868db1792c",
"assets/assets/fan.png": "f3afc312e7ad50f0732d820f524eb679",
"assets/assets/ic_switchoff.png": "b3c6559430447a5b183834661375bea1",
"assets/assets/ic_socketon.png": "8321556a27e08140d2dd72263d8b0044",
"assets/assets/ic_room_office.png": "6712b63246bd1bb2a6b48f59a381ee19",
"assets/assets/ic_trash.png": "afe6a86a266d9ff06a47387b9383b554",
"assets/assets/ic_lighton.png": "3941ac61cb3dccae9e6e950d4d7517bc",
"assets/assets/help_arrow.png": "bd5984c0c86ce6ce1b7f82debe58d224",
"assets/assets/ic_room_bathroom.png": "ad8ef6fb0b721e77e3986d9bb60932b1",
"assets/assets/ic_scene.png": "a7e9b62ac3e97be614ec8d12fe731eca",
"assets/assets/ic_status_offline.png": "781c711accf2c218292f2f3c7089dd51",
"assets/assets/ic_room_livingroom.png": "c79c214481c10438d1047730ce93f142",
"assets/assets/ic_status_online.png": "6bc3832e88fd91f9965240f78c47445f",
"assets/assets/ic_switch_off.png": "b5af249825c5d0bf3fb21d5bd8bd8032",
"assets/assets/ic_fan.png": "dc646120e707851e3fb85c2aa5ec6a40",
"assets/assets/ic_add.png": "ac8e4b2d53927438f2b3c2d50b3875a5",
"assets/assets/ic_socketoff.png": "1aa102454a20274d5b391f853b601bdb",
"assets/assets/fan1.png": "244854296b75e804be7580058d0083ca",
"assets/assets/ic_mode_offline.png": "a2d9d41029c920ec652498bdc04aedd1",
"assets/assets/ic_router.png": "7a70d30e53613863354e832457b0bde1",
"assets/assets/arrow.png": "39a5f4a45c62af96857872bf44d55e0c",
"assets/assets/ic_room_other.png": "b8f74af1fbd63fb5f9d62acba95e691c",
"assets/assets/ic_switchon.png": "c55fdfefde1099af84dab7c7af91ad08",
"assets/assets/ic_room_bedroom.png": "16ef12b232d288854c7ac3f5a2e06912",
"assets/assets/lantern.png": "339cfcd6d8ebcc9197e10ad2d52e589a",
"assets/assets/ic_usage.png": "15b3590d3bf49444905351e4ad5c3794",
"assets/assets/temperature.png": "d59a6b8585a8b9a3c7c34b8a09a329e1",
"assets/assets/ic_valveoff.png": "78255171b8ab996de04fdc93cb1408db",
"assets/assets/ic_lightoff.png": "94ae904551d34632d17581570d2d66a6",
"assets/assets/ic_room_kitchen.png": "f42f262cfd893bdd742b498ecf2370e7",
"assets/assets/blue_bg.png": "ff984e0bfd20e2fa8fe6e57663f80523",
"assets/assets/man.jpg": "8183093b18817ab8a18adf551fcdd4a3",
"assets/assets/ic_edit.png": "c6120c3a1e810d520e3b58229725784d",
"assets/assets/ic_invite_friend.png": "457811e1615c20a06134a361fad48fef",
"assets/assets/help.png": "15a97764efefbfecbf5ed439e2b69e7e",
"assets/assets/ic_alerts.png": "103ffb2933d0f106b55839ab2d00638a",
"assets/assets/head.png": "00c2cad7fb4c2562c8502d9fba559236",
"assets/assets/ic_back.png": "bd30bcccff85d0ba55a7acd7a393123b",
"assets/assets/ic_speed_up.png": "f66796d31759437d8d2e59369288a4b0",
"assets/assets/ic_help.png": "b652e635d81323c235d52eb8943f156a",
"assets/assets/ic_forgot_pass.png": "b7a54f362145527a8e3af98312554bd3",
"assets/assets/ic_support.png": "441fa6e095d66a61cbf954f3c1d004e9",
"assets/assets/ic_pump_on.png": "d83b6e52d42b3733a2fd1349c0b920ba",
"assets/assets/edit.png": "c717ff0b0f1210e216b560fa163467df",
"assets/assets/ic_mode_online.png": "a5ae2ff38d06bad419e5f6066505cf0d",
"assets/assets/ic_speed_down.png": "417eceaccc7b6b6a700f4021036dcfc3",
"assets/assets/google.png": "77cb8f6971805b72c7cef1cb898a6df8",
"assets/assets/facebook.png": "9c8bf990645fc6189df6caedab34628c",
"assets/assets/humidity.png": "0257eb49def17da2ef3399f608c32f55",
"assets/assets/setting.png": "6a9c8c50f6ebce8491819196b606b4a9",
"canvaskit/skwasm.js": "1df4d741f441fa1a4d10530ced463ef8",
"canvaskit/skwasm.wasm": "6711032e17bf49924b2b001cef0d3ea3",
"canvaskit/chromium/canvaskit.js": "8c8392ce4a4364cbb240aa09b5652e05",
"canvaskit/chromium/canvaskit.wasm": "fc18c3010856029414b70cae1afc5cd9",
"canvaskit/canvaskit.js": "76f7d822f42397160c5dfc69cbc9b2de",
"canvaskit/canvaskit.wasm": "f48eaf57cada79163ec6dec7929486ea",
"canvaskit/skwasm.worker.js": "19659053a277272607529ef87acf9d8a"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"assets/AssetManifest.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
