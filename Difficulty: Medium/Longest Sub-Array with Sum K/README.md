<h2><a href="https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k">Longest Sub-Array with Sum K</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 20px;">Given an array <strong>arr</strong> containing <strong>n</strong> integers and an integer <strong>k</strong>. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value <strong>k</strong>. </span></p>
<p>&nbsp;</p>
<p><span style="font-size: 20px;"><strong>Examples:</strong></span><br>&nbsp;</p>
<div class="pieces-code-wrapper" style="text-align: left; width: 100%; margin-top: 10px;"><pre style="margin-bottom: 0px; margin-top: 0px;"><span style="font-size: 20px;"><strong>Input :
</strong>arr[] = {10, 5, 2, 7, 1, 9</span><span style="font-size: 20px;">}, k = 15
<strong>Output :</strong> 4
<strong>Explanation:
</strong>The sub-array is <strong>{5, 2, 7, 1}</strong>.
</span></pre><div class="pieces-btn-wrapper" style="border: none; display: flex; flex-direction: row; opacity: 0; width: auto; transition: opacity 0.3s ease-out; height: 26px; margin-top: 10px; margin-bottom: 10px;"><button class="pieces-btn pieces-copy-and-save" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px 6px 4px 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png" class="pieces-logo" style="margin: 0px 4px 0px 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px;"><span class="pieces-btn-text">Copy And Save</span></button><button class="pieces-btn pieces-share" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px 6px 4px 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/link.png" class="pieces-logo" style="margin: 0px 4px 0px 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px;"><span class="pieces-btn-text">Share</span></button><button class="pieces-btn pieces-ask-copilot" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px 6px 4px 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/copilot.png" class="pieces-logo" style="margin: 0px 4px 0px 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px;"><span class="pieces-btn-text">Ask Copilot</span></button><button class="pieces-btn pieces-settings" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/settings.png" class="pieces-logo" style="margin: 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px; max-width: 100%;"></button></div></div>
<div class="pieces-code-wrapper" style="text-align: left; width: 100%; margin-top: 10px;"><pre style="margin-bottom: 0px; margin-top: 0px;"><span style="font-size: 22px;"><strong>Input :</strong> 
arr[] = {-1, 2, 3}, k = 6</span>
<span style="font-size: 22px;"><strong>Output :</strong> 0
</span><span style="font-size: 20px;"><strong>Explanation: 
</strong></span><span style="font-size: 20px;">There is no such sub-array with sum 6.</span>
</pre><div class="pieces-btn-wrapper" style="border: none; display: flex; flex-direction: row; opacity: 0; width: auto; transition: opacity 0.3s ease-out; height: 26px; margin-top: 10px; margin-bottom: 10px;"><button class="pieces-btn pieces-copy-and-save" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px 6px 4px 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png" class="pieces-logo" style="margin: 0px 4px 0px 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px;"><span class="pieces-btn-text">Copy And Save</span></button><button class="pieces-btn pieces-share" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px 6px 4px 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/link.png" class="pieces-logo" style="margin: 0px 4px 0px 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px;"><span class="pieces-btn-text">Share</span></button><button class="pieces-btn pieces-ask-copilot" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px 6px 4px 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/copilot.png" class="pieces-logo" style="margin: 0px 4px 0px 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px;"><span class="pieces-btn-text">Ask Copilot</span></button><button class="pieces-btn pieces-settings" style="width: auto; font-size: 12px; border: 1px solid rgb(33, 33, 33); border-radius: 16px; margin-right: 4px; padding: 4px; line-height: normal; height: fit-content; cursor: pointer; user-select: none; display: flex; align-items: center; background-color: rgb(33, 33, 33); color: rgb(255, 255, 255);"><img src="https://storage.googleapis.com/pieces-web-extensions-cdn/settings.png" class="pieces-logo" style="margin: 0px; border-radius: 50%; filter: none; float: left; width: 16px; height: 16px; max-width: 100%;"></button></div></div>
<p><span style="font-size: 20px;"><strong>Expected Time Complexity:</strong> O(n).<br><strong>Expected Auxiliary Space:</strong> O(n).</span></p>
<p>&nbsp;</p>
<p><span style="font-size: 20px;"><strong>Constraints:</strong></span><br><span style="font-size: 20px;">1&lt;=n&lt;=10<sup>5</sup></span><br><span style="font-size: 20px;">-10<sup>5</sup>&lt;=arr[i], K&lt;=10<sup>5</sup></span><br>&nbsp;</p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Hash</code>&nbsp;<code>Map</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;