// 主要的 JavaScript 檔案

// 當 DOM 載入完成後執行
document.addEventListener('DOMContentLoaded', function() {
    // 初始化所有工具提示
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // 初始化所有彈出視窗
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // 註冊加入訂單按鈕事件
    document.querySelectorAll('.add-order-btn').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const foodId = this.dataset.foodId;
            const formId = this.dataset.formId;
            
            // 顯示輸入姓名的對話框
            const userName = prompt('請輸入您的姓名：');
            if (userName) {
                addOrder(formId, foodId, userName);
            }
        });
    });
});

// 新增訂單
async function addOrder(formId, foodId, userName) {
    try {
        showLoading();
        const response = await fetch(`/order/${formId}/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                food_id: foodId,
                user_name: userName,
                quantity: 1
            })
        });

        if (!response.ok) {
            throw new Error('訂餐失敗');
        }

        const data = await response.json();
        showSuccessMessage('訂餐成功！');
        updateStatistics();
    } catch (error) {
        showErrorMessage('訂餐失敗：' + error.message);
    } finally {
        hideLoading();
    }
}

// 更新統計資料
async function updateStatistics() {
    const statsContainer = document.getElementById('statistics-container');
    if (!statsContainer) return;

    try {
        const formId = statsContainer.dataset.formId;
        const response = await fetch(`/statistics/${formId}`);
        const data = await response.json();
        
        // 更新統計資料顯示
        renderStatistics(data);
    } catch (error) {
        console.error('更新統計資料失敗：', error);
    }
}

// 顯示載入動畫
function showLoading() {
    const loading = document.createElement('div');
    loading.className = 'loading';
    loading.innerHTML = '<i class="fas fa-spinner fa-spin fa-3x"></i>';
    document.body.appendChild(loading);
}

// 隱藏載入動畫
function hideLoading() {
    const loading = document.querySelector('.loading');
    if (loading) {
        loading.remove();
    }
}

// 顯示成功訊息
function showSuccessMessage(message) {
    showToast('success', message);
}

// 顯示錯誤訊息
function showErrorMessage(message) {
    showToast('danger', message);
}

// 顯示提示訊息
function showToast(type, message) {
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0 position-fixed bottom-0 end-0 m-3`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    document.body.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
}

// 動畫更新數字
function animateNumber(element, start, end, duration = 1000) {
    const range = end - start;
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const current = Math.floor(start + (range * progress));
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}